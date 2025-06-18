import requests
from datetime import datetime
from flask import current_app

# Fetches current weather data for a given city using OpenWeatherMap API.
def fetch_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={current_app.config['API_KEY']}&units=metric"
    res = requests.get(url)
    data = res.json()
    return data if str(data.get("cod")) == "200" else None

# Gets current weather information for a specified city of temperature and description.
def get_weather(city):
    data = fetch_weather_data(city)
    if not data:
        return f"Sorry, I couldn't find weather for '{city}'. Can you please check the spelling or try again?"

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    suggestion = (
        "It's hot today, stay hydrated! 🥵" if temp > 30 else
        "Mild and pleasant! 🙂" if temp > 20 else
        "Cool weather, grab a jacket. 🧥" if temp > 10 else
        "It's cold, dress warmly. 🧣"
    )
    emoji = "☀️" if "clear" in desc else "🌧️" if "rain" in desc else "☁️" if "cloud" in desc else "❄️" if "snow" in desc else "🌫️"

    return f"{emoji} Weather in {city.title()} is currently {desc}, with a temperature of {temp}°C.\n{suggestion}"

# Gets specific weather field information for a city.
def get_field_info(city, field):
    data = fetch_weather_data(city)
    if not data:
        return f"Sorry, I couldn't find data for '{city}'."

    fields = {
        "temperature": lambda: f"Temperature is {data['main']['temp']}°C. Feels like {data['main']['feels_like']}°C.",
        "pressure": lambda: f"🔽 Pressure is {data['main']['pressure']} hPa.",
        "humidity": lambda: f"💧 Humidity is {data['main']['humidity']}%.",
        "visibility": lambda: f"👁️ Visibility is {data.get('visibility', 0) / 1000:.1f} km.",
        "wind": lambda: f"💨 Wind is {round(data['wind']['speed'] * 2.23694, 1)} mph, direction {data['wind'].get('deg', 'N/A')}°.",
        "cloudiness": lambda: f"☁️ Cloudiness is {data['clouds']['all']}%.",
        "rain": lambda: f"🌧️ Rain was {data.get('rain', {}).get('1h', 0)} mm in last hour.",
        "snow": lambda: f"❄️ Snow was {data.get('snow', {}).get('1h', 0)} mm in last hour.",
        "precipitation": lambda: f"🌧️ Rain: {data.get('rain', {}).get('1h', 0)} mm | ❄️ Snow: {data.get('snow', {}).get('1h', 0)} mm."
    }
    return fields.get(field, lambda: "Sorry, I can't retrieve that weather data currently.")()

# Gets a 3-day weather forecast for a specified city.
def get_forecast(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={current_app.config['API_KEY']}&units=metric"
    res = requests.get(url)
    data = res.json()
    if data.get("cod") != "200":
        return f"Sorry, I couldn't find the forecast for '{city}'."

    daily = {}
    offset = data["city"]["timezone"]

    for entry in data["list"]:
        dt = datetime.utcfromtimestamp(entry["dt"] + offset)
        day = dt.date()
        daily.setdefault(day, {"temps": [], "conditions": []})
        daily[day]["temps"].append(entry["main"]["temp"])
        daily[day]["conditions"].append(entry["weather"][0]["main"].lower())

    today = datetime.utcnow().date()
    forecast_days = [d for d in sorted(daily.keys()) if d > today][:3]

    result = [f"🌤️ 3-day forecast for {city.title()}:"]
    for day in forecast_days:
        avg = round(sum(daily[day]["temps"]) / len(daily[day]["temps"]), 1)
        condition = max(set(daily[day]["conditions"]), key=daily[day]["conditions"].count)
        emoji = "☀️" if "clear" in condition else "🌧️" if "rain" in condition else "☁️" if "cloud" in condition else "❄️" if "snow" in condition else "🌫️"
        result.append(f"{day.strftime('%A')}: {emoji} {condition.title()}, {avg}°C")
    return "\n".join(result)

# Gets sunrise and sunset times for a specified city.
def get_sun_times(city):
    data = fetch_weather_data(city)
    if not data:
        return f"Sorry, I couldn't find the sunrise/sunset times for '{city}'."
    offset = data["timezone"]
    sunrise = datetime.utcfromtimestamp(data["sys"]["sunrise"] + offset).strftime("%H:%M")
    sunset = datetime.utcfromtimestamp(data["sys"]["sunset"] + offset).strftime("%H:%M")
    return f"🌅 Sunrise in {city.title()} is at {sunrise}. 🌇 Sunset is at {sunset}."
