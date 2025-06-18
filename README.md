# Project: AI Use Case - Weather Chatbot

## Description

A simple and interactive weather chatbot built with **Python**, **Flask** and the **OpenWeatherMap API**. Users can type weather related queries to get real-time weather information and forecasts for any city.

## 📦 Features

- 🌦️ Current weather conditions.
- 🔍 Detailed information like humidity, wind, visibility, etc.
- 📅 3-day forecast summaries.
- 🌅 Sunrise and Sunset times.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/malaikadsa/weather_chatbot.git
cd weather_chatbot
```
### 2. Create and Activate a Virtual Environment
It is recommended to use Python=3.10.
```bash
python -m venv venv
source venv/bin/activate        # On Unix/macOS
venv\Scripts\activate           # On Windows
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. Add API Key to .env
Open the .env file and add your OpenWeatherMap API key. You can get your OpenWeatherMap key [here](https://home.openweathermap.org/api_keys). Finally, the file should look like this:
```bash
OPENWEATHER_API_KEY=your_openweathermap_api_key
```
### 5. Run the App
To start the chatbot interface on your machine execute the following command:
```bash
python run.py
```
This will initiate a local server at http://127.0.0.1:5000. To start chatting with the chatbot, simply open this URL in your browser.

## References
* [Python](https://www.python.org)
* [OpenWeatherMap API documentation](https://openweathermap.org/api)
* [Flask documentation](https://flask.palletsprojects.com)
* [Scikit-learn: Machine learning in Python](https://scikit-learn.org)
* [CSS: Cascading Style Sheets](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [HTML: HyperText Markup Language](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [JavaScript guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript)