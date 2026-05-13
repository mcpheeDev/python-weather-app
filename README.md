# python-weather-app

A modern, feature-rich desktop weather application built with Python and Tkinter, using the OpenWeatherMap API to fetch real-time weather data for any city.

---

## 🌤️ Features

- **Beautiful Dark-Themed UI** — Modern dark theme with accent colors for a professional look
- **Search by City** — Enter any city name to get real-time weather data
- **Comprehensive Weather Info**
  - Current temperature in °C
  - Weather description with emoji icons
  - "Feels like" temperature
  - Humidity percentage
  - Wind speed in km/h
  - Location with country code
- **Weather Emoji Icons** — Visual indicators for conditions (clear, cloudy, rainy, snowy, etc.)
- **Responsive Error Handling** — User-friendly error messages for invalid cities, network issues, and API errors
- **Focus-aware Input Field** — Smart placeholder text that clears on focus

---

## 🔄 Recent Changes

The app has been completely redesigned with significant UI/UX improvements over the original version:

- **Enhanced UI**: Custom color palette with modern dark theme instead of default Tkinter styling
- **Better Typography**: Multiple font styles for hierarchy (titles, labels, descriptions)
- **Rich Weather Display**: Shows temperature, feels-like temp, humidity, and wind speed in an organized card layout
- **Visual Feedback**: Weather-specific emoji icons and professional status indicators
- **Improved Error Handling**: Status bar with clear error messages instead of popup dialogs
- **Better Layout**: Organized sections (header, search bar, weather card, status)
- **Smoother UX**: Focus-aware entry field with placeholder text, keyboard support (Enter to search)

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
   pip install requests
   ```

3. **Run the app**
   ```bash
   python test.py
   ```

---

## Usage

1. Enter a city name in the input field (e.g., "London", "Tokyo", "New York")
2. Click **GET WEATHER** or press Enter
3. View the current temperature, conditions, humidity, wind speed, and more

---

## Project Structure

```
python-weather-app/
├── test.py          # Main application (redesigned version)
├── README.md        # Project documentation
└── .gitignore       # Git ignore rules
```

---

## Built With

- [Python](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — GUI framework
- [Requests](https://pypi.org/project/requests/) — HTTP library
- [OpenWeatherMap API](https://openweathermap.org/api) — Weather data

---

## License

This project is open source and available under the MIT License.
