from bs4 import BeautifulSoup
import requests

res = requests.get('https://sangchul.kr')

soup = BeautifulSoup(res.text, "lxml")

print("=" * 60)
for each_tag in soup.find_all("span", {"class": "title"}):
    print(each_tag.text)
print("=" * 60)