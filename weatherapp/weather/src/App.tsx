import React from "react";
import SearchBar from "./components/SearchBar";
import WeatherDisplay from "./components/WeatherDisplay";
import { Provider } from "react-redux";
import { store } from "./redux/store";
import "./styles.css";

const App: React.FC = () => {
  return (
    <Provider store={store}>
    <div className="app">
      <h1>Weather App</h1>
      <SearchBar />
      <WeatherDisplay />
      
    </div>
    </Provider>
  );
};

export default App;
