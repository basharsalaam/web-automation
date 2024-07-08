from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
username = 'pulverine'
password = 'Abdulsalam1'
even_percent = ''
odd_percent = ''
initial_balance = 10000
capital = 10000
even_stakes = {'50': 45, '100': 40, '200': 30, '400': 30, '850': 57.5, '1850': 65, '3900': 60}
even_amounts = [50, 150, 350, 750, 1600, 3450, 7350]
odd_stakes = {'50': 45, '100': 40, '200': 30, '450': 50.5, '950': 45.5, '1950': 102.5, '4000': 100}
odd_amounts = [50, 150, 350, 800, 1750, 3700, 7700]
time_list = ['15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32',
             '33', '34'
                   '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51',
             '52', '53', '54'
                         '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65']
bet_time = ['63', '64', '65', '66']
even_percent_list = ['0.00%']
odd_percent_list = ['0.00%']
times_even_lost = 0
times_odd_lost = 0
profit = 0
trigger_line = 2
draw_no = 0
highest_time_even_lost = 8
highest_time_odd_lost = 8

now = datetime.now()
date_str = now.strftime("%Y-%m-%d")
print(date_str)

driver.get(
    'https://bet9ja.espressogames.com/launch/launch.jsp?lang=en&currency=FUN&userb64=RlVO&OTP=guest&types=cd.powerBalls&redirOnExit=https%3A%2F%2Fcasino.bet9ja.com%2Fcasino&callbackOnExit=https%3A%2F%2Fcasino.bet9ja.com%2Fcasino&enableCloseDesktop=0&enableCloseMobile=0')
# try:
#     element = WebDriverWait(driver, 30).until(
#         EC.presence_of_element_located((By.XPATH,
#                                         '/html/body/div[1]/div/div/header/div/div/div[2]/div/div[1]/input[1]')),
#         EC.presence_of_element_located((By.XPATH,
#                                         '/html/body/div[1]/div/div/header/div/div/div[2]/div/div[1]/input[2]'))
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
# try:
#     element = WebDriverWait(driver, 30).until(
#         # Wait for Search bar to load
#         EC.presence_of_element_located((By.XPATH,
#                                         '/html/body/div[1]/div/div/main/div[1]/div[2]/div[1]/div/div[1]/div/input')),
#     )
# finally:
#     # Search for power balls
#     driver.find_element(By.XPATH,
#                         '/html/body/div[1]/div/div/main/div[1]/div[2]/div[1]/div/div[1]/div/input').send_keys('power')
#     time.sleep(2)

try:
    # Find the mute button
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div/div/div[3]/div[3]/div[1]')),
        # Find the statistics button
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div/div/div[1]/div/div/div[1]/div[4]/div/div[3]/div[1]'))
    )
    element_2 = WebDriverWait(driver, 30).until(
        # Find even percentage
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div/div/div[1]/div/div/div[1]/div[4]/div/div[2]/div[3]/div[5]/div[9]')),
        # Find odd percentage
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div/div/div[1]/div/div/div[1]/div[4]/div/div[2]/div[3]/div[5]/div[10]')),
    )
finally:
    if driver.find_element(By.XPATH,
                           '/html/body/div/div/div[1]/div/div/div[1]/div[3]/div[7]/div[3]').text in time_list:
        # Click on the statistics button
        driver.find_element(By.XPATH,
                            '/html/body/div/div/div[1]/div/div/div[1]/div[4]/div/div[3]/div[1]').click()
        time.sleep(1)
        # Get the even percent
        even_percent = driver.find_element(By.XPATH,
                                           '/html/body/div/div/div[1]/div/div/div[1]/div[4]/div/div[2]/div[3]/div[5]/div[9]').text
        # Get the odd percent
        odd_percent = driver.find_element(By.XPATH,
                                          '/html/body/div/div/div[1]/div/div/div[1]/div[4]/div/div[2]/div[3]/div[5]/div[10]').text

    # Click on the mute button
    driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[3]/div[1]').click()

    while True:
        timer = driver.find_element(By.XPATH,
                                    '/html/body/div/div/div[1]/div/div/div[1]/div[3]/div[7]/div[3]').text
        if timer == '0':
            time.sleep(1.5)
        timer = driver.find_element(By.XPATH,
                                    '/html/body/div/div/div[1]/div/div/div[1]/div[3]/div[7]/div[3]').text
        if timer == '0':
            driver.refresh()
            time.sleep(10)

        if driver.find_element(By.XPATH,
                               '/html/body/div/div/div[1]/div/div/div[1]/div[3]/div[7]/div[3]').text in time_list:
            # Click on the statistics button
            driver.find_element(By.XPATH,
                                '/html/body/div/div/div[1]/div/div/div[1]/div[4]/div/div[3]/div[1]').click()
            # Find even percentage
            even_percent = driver.find_element(By.XPATH,
                                               '/html/body/div/div/div[1]/div/div/div[1]/div[4]/div/div[2]/div[3]/div[5]/div[9]').text
            # Find odd percentage
            odd_percent = driver.find_element(By.XPATH,
                                              '/html/body/div/div/div[1]/div/div/div[1]/div[4]/div/div[2]/div[3]/div[5]/div[10]').text
            if even_percent_list[-1] == even_percent:
                pass
            else:
                even_percent_list.append(even_percent)
            if odd_percent_list[-1] == odd_percent:
                pass
            else:
                odd_percent_list.append(odd_percent)
            # Get the timer
            timer = driver.find_element(By.XPATH,
                                        '/html/body/div/div/div[1]/div/div/div[1]/div[3]/div[7]/div[3]').text
            if timer == '65' or timer == '64' or timer == '66' :
                prev_even_value = even_percent_list[-2]
                prev_odd_value = odd_percent_list[-2]
                print(f'previous percentages: even: {prev_even_value}, odd: {prev_odd_value}')
                print(f'current percentages: even: {even_percent}, odd: {odd_percent}')
                time.sleep(2)

                draw_no += 1
                print(f'Draw no: {draw_no}')
                prev_even_value = list(prev_even_value)
                if '%' in prev_even_value:
                    prev_even_value.remove('%')
                else:
                    pass
                prev_even_percent = ''
                for i in prev_even_value:
                    prev_even_percent += i
                prev_even_percent = float(prev_even_percent)
                print(f'Previous even value: {prev_even_percent}')

                even_percent = list(even_percent)
                even_percent.remove('%')
                even_value = ''
                for i in even_percent:
                    even_value += i
                even_value = float(even_value)
                print(f'Current even value: {even_value}\n')

                odd_percent = list(odd_percent)
                odd_percent.remove('%')
                odd_value = ''
                for i in odd_percent:
                    odd_value += i
                odd_value = float(odd_value)
                print(f'Current odd value: {odd_value}')

                prev_odd_value = list(prev_odd_value)
                if '%' in prev_odd_value:
                    prev_odd_value.remove('%')
                else:
                    pass
                prev_odd_percent = ''
                for i in prev_odd_value:
                    prev_odd_percent += i
                prev_odd_percent = float(prev_odd_percent)
                print(f'Previous odd value: {prev_odd_percent}\n')
                if even_value > odd_value:  # That means even won
                    if times_even_lost > highest_time_even_lost:
                        highest_time_even_lost = times_even_lost
                    if times_even_lost >= trigger_line and times_odd_lost == 0:
                        stake = int(list(even_stakes.keys())[times_even_lost - trigger_line])
                        profit = int(list(even_stakes.values())[times_even_lost - trigger_line])
                        initial_balance = initial_balance + profit
                        print(
                            f'#{stake} Bet on even won. New Balance is {initial_balance}. Total profit is {initial_balance - capital}')
                    times_odd_lost += 1
                    times_even_lost = 0
                    print(f'Odd has lost {times_odd_lost} times.')
                    if times_odd_lost >= trigger_line:  # Check if the trigger line has been passed
                        # Select the even or odd tab
                        driver.find_element(By.XPATH,
                                            '/html/body/div/div/div[1]/div/div/div[1]/div[5]/div/div[2]/div[5]').click()
                        # Select the sum odd option
                        driver.find_element(By.XPATH,
                                            '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                        # Get the stake value inputted
                        stake = driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[2]').text

                        if times_odd_lost == 2:  # Bet 1: 50 (50)
                            # Click on confirm and place bet (50)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()

                        elif times_odd_lost == 3:  # Bet 2: 100 (100)
                            # Increase the stake
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (100)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                        elif times_odd_lost == 4:  # Bet 3: 200 (200)
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (200)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                        elif times_odd_lost == 5:  # Bet 4: 450 (200 + 200 + 50 = 450)
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (200)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (200 + 200 = 400)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            # Click on confirm and place bet (200 + 200 + 50 = 450)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()

                        elif times_odd_lost == 6:  # Bet 5: 950 (500 + 200 + 200 + 50 = 950)
                            for i in range(5):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (500)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (500 + 200 = 700)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (500 + 200 + 200 = 900)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            # Click on confirm and place bet (500 + 200 + 200 + 50 = 950)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                        elif times_odd_lost == 7:  # Bet 6: 1950 (1000 + 500 + 200 + 200 + 50 = 1950)
                            for i in range(7):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (1000)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(5):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (1000 + 500 = 1500)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (1000 + 500 + 200 = 1700)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (1000 + 500 + 200 + 200 = 1900)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            # Click on confirm and place bet (1000 + 500 + 200 + 200 + 50 = 1950)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                        elif times_odd_lost == 8:  # Bet 7: 4000 (4000)
                            for i in range(9):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (2500)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(7):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (2500 + 1000 = 3500)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(5):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (2500 + 1000 = 3500)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()

                        print(
                            f'#{int(list(odd_stakes.keys())[times_odd_lost - trigger_line])} Bet placed on odd. New Balance:{initial_balance - odd_amounts[times_odd_lost - trigger_line]}')
                elif even_value < odd_value:  # Odd won
                    if times_odd_lost > highest_time_odd_lost:
                        highest_time_odd_lost = times_odd_lost
                    if times_odd_lost >= trigger_line and times_even_lost == 0:
                        stake = int(list(odd_stakes.keys())[times_odd_lost - trigger_line])
                        profit = int(list(odd_stakes.values())[times_odd_lost - trigger_line])
                        initial_balance = initial_balance + profit
                        print(
                            f'#{stake} Bet on odd won. New Balance is {initial_balance}. Total profit is {initial_balance - capital}')
                    times_odd_lost = 0
                    times_even_lost += 1
                    print(f'Even has lost {times_even_lost} times.')
                    if times_even_lost >= trigger_line:  # Check if the trigger line has been passed
                        # Select the even or odd tab
                        driver.find_element(By.XPATH,
                                            '/html/body/div/div/div[1]/div/div/div[1]/div[5]/div/div[2]/div[5]').click()
                        # Select the sum odd option
                        driver.find_element(By.XPATH,
                                            '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                        # Get the stake value inputted
                        stake = driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[2]').text
                        if times_even_lost == 2:  # Bet 1: 50 (50)
                            # Click on confirm and place bet (50)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()

                        elif times_even_lost == 3:  # Bet 2: 100 (100)
                            # Increase the stake
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (100)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                        elif times_even_lost == 4:  # Bet 3: 200 (200)
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (200)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                        elif times_even_lost == 5:  # Bet 4: 400 (200 + 200 = 400)
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (200)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (200 + 200 = 400)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()

                        elif times_even_lost == 6:  # Bet 5: 950 (500 + 200 + 100 + 50 = 850)
                            for i in range(5):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (500)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (500 + 200 = 700)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(1):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (500 + 200 + 100 = 900)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            # Click on confirm and place bet (500 + 200 + 100 + 50 = 850)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                        elif times_odd_lost == 7:  # Bet 6: 1850 (1000 + 500 + 200 + 100 + 50 = 1950)
                            for i in range(7):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (1000)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(5):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (1000 + 500 = 1500)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (1000 + 500 + 200 = 1700)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(1):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (1000 + 500 + 200 + 100 = 1800)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            # Click on confirm and place bet (1000 + 500 + 200 + 100 + 50 = 1850)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                        elif times_even_lost == 8:  # Bet 7: 3900 (2500 + 1000 + 200 + 200)
                            for i in range(9):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (2500)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(7):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (2500 + 1000 = 3500)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (2500 + 1000 = 3500)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (2500 + 1000 = 3500)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()

                        print(
                            f'#{int(list(even_stakes.keys())[times_even_lost - trigger_line])} Bet placed on even. New Balance:{initial_balance - even_amounts[times_even_lost - trigger_line]}')
                elif even_value - prev_even_percent > 0:  # even won
                    if times_even_lost > highest_time_even_lost:
                        highest_time_even_lost = times_even_lost
                    if times_even_lost >= trigger_line and times_odd_lost == 0:
                        stake = int(list(even_stakes.keys())[times_even_lost - trigger_line])
                        profit = int(list(even_stakes.values())[times_even_lost - trigger_line])
                        initial_balance = initial_balance + profit
                        print(
                            f'#{stake} Bet on even won. New Balance is {initial_balance}. Total profit is {initial_balance - capital}')
                    times_odd_lost += 1
                    times_even_lost = 0
                    print(f'Odd has lost {times_odd_lost} times.')
                    if times_odd_lost >= trigger_line:  # Check if the trigger line has been passed
                        # Select the even or odd tab
                        driver.find_element(By.XPATH,
                                            '/html/body/div/div/div[1]/div/div/div[1]/div[5]/div/div[2]/div[5]').click()
                        # Select the sum odd option
                        driver.find_element(By.XPATH,
                                            '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                        # Get the stake value inputted
                        stake = driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[2]').text

                        if times_odd_lost == 2:  # Bet 1: 50 (50)
                            # Click on confirm and place bet (50)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()

                        elif times_odd_lost == 3:  # Bet 2: 100 (100)
                            # Increase the stake
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (100)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                        elif times_odd_lost == 4:  # Bet 3: 200 (200)
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (200)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                        elif times_odd_lost == 5:  # Bet 4: 450 (200 + 200 + 50 = 450)
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (200)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (200 + 200 = 400)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            # Click on confirm and place bet (200 + 200 + 50 = 450)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()

                        elif times_odd_lost == 6:  # Bet 5: 950 (500 + 200 + 200 + 50 = 950)
                            for i in range(5):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (500)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (500 + 200 = 700)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (500 + 200 + 200 = 900)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            # Click on confirm and place bet (500 + 200 + 200 + 50 = 950)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                        elif times_odd_lost == 7:  # Bet 6: 1950 (1000 + 500 + 200 + 200 + 50 = 1950)
                            for i in range(7):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (1000)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(5):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (1000 + 500 = 1500)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (1000 + 500 + 200 = 1700)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (1000 + 500 + 200 + 200 = 1900)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            # Click on confirm and place bet (1000 + 500 + 200 + 200 + 50 = 1950)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                        elif times_odd_lost == 8:  # Bet 7: 4000 (4000)
                            for i in range(9):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (2500)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(7):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (2500 + 1000 = 3500)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(5):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (2500 + 1000 + 500 = 4000)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()

                        print(
                            f'#{int(list(odd_stakes.keys())[times_odd_lost - trigger_line])} Bet placed on odd. New Balance:{initial_balance - odd_amounts[times_odd_lost - trigger_line]}')
                elif even_value - prev_even_percent < 0:  # odd won
                    if times_odd_lost > highest_time_odd_lost:
                        highest_time_odd_lost = times_odd_lost
                    if times_odd_lost >= trigger_line and times_even_lost == 0:
                        stake = int(list(odd_stakes.keys())[times_odd_lost - trigger_line])
                        profit = int(list(odd_stakes.values())[times_odd_lost - trigger_line])
                        initial_balance = initial_balance + profit
                        print(
                            f'#{stake} Bet on odd won. New Balance is {initial_balance}. Total profit is {initial_balance - capital}')
                    times_odd_lost = 0
                    times_even_lost += 1
                    print(f'Even has lost {times_even_lost} times.')
                    if times_even_lost >= trigger_line:  # Check if the trigger line has been passed
                        # Select the even or odd tab
                        driver.find_element(By.XPATH,
                                            '/html/body/div/div/div[1]/div/div/div[1]/div[5]/div/div[2]/div[5]').click()
                        # Select the sum odd option
                        driver.find_element(By.XPATH,
                                            '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                        # Get the stake value inputted
                        stake = driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[2]').text
                        if times_even_lost == 2:  # Bet 1: 50 (50)
                            # Click on confirm and place bet (50)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()

                        elif times_even_lost == 3:  # Bet 2: 100 (100)
                            # Increase the stake
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (100)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                        elif times_even_lost == 4:  # Bet 3: 200 (200)
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (200)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                        elif times_even_lost == 5:  # Bet 4: 400 (200 + 200 = 400)
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (200)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (200 + 200 = 400)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()

                        elif times_even_lost == 6:  # Bet 5: 950 (500 + 200 + 100 + 50 = 850)
                            for i in range(5):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (500)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (500 + 200 = 700)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(1):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (500 + 200 + 100 = 900)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            # Click on confirm and place bet (500 + 200 + 100 + 50 = 850)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                        elif times_odd_lost == 7:  # Bet 6: 1850 (1000 + 500 + 200 + 100 + 50 = 1950)
                            for i in range(7):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (1000)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(5):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (1000 + 500 = 1500)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (1000 + 500 + 200 = 1700)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(1):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (1000 + 500 + 200 + 100 = 1800)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            # Click on confirm and place bet (1000 + 500 + 200 + 100 + 50 = 1850)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                        elif times_even_lost == 8:  # Bet 7: 3900 (2500 + 1000 + 200 + 200)
                            for i in range(9):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (2500)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(7):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (2500 + 1000 = 3500)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (2500 + 1000 + 200 = 3700)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                            # Select the sum odd option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                            for i in range(3):
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                            # Click on confirm and place bet (2500 + 1000 + 200 + 200 = 3900)
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()

                        print(
                            f'#{int(list(even_stakes.keys())[times_even_lost - trigger_line])} Bet placed on even. New Balance:{initial_balance - even_amounts[times_even_lost - trigger_line]}')
            else:
                pass
        else:
            pass
