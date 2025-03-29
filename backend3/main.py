from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenWeather API Key from environment variables
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not OPENWEATHER_API_KEY:
    raise RuntimeError("OPENWEATHER_API_KEY is missing in .env file")

# Initialize FastAPI app
app = FastAPI(
    title="Weather Proxy API",
    description="Proxy server for securely fetching weather data from OpenWeather API.",
    version="1.0.0",
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production: specify frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/weather")
async def get_weather(city: str = Query(..., description="Name of the city to fetch weather for")):
    """
    Fetch weather data for the specified city using OpenWeather API.
    """
    if not city.strip():
        raise HTTPException(status_code=400, detail="City name is required.")

    # OpenWeather API endpoint
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}"

    try:
        # Fetch weather data
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Return relevant weather data
        return {
            "name": data.get("name"),
            "country": data["sys"].get("country"),
            "temperature": data["main"].get("temp"),
            "description": data["weather"][0].get("description"),
            "humidity": data["main"].get("humidity"),
        }
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="City not found.")
        else:
            raise HTTPException(status_code=500, detail=f"OpenWeather API error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")
