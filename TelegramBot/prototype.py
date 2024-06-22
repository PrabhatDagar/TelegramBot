from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from telethon import TelegramClient, errors
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import asyncio
from selenium.webdriver.support.wait import WebDriverWait
import tkinter as tk
from tkinter import simpledialog

def get_input(prompt):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    user_input = simpledialog.askstring(title="Input", prompt=prompt)
    root.destroy()
    return user_input

def setup_driver():
    # Path to your WebDriver
    driver = webdriver.Firefox()
    driver.get('https://web.telegram.org/')
    return driver



def login(driver):
    phone_login=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div/div[2]/button')))
    phone_login.click()
    time.sleep(5)
    
    enter_number=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[1]')
    login_btn= driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[3]/button[1]')
    enter_number.send_keys('Your number here')
    login_btn.click()


def login_code(driver):
    code= get_input("Enter your telegram code here:")
    code_ele= driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[4]/div/div[3]/div/input')
    code_ele.send_keys(code)
    ActionChains(driver).send_keys(Keys.ENTER)




def search_and_open_group(driver, group_name):
    search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[1]/div[2]/input')
    search_box.clear()
    search_box.send_keys(group_name, Keys.ARROW_DOWN, Keys.ENTER)
    
    
    
    # Wait for the group chat to open

'''def send_message(driver, message):
    message_box = driver.find_element(By.XPATH, '//*[@id="editable-message-text"]')
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)'''

def main():
    # Start Telethon client
    
    

    # Setup Selenium driver
    driver = setup_driver()
    time.sleep(15)
    login(driver)
    login_code(driver)
    # Manually log in to Telegram Web with Selenium (you need to do this manually once)
    time.sleep(10)  # Adjust time as needed for manual login
    
    groups = ['Group1', 'Group2']  # Replace with your group names
    

    for group in groups:
        search_and_open_group(driver, group)
        
        time.sleep(2)  # Wait for a bit before moving to the next group

    driver.quit()

if __name__ == "__main__":
   main()