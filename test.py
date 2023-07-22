
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs

# CHROMEDRIVER = "C:\data\etc\chromedriver.exe"
CHROMEDRIVER = "venv\chromedriver"

chrome_service = fs.Service(executable_path=CHROMEDRIVER)
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.yahoo.co.jp/")

txt = driver.find_element(By.NAME, "p")
txt.send_keys("技術士")
txt.send_keys(Keys.ENTER)

time.sleep(5)

driver.quit()