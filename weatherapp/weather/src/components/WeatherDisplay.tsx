import React from "react";
import { useSelector } from "react-redux";
import { RootState } from "../redux/store";

const WeatherDisplay: React.FC = () => {
  const { data, loading, error } = useSelector((state: RootState) => state.weather);

  if (loading) {
    return <p>Loading weather data...</p>;
  }

  if (error) {
    return <p style={{ color: "red" }}>Error: {error}</p>;
  }

  // Handle empty or undefined weather data
  if (!data) {
    return <p>No weather data available. Please search for a city.</p>;
  }


  return (
    <div className="weather-display">
      <h2>Weather in {data.name}, {data.country}</h2>
      <p>Temperature: {(data.temperature - 273.15).toFixed(2)}°C</p>
      <p>Humidity: {data.humidity}%</p>
      <p>Description: {data.description}</p>
    </div>
  );
};

export default WeatherDisplay;
