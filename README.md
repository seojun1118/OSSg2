# Simple Weather Information App

## Project Overview
This program uses the OpenWeatherMap API to provide real-time weather information for a city entered by the user. Users can input the name of a city and receive details such as the current temperature, humidity, and weather conditions.

## Features
- Fetch and display real-time weather information for a user-specified city.
- Display temperature (Celsius), humidity, and weather conditions.
- Leverage the OpenWeatherMap API for data retrieval.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/username/weather-app.git
   cd weather-app
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Obtain an API key from OpenWeatherMap and add it to the `main.py` file:
   ```python
   api_key = "YOUR_API_KEY"
   ```

## Usage
1. Run the program:
   ```bash
   python main.py
   ```

2. Enter the name of the city for which you want to check the weather:
   ```
   Enter the city name: Seoul
   ```

3. Example output:
   ```
   Weather in Seoul:
   Temperature: 22°C
   Humidity: 60%
   Weather: Clear Sky
   ```

## Requirements
- `requests`: To handle API requests.

## References
- OpenWeatherMap API: [https://openweathermap.org/](https://openweathermap.org/)

