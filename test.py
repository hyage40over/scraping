import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('venv/chromedriver')
driver.get("https://www.yahoo.co.jp/")

time.sleep(5)

# "p"は検索ボックスのname
element = driver.find_element(By.TAG_NAME, "p")
element.clear()
element.send_keys("技術士")

driver.find_element_by_type("submit").click()



driver.quit()




