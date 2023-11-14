import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
def fetch_api_data():
    response = requests.get(url).json()
    image_url = response['url']
    explanation = response['explanation']
    title = response['title']
    return title,image_url,explanation

if __name__ == "__main__":
    title,url,e = fetch_api_data()
    print(title)