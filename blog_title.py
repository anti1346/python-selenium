import requests
from bs4 import BeautifulSoup

res = requests.get('https://sangchul.kr')
soup = BeautifulSoup(res.text, "lxml")

# print(soup.title.string)
titles = soup.find_all('title')
for title in titles:
    print(title.text)