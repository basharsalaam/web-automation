# This algorithm involves initiating a bet only after a particular condition has failed to come up in a draw after a certain number of times (trigger).


from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

draw_no = 0
balance = 10000
counter = 0
color_list = [50, 50, 50, 100, 100, 150, 200, 300, 400, 550, 700, 950, 1300, 1750]
profit = [140, 90, 40, 130, 30, 70, 60, 140, 120, 140, 10, 10, 40, 0]
sum_profit = [50, 100, 150, 250, 350, 500, 700, 1000, 1400, 1950, 2650, 3600, 4900, 6650]
prev_numbers = [0]
current_color = ''
trigger = 5

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
# username = 'pulverine'
# password = 'Abdulsalam1'

driver.get('https://logigames.bet9ja.com/Games/Launcher?gameId=11000&provider=0&pff=1&skin=201')

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
        driver.refresh()
        try:
            element = WebDriverWait(driver, 30).until(
                # Find the Statistics Tab
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[1]/div[1]')),
            )
        finally:
            # Click on the Statistics Tab
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[1]/div[1]').click()

        # Click on the total color option
        try:
            element = WebDriverWait(driver, 30).until(
                # Find the total color option
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[4]/div[1]/div[6]/a')),
            )
        finally:
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[4]/div[1]/div[6]/a').click()

        time.sleep(2)
        # Click on last 100 draws option
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[4]/div[1]/div[6]/div/div[1]/div').click()

        time.sleep(2)

        no_color = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[1]/td[4]').text
        green = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[2]/td[4]').text
        red = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[3]/td[4]').text
        blue = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[4]/td[4]').text

        print(no_color, green, red, blue)

        no_color_btn = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]/div/div'
        green_btn = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[1]'
        red_btn = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]'
        blue_btn = '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]'

        if int(no_color) > 1:
            # Click on statistics tab
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[1]/div[1]').click()
            time.sleep(1)
            # Click on the total color option
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[1]/a[5]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]/div/div').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH,
                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a').click()






