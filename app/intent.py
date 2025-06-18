import pickle
from sentence_transformers import SentenceTransformer
import os
import re

MODEL_DIR = "models"

# Loads the trained intent classification model
with open(os.path.join(MODEL_DIR, "intent_model.pkl"), "rb") as f:
    clf = pickle.load(f)

# Loads the SentenceTransformer model name used for embedding
with open(os.path.join(MODEL_DIR, "embedder_name.pkl"), "rb") as f:
    embedder_name = pickle.load(f)

# Initialize the SentenceTransformer model for text embedding
embedder = SentenceTransformer(embedder_name)

# Function to predict the intent of a given text
def predict_intent(text):
    embedding = embedder.encode([text])
    intent = clf.predict(embedding)[0]
    return intent

# Function to extract the city name from a given text
def extract_city(text):
    match = re.search(r"\bin\s+([a-zA-Z\s]+)", text.lower())
    if match:
        return match.group(1).strip().title()
    tokens = text.split()
    city_tokens = [w for w in tokens if w.istitle() and w.lower() != "in"]
    return " ".join(city_tokens) if city_tokens else None