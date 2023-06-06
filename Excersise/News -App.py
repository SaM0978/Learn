# Importing Modules
import requests
import json
from newsapi import NewsApiClient

query = input("What Type Of News Do You Want\n")

url = f'https://newsapi.org/v2/everything?q={query}&from=2023-03-06&sortBy=publishedAt&apiKey=b0b0f913655f4afb96f2b629c4076eec'

req = requests.get(url)

news = json.loads(req.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print('------------------------------------------------------------------------------------------------------------------------')



















































































