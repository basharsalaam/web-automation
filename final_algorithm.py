from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

draw_no = 0
counter = 0

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
username = 'pulverine'
password = 'Abdulsalam1'


driver.get('https://casino.bet9ja.com/casino/category/popular')
try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[1]/div/div/header/div/div/div[2]/div/div[1]/input[1]')),
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[1]/div/div/header/div/div/div[2]/div/div[1]/input[2]'))
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
        driver.refresh()
        try:
            element = WebDriverWait(driver, 30).until(
                # Find the statistics button
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[1]/a[4]')),
            )
        finally:
            # Click on the rainbow tab
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[1]/a[4]')
            # Click on all the 3+ balls
            red_ball = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[3]/div')
            blue_ball = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[3]/div')
            green_ball = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[3]/div')

            red_ball.click()
            # Hover over the stake input area
            element_to_hover = driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
            hover = ActionChains(driver).move_to_element(element_to_hover)
            hover.perform()
            # Increase the stake to #100
            driver.find_element(By.XPATH,
                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
            # Click submit
            driver.find_element(By.XPATH,
                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a').click()
            time.sleep(2)

            blue_ball.click()
            # Hover over the stake input area
            element_to_hover = driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
            hover = ActionChains(driver).move_to_element(element_to_hover)
            hover.perform()
            # Increase the stake to #100
            driver.find_element(By.XPATH,
                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
            # Click submit
            driver.find_element(By.XPATH,
                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a').click()
            time.sleep(2)

            green_ball.click()
            # Hover over the stake input area
            element_to_hover = driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
            hover = ActionChains(driver).move_to_element(element_to_hover)
            hover.perform()
            # Increase the stake to #100
            driver.find_element(By.XPATH,
                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
            # Click submit
            driver.find_element(By.XPATH,
                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a').click()
