import time
import smtplib
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from email.message import EmailMessage

print("""
  ____ _____ _   _          _   _  _____ ______   ____   ____ _______  
 |  _ \_   _| \ | |   /\   | \ | |/ ____|  ____| |  _ \ / __ \__   __| 
 | |_) || | |  \| |  /  \  |  \| | |    | |__    | |_) | |  | | | |    
 |  _ < | | | . ` | / /\ \ | . ` | |    |  __|   |  _ <| |  | | | |    
 | |_) || |_| |\  |/ ____ \| |\  | |____| |____  | |_) | |__| | | |    
 |____/_____|_| \_/_/    \_\_| \_|\_____|______| |____/ \____/  |_|                                                                           
""")

GMAIL = input("GMAIL address: ")
PASSWORD_MAIL = input("GMAIL password: ")
CLICK_TIMER = 7
login_method = ""
service = Service(input("Path to chrome driver: "))


def bot_clicker(has_clicked, current_time):
    print('[+] Script is now running..')
    while True:
        first = driver.find_element(By.XPATH,
                                    '//*[@id="__APP"]/div[2]/div[3]/div[3]/div/div[1]/div[1]/div[4]/div[2]').text
        second = driver.find_element(By.XPATH,
                                     '//*[@id="__APP"]/div[2]/div[3]/div[3]/div/div[1]/div[2]/div[4]/div[2]').text

        while int(first + second) <= 1:
            if int(driver.find_element(By.XPATH,'//*[@id="__APP"]/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[4]/div[2]').text+driver.find_element(By.XPATH, '//*[@id="__APP"]/div[2]/div[3]/div[3]/div/div[2]/div[2]/div[4]/div[2]').text) <= CLICK_TIMER:
                driver.find_element(By.XPATH, '//*[@id="__APP"]/div[2]/div[3]/div[5]/div').click()
                time.sleep(5)
                driver.save_screenshot("screenshot.png")
                has_clicked = True
                current_time = datetime.now()
                print(f'[+] Click trigerred on {current_time}')
                break

        if has_clicked:
            driver.quit()
            message = EmailMessage()
            message['Subject'] = 'Bitcoin Binance Game'
            message.set_content(f'Clique enregistré le {current_time}')

            with open('screenshot.png', 'rb') as fp:
                img_data = fp.read()
            message.add_attachment(img_data, maintype='image', subtype='png')

            try:
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=GMAIL, password=PASSWORD_MAIL)
                    connection.sendmail(from_addr=GMAIL, to_addrs=GMAIL, msg=message.as_string())
            except smtplib.SMTPAuthenticationError:
                print("[+] Email cannot be sent")
            else:
                print("[+] Email successfully sent")
            finally:
                break


driver = webdriver.Chrome(service=service)
driver.get("https://www.binance.com/en/activity/bitcoin-button-game/login")
driver.maximize_window()
time.sleep(3)

authorized_cookies = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
authorized_cookies.click()
time.sleep(1)

while login_method != 'b' and login_method != 't':
    login_method = input("Choose your login method('B' for Binance or 'T' for Twitter): ").lower()

terms_check_box = driver.find_element(By.XPATH, '//*[@id="__APP"]/div[2]/div[3]/div/div[4]/label/div[1]')
terms_check_box.click()

if login_method == 't':
    driver.find_element(By.XPATH, '//*[@id="__APP"]/div[2]/div[3]/div/div[3]/div[1]/div[4]/div/div/button/div[4]').click()
    login_state = input("Press 'y' when logged in: ").lower()
    if login_state == 'y':
        bot_clicker(has_clicked=False, current_time=datetime.now())
    else:
        driver.quit()
        exit()
elif login_method == 'b':
    driver.find_element(By.XPATH, '//*[@id="__APP"]/div[2]/div[3]/div/div[3]/div[2]/div[4]/div/div/button/div[4]').click()
    login_state = input("Press 'y' when logged in: ").lower()
    if login_state == 'y':
        bot_clicker(has_clicked=False, current_time=datetime.now())
    else:
        driver.quit()
        exit()
else:
    driver.quit()
    exit()
