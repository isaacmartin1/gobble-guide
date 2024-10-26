import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Access the API key from the environment
google_api_key = os.getenv("GOOGLE_API_KEY")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/restaurants", methods=["POST"])
def search_restaurants():
    data = request.get_json()
    text_query = data.get("textQuery")

    google_api_url = "https://places.googleapis.com/v1/places:searchText"
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": google_api_key,
        "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.priceLevel"
    }
    payload = {
        "textQuery": text_query
    }

    response = requests.post(google_api_url, headers=headers, json=payload)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to retrieve data from Google Places API"}), response.status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
