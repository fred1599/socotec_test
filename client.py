import requests

HEADERS = {"content-type": "application/json"}
URL_REVIEW = "http://127.0.0.1:8000/review/review_add/"
DATA_REVIEW = {"grade": 3, "name": "It Must Be Heaven", "text": "C'est un super film"}

client = requests.post(URL_REVIEW, json=DATA_REVIEW, headers=HEADERS)
print(client.json())
