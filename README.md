# python-weather-app
My first python project, a weather app.

# 🌤️ Python Weather App

A simple desktop weather application built with Python and Tkinter, using the OpenWeatherMap API to fetch real-time weather data for any city.

> Built following the guide by [BuddyMinds on Medium](https://medium.com/@buddyminds/creating-a-weather-application-in-python-a-step-by-step-guide-b14152cc936a), with additional improvements including environment variable handling and better error management.

---

## Features

- Search weather by city name
- Displays current temperature in °C
- Shows weather description (e.g. light rain, clear sky)
- Friendly error messages for invalid cities or API issues
- API key stored securely via environment variables

---

## Prerequisites

- Python 3.x
- A free API key from [OpenWeatherMap](https://openweathermap.org/api)

---

## Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/mcpheeDev/python-weather-app.git
   cd python-weather-app
   ```

2. **Install dependencies**
   ```bash
   pip install requests python-dotenv
   ```

3. **Set up your API key**

   Create a `.env` file in the project root:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```
   You can use `.env.example` as a template.

4. **Run the app**
   ```bash
   python main.py
   ```

---

## Usage

1. Enter a city name in the input field
2. Click **Get Weather**
3. View the current temperature and conditions

---

## Project Structure

```
python-weather-app/
├── main.py          # Main application
├── .env             # Your API key (not committed)
├── .env.example     # Template for API key setup
├── .gitignore       # Ensures .env is never pushed
└── README.md
```

---

## Built With

- [Python](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — GUI framework
- [Requests](https://pypi.org/project/requests/) — HTTP library
- [OpenWeatherMap API](https://openweathermap.org/api) — Weather data

---

## Acknowledgements

- Tutorial by [BuddyMinds on Medium](https://medium.com/@buddyminds/creating-a-weather-application-in-python-a-step-by-step-guide-b14152cc936a)
