import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def neos_page(page):

    url = "https://api.nasa.gov/neo/rest/v1/neo/browse"

    params = {
        "api_key": API_KEY,
        "page": page
    }

    response = requests.get(url, params=params)
    return response.json()