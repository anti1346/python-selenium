import requests
from bs4 import BeautifulSoup

res = requests.get('https://sangchul.kr')

soup = BeautifulSoup(res.text, "lxml")

text = soup.find_all('title')
print(text)

