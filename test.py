import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome('venv/chromedriver')
driver.get("https://www.yahoo.co.jp/")
time.sleep(5)


## 検索
def search(word):
    # "p"は検索ボックスのname
    element = driver.find_element(By.TAG_NAME, "p")
    element.click()

search("Selenium")



driver.quit()




