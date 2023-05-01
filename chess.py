from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import chess

# import chess.engine 

def main():

    login_url = "https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/"

    driver = webdriver.Chrome()
    driver.get(login_url)

    input_username = driver.find_element(By.XPATH, '//input[@id="username"]')
    input_username.send_keys("hugginos")

    input_password = driver.find_element(By.XPATH, '//input[@id="password"]')
    input_password.send_keys("Wizzie101")

    login_button = driver.find_element(By.XPATH, '//button[@id="login"]')
    login_button.click()

    time.sleep(100)


    print("Chess Bot Online!")

main()
