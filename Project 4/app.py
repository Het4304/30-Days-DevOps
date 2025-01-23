from flask import Flask, jsonify ,render_template
import requests
import os

app = Flask(__name__)

SERP_API_URL = "https://api.sportsdata.io/v3/nfl/scores/json/ScoresByDate/2025-01-19?"
SERP_API_KEY = os.getenv("SPORTS_API_KEY")

@app.route('/', methods=['GET'])
def get_nfl_schedule():
    #Fetches the NFL schedule from SportsDATAAPI and returns it as JSON
    try:
        # Query SerpAPI
        params = {
            "key": SERP_API_KEY
        }
        response = requests.get(SERP_API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        return jsonify({"message": "An error occurred.", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)