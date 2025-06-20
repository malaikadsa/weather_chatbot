# Project: AI Use Case - Weather Chatbot

## Description

A simple and interactive weather chatbot built with **Python**, **Flask** and the **OpenWeatherMap API**. Users can type weather related queries to get real-time weather information and forecasts for any city.

## Installation

Installation presumes an existing Python installation.
### 1. Clone the Repository

```bash
git clone https://github.com/malaikadsa/weather_chatbot.git
cd weather_chatbot
```
### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # On Unix/macOS
venv\Scripts\activate           # On Windows
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. Train the Model

```bash
python models/train_intent_model.py
```
### 5. Add API Key to .env
Open the .env file and add your OpenWeatherMap API key. You can get your OpenWeatherMap key [here](https://home.openweathermap.org/api_keys). Finally, the file should look like this:
```bash
OPENWEATHER_API_KEY=your_openweathermap_api_key
```
### 6. Run the App
To start the chatbot interface on your machine execute the following command:
```bash
python run.py
```
This will initiate a local server at http://127.0.0.1:5000. To start chatting with the chatbot, simply open this URL in your browser.

## Example

Type in your weather related query and click on the arrow or press enter. <br>
You can ask things like: <br>
"What's the weather in Paris?" <br>
"Tell me the humidity in New York." <br>
"When is sunset in Mumbai?" <br>
"What’s the forecast for the next few days in Madrid?" <br>
"What's the wind speed in Chicago?" <br>

## 📦 Features

- 🌦️ Current weather conditions like temperature, pressure, humidity, wind, visibility, cloudiness, rain, snow.
- 📅 3-day forecast summaries.
- 🌅 Sunrise and Sunset times.

## References
* [Python](https://www.python.org)
* [OpenWeatherMap API documentation](https://openweathermap.org/api)
* [Flask documentation](https://flask.palletsprojects.com)
* [Scikit-learn: Machine learning in Python](https://scikit-learn.org)
* [CSS: Cascading Style Sheets](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [HTML: HyperText Markup Language](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [JavaScript guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript)