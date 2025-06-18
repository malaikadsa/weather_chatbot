from flask import Blueprint, render_template, request, jsonify
from .intent import predict_intent, extract_city
from .weather import get_weather, get_field_info, get_forecast, get_sun_times

main = Blueprint("main", __name__)

# Main chat interface
@main.route("/")
def index():
    return render_template("index.html")

# Handles user input and returns a response
@main.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json.get("message", "")
    lowered = user_input.lower()
    city = extract_city(user_input)
    intent = predict_intent(user_input)

    if intent == "weather_now":
        response = get_weather(city) if city else "Please specify a city."
    elif intent in {"temperature", "pressure", "humidity", "visibility", "wind", "cloudiness", "rain", "snow", "precipitation"}:
        response = get_field_info(city, intent) if city else f"Please tell me which city you would like the {intent} information for."
    elif intent == "forecast":
        response = get_forecast(city) if city else "Which city would you like the forecast for?"  
    elif intent == "sun_times":
        response = get_sun_times(city) if city else "Tell me which city you would like the sunrise/sunset times for."
    elif intent == "greeting":
        response = "Hello! I'm Sunny 🌞, your friendly weather bot. Ask me about the weather!"
    elif intent == "thanks":
        response = "You're welcome! Stay safe and weather-aware! 😊"
    elif intent == "how_are_you":
        response = "I'm sunny as ever! ☀️ How can I help you today?"
    elif intent == "who_are_you":
        response = "I'm Sunny ☀️ – your friendly weather chatbot."
    elif intent == "hourly_forecast":
        response = "Hourly weather updates aren’t available yet, but they are on the way! ⏳ Stay tuned. 😊"
    else:
        response = "Sorry, I didn’t understand that. I can only answer weather-related questions."

    return jsonify({"response": response})
