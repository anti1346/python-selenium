from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
url = 'https://finance.naver.com/sise/sise_market_sum.nhn'
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

stocks = soup.select('#contentarea > div.box_type_l > table.type_2 > tbody > tr')

for stock in stocks:
    a_tag = stock.select_one('td:nth-child(2) > a')
    if a_tag is not None:
        price = stock.select_one('td:nth-child(3)').text
        name = a_tag.text
        row = {
            'name': name,
            'price': price
        }
        print(name, price)
        

driver.quit()