import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

EMAIL = "email@twitter.com"
PASSWORD = "motdepasse"
CLICK_TIMER = 5
has_clicked = False
current_time = datetime.now()
service = Service("C:\Development\chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.get("https://www.binance.com/en/activity/bitcoin-button-game")
driver.maximize_window()
time.sleep(3)

authorized_cookies = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
authorized_cookies.click()
time.sleep(1)

sign_in_button = driver.find_element(By.XPATH, '//*[@id="__APP"]/div[2]/div[2]/div/div[1]/div[2]')
sign_in_button.click()
time.sleep(3)

terms_check_box = driver.find_element(By.XPATH, '//*[@id="__APP"]/div[2]/div[3]/div/div[4]/label/div[1]')
terms_check_box.click()

twitter_login = driver.find_element(By.XPATH, '//*[@id="__APP"]/div[2]/div[3]/div/div[3]/div[1]/div[4]/div/div/button')
twitter_login.click()
time.sleep(2)

email_input = driver.find_element(By.XPATH, '//*[@id="username_or_email"]')
email_input.send_keys(EMAIL)

password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
password_input.send_keys(PASSWORD)

remember_me = driver.find_element(By.XPATH, '//*[@id="remember"]')
remember_me.click()

time.sleep(2)
login = driver.find_element(By.XPATH, '//*[@id="allow"]')
login.click()

time.sleep(6)

while True:
    first = driver.find_element(By.XPATH, '//*[@id="__APP"]/div[2]/div[3]/div[3]/div/div[1]/div[1]/div[4]/div[2]').text
    second = driver.find_element(By.XPATH, '//*[@id="__APP"]/div[2]/div[3]/div[3]/div/div[1]/div[2]/div[4]/div[2]').text

    if int(first+second) <= 3:
        while driver.find_element(By.XPATH, '//*[@id="__APP"]/div[2]/div[3]/div[3]/div/div[1]/div[1]/div[4]/div[2]').text+driver.find_element(By.XPATH, '//*[@id="__APP"]/div[2]/div[3]/div[3]/div/div[1]/div[2]/div[4]/div[2]').text <= 3:
            if int(driver.find_element(By.XPATH, '//*[@id="__APP"]/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[4]/div[2]').text+driver.find_element(By.XPATH, '//*[@id="__APP"]/div[2]/div[3]/div[3]/div/div[2]/div[2]/div[4]/div[2]').text) <= CLICK_TIMER:
                driver.find_element(By.XPATH, '//*[@id="__APP"]/div[2]/div[3]/div[5]/div').click()
                has_clicked = True
                current_time = datetime.now()
                driver.quit()

    if has_clicked:
        break

if has_clicked:
    print(f'Clique enregistré le {current_time}')
