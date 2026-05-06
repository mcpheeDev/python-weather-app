import tkinter as tk
from tkinter import messagebox
import requests
import os

root = tk.Tk()
root.title("Weather App")

city_entry = tk.Entry(root)
city_entry.pack()

fetch_button = tk.Button(root, text="Get Weather")
fetch_button.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()

def fetch_weather():
    city = city_entry.get()
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    
    if not api_key:
        messagebox.showerror("Error", "API key not found. Set OPENWEATHER_API_KEY environment variable.")
        return
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        if response.status_code == 401:
            messagebox.showerror("Error", "Invalid or inactive API key.")
            return
        elif response.status_code == 404:
            messagebox.showerror("Error", "City not found.")
            return
        data = response.json()
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        weather_label.config(text=f"Temperature: {temperature}°C\nWeather: {weather}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

fetch_button.config(command=fetch_weather)
root.mainloop()
