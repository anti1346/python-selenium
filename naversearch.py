from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime

#웹드라이버 설정
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)


driver.implicitly_wait(time_to_wait=5)

driver.get("https://www.naver.com")

element = driver.find_element(By.ID, 'query')
element.send_keys("변군이글루")
element.send_keys(Keys.ENTER)
time.sleep(7)

# element1 = driver.find_element(By.XPATH, '//*[@id="web_1"]/div[1]/div[2]/div[2]/a')
element1 = driver.find_element(By.XPATH, '//*[@id="web_1"]/div[1]/div[2]/div[2]/a')
element1.send_keys(Keys.RETURN)
time.sleep(10)

element2 = driver.find_element(By.XPATH, '/html/body/div[2]/section/article/div[2]/div[1]/a')
element2.send_keys(Keys.RETURN)
time.sleep(10)