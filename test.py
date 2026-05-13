import os
import tkinter as tk
from tkinter import ttk
import requests

# ── Palette ──────────────────────────────────────────────
BG          = "#0f1923"
CARD        = "#1a2635"
ACCENT      = "#4fc3f7"
ACCENT_DIM  = "#1a3a4a"
TEXT        = "#e8f4fd"
SUBTEXT     = "#7a9ab5"
ERROR_COL   = "#ef5350"
FONT_TITLE  = ("Georgia", 22, "bold")
FONT_LABEL  = ("Courier New", 11)
FONT_SMALL  = ("Courier New", 9)
FONT_TEMP   = ("Georgia", 48, "bold")
FONT_DESC   = ("Georgia", 14, "italic")
FONT_BTN    = ("Courier New", 11, "bold")

WEATHER_ICONS = {
    "clear": "☀️", "cloud": "☁️", "rain": "🌧️",
    "drizzle": "🌦️", "thunder": "⛈️", "snow": "❄️",
    "mist": "🌫️", "fog": "🌫️", "haze": "🌫️",
    "smoke": "🌫️", "dust": "🌫️", "tornado": "🌪️",
}

def get_icon(description: str) -> str:
    desc = description.lower()
    for key, icon in WEATHER_ICONS.items():
        if key in desc:
            return icon
    return "🌡️"

# ── Root ─────────────────────────────────────────────────
root = tk.Tk()
root.title("Weather")
root.configure(bg=BG)
root.resizable(False, False)
root.geometry("360x520")

# ── Header ───────────────────────────────────────────────
header = tk.Frame(root, bg=BG, pady=24)
header.pack(fill="x")

tk.Label(header, text="WEATHER", font=FONT_TITLE,
         bg=BG, fg=ACCENT).pack()
tk.Label(header, text="real-time conditions", font=FONT_SMALL,
         bg=BG, fg=SUBTEXT).pack()

# ── Search bar ───────────────────────────────────────────
search_frame = tk.Frame(root, bg=BG, padx=28)
search_frame.pack(fill="x")

entry_wrap = tk.Frame(search_frame, bg=CARD,
                      highlightbackground=ACCENT_DIM,
                      highlightthickness=1, bd=0)
entry_wrap.pack(fill="x", pady=(0, 12))

tk.Label(entry_wrap, text="📍", bg=CARD, fg=SUBTEXT,
         font=("Courier New", 12), padx=8).pack(side="left")

city_entry = tk.Entry(entry_wrap, font=FONT_LABEL,
                      bg=CARD, fg=TEXT, insertbackground=ACCENT,
                      bd=0, relief="flat",
                      highlightthickness=0)
city_entry.pack(side="left", fill="x", expand=True, ipady=10)
city_entry.insert(0, "Enter city…")

def on_focus_in(e):
    if city_entry.get() == "Enter city…":
        city_entry.delete(0, "end")
        city_entry.config(fg=TEXT)

def on_focus_out(e):
    if not city_entry.get():
        city_entry.insert(0, "Enter city…")
        city_entry.config(fg=SUBTEXT)

city_entry.bind("<FocusIn>", on_focus_in)
city_entry.bind("<FocusOut>", on_focus_out)
city_entry.config(fg=SUBTEXT)

# ── Fetch button ─────────────────────────────────────────
fetch_btn = tk.Button(search_frame, text="GET WEATHER",
                      font=FONT_BTN, bg=ACCENT, fg=BG,
                      bd=0, relief="flat", cursor="hand2",
                      activebackground="#81d4fa", activeforeground=BG,
                      padx=0, pady=10)
fetch_btn.pack(fill="x")

# ── Divider ──────────────────────────────────────────────
tk.Frame(root, bg=ACCENT_DIM, height=1).pack(fill="x", padx=28, pady=20)

# ── Weather card ─────────────────────────────────────────
card_outer = tk.Frame(root, bg=BG, padx=28)
card_outer.pack(fill="x")

card = tk.Frame(card_outer, bg=CARD,
                highlightbackground=ACCENT_DIM,
                highlightthickness=1)
card.pack(fill="x")

icon_lbl  = tk.Label(card, text="", font=("Segoe UI Emoji", 48),
                     bg=CARD, pady=16)
icon_lbl.pack()

temp_lbl  = tk.Label(card, text="", font=FONT_TEMP,
                     bg=CARD, fg=TEXT)
temp_lbl.pack()

desc_lbl  = tk.Label(card, text="", font=FONT_DESC,
                     bg=CARD, fg=SUBTEXT, pady=4)
desc_lbl.pack()

details_frame = tk.Frame(card, bg=CARD, pady=12)
details_frame.pack()

feels_lbl    = tk.Label(details_frame, text="", font=FONT_SMALL,
                        bg=CARD, fg=SUBTEXT)
feels_lbl.pack()
humidity_lbl = tk.Label(details_frame, text="", font=FONT_SMALL,
                        bg=CARD, fg=SUBTEXT)
humidity_lbl.pack()
wind_lbl     = tk.Label(details_frame, text="", font=FONT_SMALL,
                        bg=CARD, fg=SUBTEXT)
wind_lbl.pack(pady=(0, 12))

# ── Status bar ───────────────────────────────────────────
status_lbl = tk.Label(root, text="", font=FONT_SMALL,
                      bg=BG, fg=SUBTEXT, pady=8)
status_lbl.pack()

# ── Logic ─────────────────────────────────────────────────
def set_error(msg: str):
    status_lbl.config(text=f"⚠  {msg}", fg=ERROR_COL)
    icon_lbl.config(text="")
    temp_lbl.config(text="")
    desc_lbl.config(text="")
    feels_lbl.config(text="")
    humidity_lbl.config(text="")
    wind_lbl.config(text="")

def fetch_weather():
    city = city_entry.get().strip()
    if not city or city == "Enter city…":
        set_error("Please enter a city name.")
        return

    api_key = "b523aa7d78063897605879a0ca9c8e45"
    if not api_key:
        set_error("OPENWEATHER_API_KEY env var not set.")
        return

    fetch_btn.config(text="LOADING…", state="disabled")
    status_lbl.config(text="", fg=SUBTEXT)
    root.update_idletasks()

    try:
        url = (f"https://api.openweathermap.org/data/2.5/weather"
               f"?q={city}&appid={api_key}&units=metric")
        r = requests.get(url, timeout=10)

        if r.status_code == 401:
            set_error("Invalid API key.")
            return
        if r.status_code == 404:
            set_error(f'City "{city}" not found.')
            return
        r.raise_for_status()

        d    = r.json()
        temp = round(d["main"]["temp"])
        desc = d["weather"][0]["description"].capitalize()
        feel = round(d["main"]["feels_like"])
        hum  = d["main"]["humidity"]
        wind = round(d["wind"]["speed"] * 3.6)  # m/s → km/h
        name = d["name"]
        country = d["sys"]["country"]

        icon_lbl.config(text=get_icon(desc))
        temp_lbl.config(text=f"{temp}°C")
        desc_lbl.config(text=desc)
        feels_lbl.config(text=f"Feels like {feel}°C")
        humidity_lbl.config(text=f"Humidity  {hum}%")
        wind_lbl.config(text=f"Wind  {wind} km/h")
        status_lbl.config(text=f"{name}, {country}", fg=SUBTEXT)

    except requests.exceptions.ConnectionError:
        set_error("No internet connection.")
    except Exception as e:
        set_error(str(e))
    finally:
        fetch_btn.config(text="GET WEATHER", state="normal")

fetch_btn.config(command=fetch_weather)
city_entry.bind("<Return>", lambda e: fetch_weather())

root.mainloop()
