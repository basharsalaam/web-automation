# # This algorithm involves checking the result of the last draw of the rainbow game if each color had at least 2+ balls.
# # The algorithm starts making bets immediately the loss passes the trigger line. Currently, the trigger is 1.
# # That means if the last draw had less than 2+ balls of a particular color, the algorithm makes a bet.

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
first_bet = True

draw_no = 0
red_loss = 0
green_loss = 0
blue_loss = 0
index = 0
trigger = 10
prev_green_losses = 0
prev_blue_losses = 0
prev_red_losses = 0

stake_list = [50, 50, 50, 100, 100, 150, 200, 300, 400, 550, 750, 1000, 1350]
profit_list = [140, 90, 40, 130, 30, 70, 60, 140, 120, 140, 150, 100, 80]
clicks = [0, 0, 0, 2, 2, 3, 4, 6, 8, 11, 14, 19, 26]

balance = 10000

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
username = 'pulverine'
password = 'Abdulsalam1'


driver.get('https://casino.bet9ja.com/casino/category/popular')
try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[1]/div/div/header/div/div/div[2]/div/div[1]/input[1]')),
    )
finally:
    # input username
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/header/div/div/div[2]/div/div[1]/input[1]') \
        .send_keys(username)
    # input password
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/header/div/div/div[2]/div/div[1]/input[2]') \
        .send_keys(password)
    # Submit Credentials
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/header/div/div/div[2]/div/div[1]/button').click()

driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div['
                              '2]/div/div[5]/div').click()

element_to_hover = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div[2]')

hover = ActionChains(driver).move_to_element(element_to_hover)
hover.perform()

# Demo link
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div['
                              '2]/div/div[3]/button[2]').click()
# Live game link
# driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div['
#                               '2]/div/div[3]/button[1]').click()
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])

while True:
    try:
        element = WebDriverWait(driver, 30).until(
            # Find timer
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div[1]/div/div/div/footer/div[2]/div[4]/div/div/div'))
        )
    finally:
        # Get the current time
        curr_time = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/footer/div[2]/div[4]/div/div/div').text

    if curr_time == '40':
        draw_no += 1
        print(f'Draw {draw_no}')
        try:
            element_2 = WebDriverWait(driver, 30).until(
                # Find the Total Color option
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[4]/div[1]/div[6]/a')))

        finally:
            # Click on the Bet Zero option
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[1]/a[6]').click()

        b_1 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[1]'
        b_2 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]'
        b_3 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[3]'
        b_4 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[4]'
        b_5 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[5]'
        b_6 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[6]'
        b_7 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[7]'
        b_8 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[8]'
        b_9 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[9]'
        b_10 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[10]'
        b_11 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[11]'
        b_12 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[12]'
        b_13 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[1]'
        b_14 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[2]'
        b_15 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[3]'
        b_16 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[4]'
        b_17 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[5]'
        b_18 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[6]'
        b_19 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[7]'
        b_20 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[8]'
        b_21 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[9]'
        b_22 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[10]'
        b_23 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[11]'
        b_24 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[12]'
        b_25 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[1]'
        b_26 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[2]'
        b_27 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[3]'
        b_28 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[4]'
        b_29 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[5]'
        b_30 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[6]'
        b_31 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[7]'
        b_32 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[8]'
        b_33 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[9]'
        b_34 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[10]'
        b_35 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[11]'
        b_36 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[12]'
        b_37 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[1]'
        b_38 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[2]'
        b_39 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[3]'
        b_40 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[4]'
        b_41 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[5]'
        b_42 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[6]'
        b_43 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[7]'
        b_44 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[8]'
        b_45 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[9]'
        b_46 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[10]'
        b_47 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[11]'
        b_48 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[12]'
        b_49 = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[13]'

        balls = [b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9, b_10, b_11, b_12, b_13, b_14, b_15, b_16, b_17, b_18,
                 b_19, b_20,
                 b_21, b_22, b_23, b_24, b_25, b_26, b_27, b_28, b_29, b_30, b_31, b_32, b_33, b_34, b_35, b_36, b_37,
                 b_38,
                 b_39, b_40, b_41, b_42, b_43, b_44, b_45, b_46, b_47, b_48]

        first_bet = False
        driver.find_element(By.XPATH, random.choice(balls)).click()
        driver.find_element(By.XPATH, random.choice(balls)).click()

        # Click submit
        time.sleep(2)
        button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
        button.click()
        time.sleep(1)
        button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div')))
        button.click()





