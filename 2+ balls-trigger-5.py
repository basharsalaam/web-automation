# This algorithm involves checking the result of the last draw of the rainbow game if each color had at least 2+ balls.
# The algorithm starts making bets immediately the loss passes the trigger line. Currently, the trigger is 1.
# That means if the last draw had less than 2+ balls of a particular color, the algorithm makes a bet.


from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

draw_no = 0
red_loss = 0
green_loss = 0
blue_loss = 0

balance = 10000

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
username = 'pulverine'
password = 'Abdulsalam1'

driver.get('https://logigames.bet9ja.com/Games/Launcher?gameId=11000&provider=0&pff=1&skin=201')
# try:
#     element = WebDriverWait(driver, 30).until(
#         EC.presence_of_element_located((By.XPATH,
#                                         '/html/body/div[1]/div/div/header/div/div/div[2]/div/div[1]/input[1]')),
#     )
# finally:
#     # input username
#     driver.find_element(By.XPATH, '/html/body/div[1]/div/div/header/div/div/div[2]/div/div[1]/input[1]') \
#         .send_keys(username)
#     # input password
#     driver.find_element(By.XPATH, '/html/body/div[1]/div/div/header/div/div/div[2]/div/div[1]/input[2]') \
#         .send_keys(password)
#     # Submit Credentials
#     driver.find_element(By.XPATH, '/html/body/div[1]/div/div/header/div/div/div[2]/div/div[1]/button').click()
#
# driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div['
#                               '2]/div/div[5]/div').click()
# element_to_hover = driver.find_element(By.XPATH,
#                                        '/html/body/div[1]/div/div/main/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div[2]')
# hover = ActionChains(driver).move_to_element(element_to_hover)
# hover.perform()
# # Demo link
# driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div['
#                               '2]/div/div[3]/button[2]').click()
# # Live game link
# # driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div['
# #                               '2]/div/div[3]/button[1]').click()
# time.sleep(1)
# driver.switch_to.window(driver.window_handles[1])

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

        time.sleep(5)

        red_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[1]/td[5]/div/div[1]')))
        green_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[1]/td[5]/div/div[2]')))
        blue_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[1]/td[5]/div/div[3]')))

        red_amount = driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[1]/td[5]/div/div[1]').text
        green_amount = driver.find_element(By.XPATH,
                                           '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[1]/td[5]/div/div[2]').text
        blue_amount = driver.find_element(By.XPATH,
                                          '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[1]/td[5]/div/div[3]').text

        # Click on the Statistics Tab
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[1]/div[1]').click()

        # Click on the Rainbow Tab
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[1]/a[4]').click()

        if int(blue_amount) < 2:
            blue_loss += 1
            time.sleep(2)
            if blue_loss == 5:  # Stake is #50
                # Click on the 2+ blue balls option
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/div').click()

                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()
                balance -= 50
                print(f'#50 bet made on 2+ blue balls.Balance: {balance}')
            elif blue_loss == 6:  # Stake is #150

                # Click on the 2+ blue balls option
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/div').click()

                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()
                # Increase the stake to #150
                for i in range(3):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()
                balance -= 150
                print(f'#150 bet made on 2+ blue balls.Balance: {balance}')
            elif blue_loss == 7:  # Stake is #450

                # Click on the 2+ blue balls option
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/div').click()
                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                # Increase the stake to #450
                for i in range(9):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()
                balance -= 450
                print(f'#450 bet made on 2+ blue balls.Balance: {balance}')
            elif blue_loss == 8:  # Stake is #1350

                # Click on the 2+ blue balls option
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/div').click()
                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                # Increase the stake to #1000
                for i in range(20):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()

                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                # Decrease the stake to #1000
                for i in range(13):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[2]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()
                balance -= 1350
                print(f'#1350 bet made on 2+ blue balls.Balance: {balance}')
            elif blue_loss == 9:  # Stake is #4050

                # Click on the 2+ blue balls option
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/div').click()
                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                # Increase the stake to #4000
                for i in range(32):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()

                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                # Decrease the stake to #50
                for i in range(32):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[2]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()
                balance -= 4050
                print(f'#4050 bet made on 2+ blue balls.Balance: {balance}')
            elif blue_loss == 10:  # Stake is #4050

                # Click on the 2+ blue balls option
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/div').click()
                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                # Increase the stake to #12000
                for i in range(50):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()

                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                # Decrease the stake to #12000
                for i in range(47):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[2]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()
                balance -= 12150
                print(f'#12150 bet made on 2+ blue balls.Balance: {balance}')
            elif blue_loss > 10:
                print(f'Blue lost more than 10 times ({blue_loss} times)')
        else:
            if blue_loss == 5:
                balance += 25 + 50
                print(f'#50 Bet won. Balance: {balance}')
            if blue_loss == 6:
                balance += 25 + 200
                print(f'#150 Bet won. Balance: {balance}')
            if blue_loss == 7:
                balance += 25 + 650
                print(f'#450 Bet won. Balance: {balance}')
            if blue_loss == 8:
                balance += 25 + 2000
                print(f'#1350 Bet won. Balance: {balance}')
            if blue_loss == 9:
                balance += 25 + 6050
                print(f'#4050 Bet won. Balance: {balance}')
            if blue_loss == 10:
                balance += 25 + 18200
                print(f'#12150 Bet won. Balance: {balance}')
            blue_loss = 0

        if int(red_amount) < 2:
            red_loss += 1
            time.sleep(2)
            if red_loss == 5:  # Stake is #50
                # Click on the 2+ red balls option
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div/div').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()
                balance -= 50
                print(f'#50 bet made on 2+ red balls.Balance: {balance}')
            elif red_loss == 6:  # Stake is #150
                # Click on the 2+ red balls option
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div').click()

                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()
                # Increase the stake to #150
                for i in range(3):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()
                balance -= 150
                print(f'#150 bet made on 2+ red balls.Balance: {balance}')
            elif red_loss == 7:  # Stake is #450

                # Click on the 2+ red balls option
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div').click()
                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                # Increase the stake to #450
                for i in range(9):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()
                balance -= 450
                print(f'#450 bet made on 2+ red balls.Balance: {balance}')
            elif red_loss == 8:  # Stake is #1350
                # Click on the 2+ red balls option
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div').click()
                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                # Increase the stake to #1000
                for i in range(20):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()

                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                # Decrease the stake to #1000
                for i in range(13):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[2]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()
                balance -= 1350
                print(f'#1350 bet made on 2+ red balls.Balance: {balance}')
            elif red_loss == 9:  # Stake is #4050

                # Click on the 2+ red balls option
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div').click()
                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                # Increase the stake to #4000
                for i in range(32):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()

                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                # Decrease the stake to #4000
                for i in range(32):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[2]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()
                balance -= 4050
                print(f'#4050 bet made on 2+ red balls.Balance: {balance}')
            elif red_loss == 10:  # Stake is #4050

                # Click on the 2+ red balls option
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div').click()
                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                # Increase the stake to #12000
                for i in range(50):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()

                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                # Decrease the stake to #12000
                for i in range(47):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[2]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()
                balance -= 12150
                print(f'#12150 bet made on 2+ red balls.Balance: {balance}')
            elif red_loss > 10:
                print(f'Red lost more than 10 times ({red_loss} times)')
        else:
            if red_loss == 5:
                balance += 25 + 50
                print(f'#50 Bet won. Balance: {balance}')
            if red_loss == 6:
                balance += 25 + 200
                print(f'#150 Bet won. Balance: {balance}')
            if red_loss == 7:
                balance += 25 + 650
                print(f'#450 Bet won. Balance: {balance}')
            if red_loss == 8:
                balance += 25 + 2000
                print(f'#1350 Bet won. Balance: {balance}')
            if red_loss == 9:
                balance += 25 + 6050
                print(f'#4050 Bet won. Balance: {balance}')
            if red_loss == 10:
                balance += 25 + 18200
                print(f'#12150 Bet won. Balance: {balance}')
            red_loss = 0

        if int(green_amount) < 2:
            green_loss += 1
            time.sleep(2)
            if green_loss == 5:  # Stake is #50

                # Click on the 2+ green balls option
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[2]/div/div').click()

                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()
                balance -= 50
                print(f'#50 bet made on 2+ green balls.Balance: {balance}')
            elif green_loss == 6:  # Stake is #150

                # Click on the 2+ green balls option
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[2]/div/div').click()

                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()
                # Increase the stake to #150
                for i in range(3):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()
                balance -= 150
                print(f'#150 bet made on 2+ green balls.Balance: {balance}')
            elif green_loss == 7:  # Stake is #450

                # Click on the 2+ green balls option
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[2]/div/div').click()
                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                # Increase the stake to #450
                for i in range(9):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()
                balance -= 450
                print(f'#450 bet made on 2+ green balls.Balance: {balance}')
            elif green_loss == 8:  # Stake is #1350

                # Click on the 2+ green balls option
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[2]/div/div').click()
                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                # Increase the stake to #1000
                for i in range(20):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()

                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()
                # Decrease the stake to #350
                for i in range(7):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[2]').click()

                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()
                balance -= 1350
                print(f'#1350 bet made on 2+ green balls.Balance: {balance}')
            elif green_loss == 9:  # Stake is #4050

                # Click on the 2+ green balls option
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[2]/div/div').click()
                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                # Increase the stake to #50
                for i in range(32):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()

                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[2]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                # Decrease the stake to #4000
                for i in range(32):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[2]').click()

                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()
                balance -= 4050
                print(f'#4050 bet made on 2+ green balls.Balance: {balance}')
            elif green_loss == 10:  # Stake is #4050

                # Click on the 2+ green balls option
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[2]/div/div').click()
                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                # Increase the stake to #1000
                for i in range(50):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[1]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()

                element_to_hover = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/input')
                hover = ActionChains(driver).move_to_element(element_to_hover)
                hover.perform()

                # Decrease the stake to #1000
                for i in range(47):
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[2]').click()
                # Click submit
                button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]/div[3]/a')))
                button.click()
                balance -= 12150
                print(f'#12150 bet made on 2+ green balls.Balance: {balance}')
            elif green_loss > 10:
                print(f'Green lost more than 10 times ({green_loss} times)')

        else:
            if green_loss == 5:
                balance += 25 + 50
                print(f'#50 Bet won. Balance: {balance}')
            if green_loss == 6:
                balance += 25 + 200
                print(f'#150 Bet won. Balance: {balance}')
            if green_loss == 7:
                balance += 25 + 650
                print(f'#450 Bet won. Balance: {balance}')
            if green_loss == 8:
                balance += 25 + 2000
                print(f'#1350 Bet won. Balance: {balance}')
            if green_loss == 9:
                balance += 25 + 6050
                print(f'#4050 Bet won. Balance: {balance}')
            if green_loss == 10:
                balance += 25 + 18200
                print(f'#12150 Bet won. Balance: {balance}')
            green_loss = 0
        print('----------------------------------------------------------------------------')
