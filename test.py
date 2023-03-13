import time
from selenium import webdriver

driver = webdriver.Chrome('venv/chromedriver')
driver.get("https://www.yahoo.co.jp/")
time.sleep(5)
driver.quit()




