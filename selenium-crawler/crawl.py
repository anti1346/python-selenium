from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")

driver = webdriver.Remote(
    command_executor="http://selenium:4444/wd/hub",
    options=options
)

driver.get("http://scbyun.com")
print("Title:", driver.title)

links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print(link.text, link.get_attribute("href"))

driver.quit()