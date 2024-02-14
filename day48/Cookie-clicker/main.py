from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

count = driver.find_element(By.XPATH, value='//*[@id="money"]')

cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')

cursor15 = driver.find_element(By.XPATH, value='//*[@id="buyCursor"]')
grandma100 = driver.find_element(By.XPATH, value='//*[@id="buyGrandma"]')
factory500 = driver.find_element(By.XPATH, value='//*[@id="buyFactory"]')
mine2000 = driver.find_element(By.XPATH, value='//*[@id="buyMine"]')
shipment7000 = driver.find_element(By.XPATH, value='//*[@id="buyShipment"]')
alchemy_lab50000 = driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]')
portal1000000 = driver.find_element(By.XPATH, value='//*[@id="buyPortal"]')
time_machine123456789 = driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]')

five_second = time.time() + 5
five_minute = time.time() + 300

actions = [
    (123456789, lambda: ActionChains(driver).double_click(time_machine123456789).perform(), 123456789),
    (10000000, lambda: ActionChains(driver).double_click(portal1000000).perform(), 10000000),
    (50000, lambda: ActionChains(driver).double_click(alchemy_lab50000).perform(), 50000),
    (7000, lambda: ActionChains(driver).double_click(shipment7000).perform(), 7000),
    (2000, lambda: ActionChains(driver).double_click(mine2000).perform(), 2000),
    (500, lambda: ActionChains(driver).double_click(factory500).perform(), 500),
    (100, lambda: ActionChains(driver).double_click(grandma100).perform(), 100),
    (15, lambda: ActionChains(driver).double_click(cursor15).perform(), 15),
]



while True:
    cookie.click()

    if time.time() > five_second:
        count = driver.find_element(By.XPATH, value='//*[@id="money"]')

        count = int(count.text)
        print(count)
        while count > 15:
            for threshold, action, decrement in actions:
                if count > threshold:
                    action()
                    count -= decrement

        five_second = time.time() + 5


    if time.time() > five_minute:
        print("end the game")
        break
