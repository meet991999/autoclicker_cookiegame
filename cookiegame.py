from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

chrome_driver = "D:\Meet\day 48 automation\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver)
driver = webdriver.Chrome(service=service)
# using  driver = webdriver.Chrome(executable_path=chrome_driver) gives DeprecationWarning
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.XPATH,'//*[@id="cookie"]')
upgrades_id = ["buyTime machine", "buyPortal", "buyAlchemy lab", "buyShipment", "buyMine", "buyFactory",
               "buyGrandma", "buyCursor"]

clicks = 60
timeout = time.time() + (60*5)

while time.time() <= timeout:
    for _ in range(clicks):
        cookie.click()

    for upgrade_id in upgrades_id:
        try:
            driver.find_element(By.ID,upgrade_id).click()
        except:
            continue

    clicks += 60

cps = driver.find_element(By.ID,"cps").text
print(cps)

driver.quit()

