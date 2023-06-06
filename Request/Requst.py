import requests
from bs4 import BeautifulSoup

url = 'https://www.codewithharry.com/blogpost/python-action-plan-to-learn-in-2023/'

r = requests.get(url)

# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')

print(soup.prettify())