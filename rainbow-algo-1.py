from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

stakes = [50, 100, 250, 650, 1650, 4200]
profits = [32, 15, 12.5, 22.5, 22.5, 30]
stake_index = 0
stake = 50
profit = 32
balance = 15000
initial_balance = 15000
times_lost = 0
draw_no = 0
counter = 0
bet_won = True
session = True
stopped_bet = False
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
username = 'pulverine'
password = 'Abdulsalam1'

bet_numbers = []

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
# driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div['
#                               '2]/div/div[3]/button[2]').click()
# Live game link
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div['
                              '2]/div/div[3]/button[1]').click()
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])

while session is True:
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
                                                '/html/body/div[1]/div/div/div/main/div[1]/div[1]')),
            )
        finally:
            #  Click on Statistics Tab
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[1]/div[1]').click()

            time.sleep(5)
            # Bet results
            bet_results = [driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/span[1]').text,
                           driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/span[2]').text,
                           driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/span[3]').text,
                           driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/span[4]').text,
                           driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/span[5]').text,
                           driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/span[6]').text,
                           ]
            #  Click on Statistics Tab
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[1]/div[1]').click()
        try:
            element = WebDriverWait(driver, 30).until(
                # Find the betzero tab
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[1]/a[6]')),
            )
        finally:
            #  Click on the Betzero tab
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[1]/a[6]').click()
            counter += 1
            time.sleep(2)
            bet_numbers = {
                46: driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[10]'),
                47: driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[11]'),
                48: driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[12]'),
                49: driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[13]')
            }

            # Check if any of the numbers are in the bet results
            if '46' in bet_results or '47' in bet_results or '48' in bet_results or '49' in bet_results:
                print(f'Previous Draw results: {bet_results}\nOne or more of the numbers was in the draw. Stopping bet.')
                times_lost += 1
                if times_lost == 2:
                    # Select the bet numbers
                    for i in bet_numbers:
                        bet_numbers[i].click()
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a').click()
                    balance -= 50
                    print(f'#50 bet made. New balance: {balance}')
                if times_lost == 3:
                    # Select the bet numbers
                    for i in bet_numbers:
                        bet_numbers[i].click()
                    element_to_hover = driver.find_element(By.XPATH,
                                                           '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                    hover = ActionChains(driver).move_to_element(element_to_hover)
                    hover.perform()
                    for i in range(2):
                        driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a').click()
                    balance -= 100
                    print(f'#100 bet made. New balance: {balance}')
                if times_lost == 4:
                    # Select the bet numbers
                    for i in bet_numbers:
                        bet_numbers[i].click()
                    element_to_hover = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                    hover = ActionChains(driver).move_to_element(element_to_hover)
                    hover.perform()
                    for i in range(5):
                        driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a').click()
                    balance -= 250
                    print(f'#250 bet made. New balance: {balance}')
                if times_lost == 5:
                    # Select the bet numbers
                    for i in bet_numbers:
                        bet_numbers[i].click()
                    element_to_hover = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                    hover = ActionChains(driver).move_to_element(element_to_hover)
                    hover.perform()
                    for i in range(13):
                        driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a').click()
                    balance -= 650
                    print(f'#650 bet made. New balance: {balance}')
                if times_lost == 6:
                    # Select the bet numbers
                    for i in bet_numbers:
                        bet_numbers[i].click()
                    # Select the bet numbers
                    element_to_hover = driver.find_element(By.XPATH,
                                                           '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                    hover = ActionChains(driver).move_to_element(element_to_hover)
                    hover.perform()
                    for i in range(13):
                        driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a').click()
                    time.sleep(2)
                    element_to_hover = driver.find_element(By.XPATH,
                                                           '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                    hover = ActionChains(driver).move_to_element(element_to_hover)
                    hover.perform()
                    for i in range(7):
                        driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
                    button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                        (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                    button.click()
                    balance -= 1650
                    print(f'#1650 bet made. New balance: {balance}')
                if times_lost == 7:
                    # Select the bet numbers
                    for i in bet_numbers:
                        bet_numbers[i].click()
                    element_to_hover = driver.find_element(By.XPATH,
                                                           '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                    hover = ActionChains(driver).move_to_element(element_to_hover)
                    hover.perform()
                    for i in range(24):
                        driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a').click()
                    time.sleep(2)
                    button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                        (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                    button.click()
                    element_to_hover = driver.find_element(By.XPATH,
                                                           '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                    hover = ActionChains(driver).move_to_element(element_to_hover)
                    hover.perform()
                    for i in range(20):
                        driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[2]').click()
                    button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                        (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                    button.click()
                    balance -= 4200
                    print(f'#4200 bet made. New balance: {balance}')
                print('---------------------------------------------------------------------------------------')

            elif '46' not in bet_results and '47' not in bet_results and '48' not in bet_results and '49' not in bet_results:
                print(f'Previous Draw results: {bet_results}\nNone of the numbers were in the draw.')
                if times_lost == 2:
                    balance += 32 + 50
                    print(f'#50 bet won. Profit: {balance - initial_balance}, total stake was 50.')
                    times_lost = 0
                if times_lost == 3:
                    balance += 15 + 150
                    print(f'#100 bet won. Profit: {balance - initial_balance}, total stake was 150.')
                    times_lost = 0
                if times_lost == 4:
                    balance += 12.5 + 400
                    print(f'#250 bet won. Profit: {balance - initial_balance}, total stake was 400.')
                    times_lost = 0
                if times_lost == 5:
                    balance += 22.5 + 1050
                    print(f'#650 bet won. Profit: {balance - initial_balance}, total stake was 1050.')
                    times_lost = 0
                if times_lost == 6:
                    balance += 22.5 + 2700
                    print(f'#1650 bet won. Profit: {balance - initial_balance}, total stake was 1700.')
                    times_lost = 0
                if times_lost == 7:
                    balance += 22.5 + 6900
                    print(f'#4200 bet won. Profit: {balance - initial_balance}, total stake was 5900.')
                    times_lost = 0
                times_lost = 0
                print('---------------------------------------------------------------------------------------')

    else:
        pass

