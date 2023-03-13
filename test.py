import time
from selenium import webdriver

driver = webdriver.Edge(executable_path="msedgedriver.exe")
driver.get("https://www.yahoo.co.jp/")
time.sleep(5)
driver.quit()