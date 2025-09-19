import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_address_suggestions(input_text: str) -> list:
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    url = "https://maps.googleapis.com/maps/api/place/autocomplete/json"
    params = {
        "input": input_text,
        "key": api_key,
        "types": "address",
        "components": "country:us"
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data["status"] != "OK":
        return []
    return [item["description"] for item in data["predictions"]]