# Weather Application

## Overview
This Weather Application is a full-stack project that allows users to fetch and display real-time weather data for any city. The app leverages a FastAPI backend as a proxy server for OpenWeather API requests and a React frontend to display the weather data. The application uses Redux Toolkit for state management and is designed to be user-friendly and efficient.

---

## Features
- **Search Weather**: Enter a city name to fetch its current weather conditions.
- **Real-time Data**: Displays temperature, humidity, weather description, and the city name.
- **Loading State**: Shows a loading spinner or message during API requests.
- **Error Handling**: Displays user-friendly error messages for invalid city names or server errors.

---

## Technologies Used
### Frontend:
- React
- TypeScript
- Redux Toolkit
- Axios
- Tailwind CSS (optional, for styling)

### Backend:
- FastAPI
- Python
- Requests
- dotenv (for environment variable management)

### External API:
- OpenWeather API

---

## Installation

### Prerequisites
Ensure the following are installed on your system:
- Node.js (LTS recommended)
- Python (>= 3.9)

### Clone the Repository
```bash
$ git clone https://github.com/your-username/weather-app.git
$ cd weather-app
```

### Backend Setup
1. Navigate to the `backend` folder:
   ```bash
   $ cd backend
   ```

2. Install dependencies:
   ```bash
   $ pip install -r requirements.txt
   ```

3. Create a `.env` file in the `backend` directory and add your OpenWeather API key:
   ```env
   OPENWEATHER_API_KEY=your_openweather_api_key
   ```

4. Run the backend server:
   ```bash
   $ uvicorn main:app --reload
   ```
   The backend will be available at `http://127.0.0.1:8080`.

### Frontend Setup
1. Navigate to the `frontend` folder:
   ```bash
   $ cd ../frontend
   ```

2. Install dependencies:
   ```bash
   $ npm install
   ```

3. Start the React development server:
   ```bash
   $ npm start
   ```
   The frontend will be available at `http://localhost:3000`.

---

## Usage
1. Open the application in your browser at `http://localhost:3000`.
2. Enter the name of a city in the search bar.
3. Click the "Search" button to fetch weather data.
4. View the weather information displayed, including temperature, humidity, and description.

---

## File Structure
```
weather-app/
├── backend/
│   ├── main.py         # FastAPI backend implementation
│   ├── .env            # Environment variables
│   ├── requirements.txt # Backend dependencies
│   └── ...
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── SearchBar.tsx       # Search bar component
│   │   │   ├── WeatherDisplay.tsx  # Weather display component
│   │   ├── redux/
│   │   │   ├── store.ts           # Redux store
│   │   │   ├── weatherSlice.ts    # Weather slice
│   │   └── App.tsx                # Main React app
│   ├── public/
│   └── package.json
└── README.md
```

---

## API Endpoints
### Backend:
- **`GET /api/weather?city={city}`**
  - **Description**: Fetches weather data for the specified city.
  - **Query Parameters**:
    - `city` (string): The name of the city.
  - **Response**:
    ```json
    {
      "name": "Hyderabad",
      "country": "IN",
      "temperature": 309.26,
      "description": "clear sky",
      "humidity": 16
    }
    ```

---

## Known Issues
- Ensure the `.env` file is correctly configured.
- Cross-origin errors may occur if CORS is not properly configured for production.

---

## Future Enhancements
- Add a 5-day weather forecast feature.
- Implement unit selection (Celsius/Fahrenheit).
- Improve UI/UX with more detailed weather visuals.

---

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

## Contact
For questions or feedback, please contact:
- **Your Name**
- **Email**: your-email@example.com
- **GitHub**: [your-username](https://github.com/your-username)

