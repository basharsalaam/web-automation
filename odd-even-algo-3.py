from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import sys

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
bet_time_1 = ['63', '64', '65', '66']
bet_time_2 = ['40', '39', '38', '37']
even_percent_list = ['0.00%']
odd_percent_list = ['0.00%']

times_even_lost = 0
times_odd_lost = 0

profit = 0
trigger_line = 1
draw_no = 0
counter = 0

with open('loss-log.txt') as f:
    data = f.readlines()
highest_time_lost = ''
for item in data[0]:
    highest_time_lost += item

draws_odd_lost_1_times = [0]
draws_odd_lost_2_times = [0]
draws_odd_lost_3_times = [0]
draws_odd_lost_4_times = [0]
draws_odd_lost_5_times = [0]
draws_odd_lost_6_times = [0]
draws_odd_lost_7_times = [0]
draws_odd_lost_8_times = [0]
draws_odd_lost_9_times = [0]
draws_odd_lost_10_times = [0]
draws_odd_lost_11_times = [0]
draws_odd_lost_12_times = [0]
draws_odd_lost_13_times = [0]
draws_odd_lost_14_times = [0]
draws_odd_lost_15_times = [0]

draws_even_lost_1_times = [0]
draws_even_lost_2_times = [0]
draws_even_lost_3_times = [0]
draws_even_lost_4_times = [0]
draws_even_lost_5_times = [0]
draws_even_lost_6_times = [0]
draws_even_lost_7_times = [0]
draws_even_lost_8_times = [0]
draws_even_lost_9_times = [0]
draws_even_lost_10_times = [0]
draws_even_lost_11_times = [0]
draws_even_lost_12_times = [0]
draws_even_lost_13_times = [0]
draws_even_lost_14_times = [0]
draws_even_lost_15_times = [0]

times_odd_lost_1_time = 0
times_odd_lost_2_time = 0
times_odd_lost_3_time = 0
times_odd_lost_4_time = 0
times_odd_lost_5_time = 0
times_odd_lost_6_time = 0
times_odd_lost_7_time = 0
times_odd_lost_8_time = 0
times_odd_lost_9_time = 0
times_odd_lost_10_time = 0
times_odd_lost_11_time = 0
times_odd_lost_12_time = 0
times_odd_lost_13_time = 0
times_odd_lost_14_time = 0
times_odd_lost_15_time = 0

times_even_lost_1_time = 0
times_even_lost_2_time = 0
times_even_lost_3_time = 0
times_even_lost_4_time = 0
times_even_lost_5_time = 0
times_even_lost_6_time = 0
times_even_lost_7_time = 0
times_even_lost_8_time = 0
times_even_lost_9_time = 0
times_even_lost_10_time = 0
times_even_lost_11_time = 0
times_even_lost_12_time = 0
times_even_lost_13_time = 0
times_even_lost_14_time = 0
times_even_lost_15_time = 0

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
            time.sleep(3)
        timer = driver.find_element(By.XPATH,
                                    '/html/body/div/div/div[1]/div/div/div[1]/div[3]/div[7]/div[3]').text
        if timer == '0':
            driver.refresh()
            try:
                timer = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[3]/div[7]/div[3]'))
                )
            finally:
                pass

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

            if timer == '40':
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
                if counter == 0:
                    counter += 1
                    pass
                else:
                    if even_value > prev_even_percent:  # Even won
                        if times_even_lost > int(highest_time_lost):
                            highest_time_lost = times_even_lost
                            # Open the loss log file in read only
                            with open('loss-log.txt', 'r') as file:
                                data = file.read()  # Read the contents of the file
                                data = data.replace(f'{highest_time_lost}', f'{times_even_lost}')  # Replace the previous highest time with the new highest
                        if 1 <= times_odd_lost > 6:
                            stake = 0
                            profit = 0
                            print(f'Odd has lost more than 6 times. {times_odd_lost} times exactly.')
                        elif times_even_lost >= trigger_line and times_odd_lost == 0:
                            stake = int(list(even_stakes.keys())[times_even_lost - trigger_line])
                            profit = int(list(even_stakes.values())[times_even_lost - trigger_line])
                            initial_balance = initial_balance + profit
                            print(f'#{stake} Bet on even won. New Balance is {initial_balance}. Total profit is {initial_balance - capital}')
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
                            if times_odd_lost == 0:
                                pass
                            elif times_odd_lost == 1:  # Bet 1: 50 (50)
                                # Click on confirm and place bet (50)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_odd_lost_1_times.append(draw_no)
                                prev_time_odd_lost_1 = ((draws_odd_lost_1_times[-1] - draws_odd_lost_1_times[-2]) * 75) / 60
                                times_odd_lost_1_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_1} mins since the last time Odd lost 1 times\n'
                                    f'Overall Odd has lost 1 times {times_odd_lost_1_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(odd_stakes.keys())[times_odd_lost - trigger_line])} Bet placed on odd. New Balance:{initial_balance - odd_amounts[times_odd_lost - trigger_line]}')
                            elif times_odd_lost == 2:  # Bet 2: 100 (100)
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (100)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_odd_lost_2_times.append(draw_no)
                                prev_time_odd_lost_2 = ((draws_odd_lost_2_times[-1] - draws_odd_lost_2_times[-2]) * 75) / 60
                                times_odd_lost_2_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_2} mins since the last time Odd lost 2 times\n'
                                    f'Overall Odd has lost 2 times {times_odd_lost_2_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(odd_stakes.keys())[times_odd_lost - trigger_line])} Bet placed on odd. New Balance:{initial_balance - odd_amounts[times_odd_lost - trigger_line]}')
                            elif times_odd_lost == 3:  # Bet 3: 200 (200)
                                for i in range(3):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (200)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_odd_lost_3_times.append(draw_no)
                                prev_time_odd_lost_3 = ((draws_odd_lost_3_times[-1] - draws_odd_lost_3_times[-2]) * 75) / 60
                                times_odd_lost_3_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_3} mins since the last time Odd lost 3 times\n'
                                    f'Overall Odd has lost 3 times {times_odd_lost_3_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(odd_stakes.keys())[times_odd_lost - trigger_line])} Bet placed on odd. New Balance:{initial_balance - odd_amounts[times_odd_lost - trigger_line]}')
                            elif times_odd_lost == 4:  # Bet 4: 450 (200 + 200 + 50 = 450)
                                for i in range(3):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (200)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                time.sleep(1)
                                # Select the sum odd option
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                                time.sleep(0.5)
                                for i in range(3):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (200 + 200)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                time.sleep(1)
                                # Select the sum odd option
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                                # Click on confirm and place bet (200 + 200 + 50)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_odd_lost_4_times.append(draw_no)
                                prev_time_odd_lost_4 = ((draws_odd_lost_4_times[-1] - draws_odd_lost_4_times[-2]) * 75) / 60
                                times_odd_lost_4_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_4} mins since the last time Odd lost 4 times\n'
                                    f'Overall Odd has lost 4 times {times_odd_lost_4_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(odd_stakes.keys())[times_odd_lost - trigger_line])} Bet placed on odd. New Balance:{initial_balance - odd_amounts[times_odd_lost - trigger_line]}')
                            elif times_odd_lost == 5:  # Bet 5: 950 (500 + 200 + 200 + 50 = 950)
                                for i in range(5):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (500)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                time.sleep(1)
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
                                # Click on confirm and place bet (500 + 200 + 200 = 900)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_odd_lost_5_times.append(draw_no)
                                prev_time_odd_lost_5 = ((draws_odd_lost_5_times[-1] - draws_odd_lost_5_times[-2]) * 75) / 60
                                times_odd_lost_5_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_5} mins since the last time Odd lost 5 times\n'
                                    f'Overall Odd has lost 5 times {times_odd_lost_5_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(odd_stakes.keys())[times_odd_lost - trigger_line])} Bet placed on odd. New Balance:{initial_balance - odd_amounts[times_odd_lost - trigger_line]}')
                            elif times_odd_lost == 6:
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
                                draws_odd_lost_6_times.append(draw_no)
                                prev_time_odd_lost_6 = ((draws_odd_lost_6_times[-1] - draws_odd_lost_6_times[-2]) * 75) / 60
                                times_odd_lost_6_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_6} mins since the last time Odd lost 6 times\n'
                                    f'Overall Odd has lost 6 times {times_odd_lost_6_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(odd_stakes.keys())[times_odd_lost - trigger_line])} Bet placed on odd. New Balance:{initial_balance - odd_amounts[times_odd_lost - trigger_line]}')
                            elif times_odd_lost == 7:
                                draws_odd_lost_7_times.append(draw_no)
                                prev_time_odd_lost_7 = ((draws_odd_lost_7_times[-1] - draws_odd_lost_7_times[-2]) * 75) / 60
                                times_odd_lost_7_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_7} mins since the last time Odd lost 7 times\n'
                                    f'Overall Odd has lost 7 times {times_odd_lost_7_time} in the last {time_spent} mins')
                            elif times_odd_lost == 8:
                                draws_odd_lost_8_times.append(draw_no)
                                prev_time_odd_lost_8 = ((draws_odd_lost_8_times[-1] - draws_odd_lost_8_times[-2]) * 75) / 60
                                times_odd_lost_8_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_8} mins since the last time Odd lost 8 times\n'
                                    f'Overall Odd has lost 8 times {times_odd_lost_8_time} in the last {time_spent} mins')
                            elif times_odd_lost == 9:
                                draws_odd_lost_9_times.append(draw_no)
                                prev_time_odd_lost_9 = ((draws_odd_lost_9_times[-1] - draws_odd_lost_9_times[-2]) * 75) / 60
                                times_odd_lost_9_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_9} mins since the last time Odd lost 9 times\n'
                                    f'Overall Odd has lost 9 times {times_odd_lost_9_time} in the last {time_spent} mins')
                            elif times_odd_lost == 10:
                                draws_odd_lost_10_times.append(draw_no)
                                prev_time_odd_lost_10 = ((draws_odd_lost_10_times[-1] - draws_odd_lost_10_times[-2]) * 75) / 60
                                times_odd_lost_10_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_10} mins since the last time Odd lost 10 times\n'
                                    f'Overall Odd has lost 10 times {times_odd_lost_10_time} in the last {time_spent} mins')
                            elif times_odd_lost == 11:
                                draws_odd_lost_11_times.append(draw_no)
                                prev_time_odd_lost_11 = ((draws_odd_lost_11_times[-1] - draws_odd_lost_11_times[-2]) * 75) / 60
                                times_odd_lost_11_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_11} mins since the last time Odd lost 11 times\n'
                                    f'Overall Odd has lost 11 times {times_odd_lost_11_time} in the last {time_spent} mins')
                            elif times_odd_lost == 12:
                                draws_odd_lost_12_times.append(draw_no)
                                prev_time_odd_lost_12 = ((draws_odd_lost_12_times[-1] - draws_odd_lost_12_times[-2]) * 75) / 60
                                times_odd_lost_12_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_12} mins since the last time Odd lost 12 times\n'
                                    f'Overall Odd has lost 12 times {times_odd_lost_12_time} in the last {time_spent} mins')
                            elif times_odd_lost == 13:
                                draws_odd_lost_13_times.append(draw_no)
                                prev_time_odd_lost_13 = ((draws_odd_lost_13_times[-1] - draws_odd_lost_13_times[-2]) * 75) / 60
                                times_odd_lost_13_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_13} mins since the last time Odd lost 13 times\n'
                                    f'Overall Odd has lost 13 times {times_odd_lost_13_time} in the last {time_spent} mins')
                            elif times_odd_lost == 14:
                                draws_odd_lost_14_times.append(draw_no)
                                prev_time_odd_lost_14 = ((draws_odd_lost_14_times[-1] - draws_odd_lost_14_times[-2]) * 75) / 60
                                times_odd_lost_14_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_14} mins since the last time Odd lost 14 times\n'
                                    f'Overall Odd has lost 14 times {times_odd_lost_14_time} in the last {time_spent} mins')
                            elif times_odd_lost == 15:
                                draws_odd_lost_15_times.append(draw_no)
                                prev_time_odd_lost_15 = ((draws_odd_lost_15_times[-1] - draws_odd_lost_15_times[-2]) * 75) / 60
                                times_odd_lost_15_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_15} mins since the last time Odd lost 15 times\n'
                                    f'Overall Odd has lost 15 times {times_odd_lost_15_time} in the last {time_spent}')
                    elif even_value < prev_even_percent:  # Odd won
                        if times_odd_lost > int(highest_time_lost):
                            highest_time_lost = times_odd_lost
                            # Open the loss log file in read only
                            with open('loss-log.txt', 'r') as file:
                                data = file.read()  # Read the contents of the file
                                data = data.replace(f'{highest_time_lost}', f'{times_even_lost}')  # Replace the previous highest time with the new highest
                        if times_odd_lost + 1 > 6:
                            stake = 0
                            profit = 0
                            print(f'Even has lost more than 6 times. {times_odd_lost} times exactly.')
                        elif times_odd_lost >= trigger_line and times_even_lost == 0 and times_even_lost <= 6:
                            stake = int(list(odd_stakes.keys())[times_odd_lost - trigger_line])
                            profit = int(list(odd_stakes.values())[times_odd_lost - trigger_line])
                            initial_balance = initial_balance + profit
                            print(f'#{stake} Bet on odd won. New Balance is {initial_balance}. Total profit is {initial_balance - capital}')
                        times_even_lost += 1
                        times_odd_lost = 0
                        print(f'Even has lost {times_even_lost} times.')
                        if times_even_lost >= trigger_line:  # Check if the trigger line has been passed
                            # Select the even or odd tab
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[5]/div/div[2]/div[5]').click()
                            # Select the sum even option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[1]').click()
                            # Get the stake value inputted
                            stake = driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[2]').text
                            if times_even_lost == 0:
                                pass
                            elif times_even_lost == 1:  # Bet 1: 50 (50)
                                # Click on confirm and place bet (50)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_even_lost_1_times.append(draw_no)
                                prev_time_even_lost_1 = ((draws_even_lost_1_times[-1] - draws_even_lost_1_times[-2]) * 75) / 60
                                times_even_lost_1_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_1} mins since the last time Even lost 1 times\n'
                                    f'Overall Even has lost 1 times {times_even_lost_1_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(even_stakes.keys())[times_even_lost - trigger_line])} Bet placed on even. New Balance:{initial_balance - even_amounts[times_even_lost - trigger_line]}')
                            elif times_even_lost == 2:  # Bet 2: 100 (100)
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (100)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_even_lost_2_times.append(draw_no)
                                prev_time_even_lost_2 = ((draws_even_lost_2_times[-1] - draws_even_lost_2_times[-2]) * 75) / 60
                                times_even_lost_2_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_2} mins since the last time even lost 2 times\n'
                                    f'Overall even has lost 2 times {times_even_lost_2_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(even_stakes.keys())[times_even_lost - trigger_line])} Bet placed on even. New Balance:{initial_balance - even_amounts[times_even_lost - trigger_line]}')
                            elif times_even_lost == 3:  # Bet 3: 200 (200)
                                for i in range(3):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (200)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_even_lost_3_times.append(draw_no)
                                prev_time_even_lost_3 = ((draws_even_lost_3_times[-1] - draws_even_lost_3_times[-2]) * 75) / 60
                                times_even_lost_3_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_3} mins since the last time even lost 3 times\n'
                                    f'Overall even has lost 3 times {times_even_lost_3_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(even_stakes.keys())[times_even_lost - trigger_line])} Bet placed on even. New Balance:{initial_balance - even_amounts[times_even_lost - trigger_line]}')
                            elif times_even_lost == 4:  # Bet 4: 450 (200 + 200 + 50 = 450)
                                for i in range(3):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (200)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                time.sleep(1)
                                # Select the sum even option
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                                time.sleep(0.5)
                                for i in range(3):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (200 + 200)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                time.sleep(1)
                                # Select the sum even option
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                                # Click on confirm and place bet (200 + 200 + 50)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_even_lost_4_times.append(draw_no)
                                prev_time_even_lost_4 = ((draws_even_lost_4_times[-1] - draws_even_lost_4_times[-2]) * 75) / 60
                                times_even_lost_4_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_4} mins since the last time even lost 4 times\n'
                                    f'Overall even has lost 4 times {times_even_lost_4_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(even_stakes.keys())[times_even_lost - trigger_line])} Bet placed on even. New Balance:{initial_balance - even_amounts[times_even_lost - trigger_line]}')
                            elif times_even_lost == 5:  # Bet 5: 950 (500 + 200 + 200 + 50 = 950)
                                for i in range(5):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (500)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                time.sleep(1)
                                # Select the sum even option
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                                for i in range(3):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (500 + 200 = 700)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                # Select the sum even option
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                                # Click on confirm and place bet (500 + 200 + 200 = 900)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_even_lost_5_times.append(draw_no)
                                prev_time_even_lost_5 = ((draws_even_lost_5_times[-1] - draws_even_lost_5_times[-2]) * 75) / 60
                                times_even_lost_5_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_5} mins since the last time even lost 5 times\n'
                                    f'Overall even has lost 5 times {times_even_lost_5_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(even_stakes.keys())[times_even_lost - trigger_line])} Bet placed on even. New Balance:{initial_balance - even_amounts[times_even_lost - trigger_line]}')
                            elif times_even_lost == 6:
                                for i in range(5):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (500)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                # Select the sum even option
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                                for i in range(3):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (500 + 200 = 700)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                # Select the sum even option
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                                for i in range(3):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (500 + 200 + 200 = 900)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                # Select the sum even option
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                                # Click on confirm and place bet (500 + 200 + 200 + 50 = 950)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_even_lost_6_times.append(draw_no)
                                prev_time_even_lost_6 = ((draws_even_lost_6_times[-1] - draws_even_lost_6_times[-2]) * 75) / 60
                                times_even_lost_6_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_6} mins since the last time even lost 6 times\n'
                                    f'Overall even has lost 6 times {times_even_lost_6_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(even_stakes.keys())[times_even_lost - trigger_line])} Bet placed on even. New Balance:{initial_balance - even_amounts[times_even_lost - trigger_line]}')
                            elif times_even_lost == 7:
                                draws_even_lost_7_times.append(draw_no)
                                prev_time_even_lost_7 = ((draws_even_lost_7_times[-1] - draws_even_lost_7_times[-2]) * 75) / 60
                                times_even_lost_7_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_7} mins since the last time even lost 7 times\n'
                                    f'Overall even has lost 7 times {times_even_lost_7_time} in the last {time_spent} mins')
                            elif times_even_lost == 8:
                                draws_even_lost_8_times.append(draw_no)
                                prev_time_even_lost_8 = ((draws_even_lost_8_times[-1] - draws_even_lost_8_times[-2]) * 75) / 60
                                times_even_lost_8_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_8} mins since the last time even lost 8 times\n'
                                    f'Overall even has lost 8 times {times_even_lost_8_time} in the last {time_spent} mins')
                            elif times_even_lost == 9:
                                draws_even_lost_9_times.append(draw_no)
                                prev_time_even_lost_9 = ((draws_even_lost_9_times[-1] - draws_even_lost_9_times[-2]) * 75) / 60
                                times_even_lost_9_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_9} mins since the last time even lost 9 times\n'
                                    f'Overall even has lost 9 times {times_even_lost_9_time} in the last {time_spent} mins')
                            elif times_even_lost == 10:
                                draws_even_lost_10_times.append(draw_no)
                                prev_time_even_lost_10 = ((draws_even_lost_10_times[-1] - draws_even_lost_10_times[-2]) * 75) / 60
                                times_even_lost_10_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_10} mins since the last time even lost 10 times\n'
                                    f'Overall even has lost 10 times {times_even_lost_10_time} in the last {time_spent} mins')
                            elif times_even_lost == 11:
                                draws_even_lost_11_times.append(draw_no)
                                prev_time_even_lost_11 = ((draws_even_lost_11_times[-1] - draws_even_lost_11_times[-2]) * 75) / 60
                                times_even_lost_11_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_11} mins since the last time even lost 11 times\n'
                                    f'Overall even has lost 11 times {times_even_lost_11_time} in the last {time_spent} mins')
                            elif times_even_lost == 12:
                                draws_even_lost_12_times.append(draw_no)
                                prev_time_even_lost_12 = ((draws_even_lost_12_times[-1] - draws_even_lost_12_times[-2]) * 75) / 60
                                times_even_lost_12_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_12} mins since the last time even lost 12 times\n'
                                    f'Overall even has lost 12 times {times_even_lost_12_time} in the last {time_spent} mins')
                            elif times_even_lost == 13:
                                draws_even_lost_13_times.append(draw_no)
                                prev_time_even_lost_13 = ((draws_even_lost_13_times[-1] - draws_even_lost_13_times[-2]) * 75) / 60
                                times_even_lost_13_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_13} mins since the last time even lost 13 times\n'
                                    f'Overall even has lost 13 times {times_even_lost_13_time} in the last {time_spent} mins')
                            elif times_even_lost == 14:
                                draws_even_lost_14_times.append(draw_no)
                                prev_time_even_lost_14 = ((draws_even_lost_14_times[-1] - draws_even_lost_14_times[-2]) * 75) / 60
                                times_even_lost_14_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_14} mins since the last time even lost 14 times\n'
                                    f'Overall even has lost 14 times {times_even_lost_14_time} in the last {time_spent} mins')
                            elif times_even_lost == 15:
                                draws_even_lost_15_times.append(draw_no)
                                prev_time_even_lost_15 = ((draws_even_lost_15_times[-1] - draws_even_lost_15_times[-2]) * 75) / 60
                                times_even_lost_15_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_15} mins since the last time even lost 15 times\n'
                                    f'Overall even has lost 15 times {times_even_lost_15_time} in the last {time_spent}')
                    elif even_value - prev_even_percent > 0:
                        if times_even_lost > int(highest_time_lost):
                            highest_time_lost = times_even_lost
                            # Open the loss log file in read only
                            with open('loss-log.txt', 'r') as file:
                                data = file.read()  # Read the contents of the file
                                data = data.replace(f'{highest_time_lost}',
                                                    f'{times_even_lost}')  # Replace the previous highest time with the new highest
                        if times_even_lost + 1 > 6:
                            stake = 0
                            profit = 0
                            print(f'Even has lost more than 6 times. {times_even_lost} times exactly.')
                        elif times_even_lost >= trigger_line and times_odd_lost == 0:
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
                            if times_odd_lost == 0:
                                pass
                            elif times_odd_lost == 1:  # Bet 1: 50 (50)
                                # Click on confirm and place bet (50)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_odd_lost_1_times.append(draw_no)
                                prev_time_odd_lost_1 = ((draws_odd_lost_1_times[-1] - draws_odd_lost_1_times[
                                    -2]) * 75) / 60
                                times_odd_lost_1_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_1} mins since the last time Odd lost 1 times\n'
                                    f'Overall Odd has lost 1 times {times_odd_lost_1_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(odd_stakes.keys())[times_odd_lost - trigger_line])} Bet placed on odd. New Balance:{initial_balance - odd_amounts[times_odd_lost - trigger_line]}')
                            elif times_odd_lost == 2:  # Bet 2: 100 (100)
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (100)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_odd_lost_2_times.append(draw_no)
                                prev_time_odd_lost_2 = ((draws_odd_lost_2_times[-1] - draws_odd_lost_2_times[
                                    -2]) * 75) / 60
                                times_odd_lost_2_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_2} mins since the last time Odd lost 2 times\n'
                                    f'Overall Odd has lost 2 times {times_odd_lost_2_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(odd_stakes.keys())[times_odd_lost - trigger_line])} Bet placed on odd. New Balance:{initial_balance - odd_amounts[times_odd_lost - trigger_line]}')
                            elif times_odd_lost == 3:  # Bet 3: 200 (200)
                                for i in range(3):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (200)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_odd_lost_3_times.append(draw_no)
                                prev_time_odd_lost_3 = ((draws_odd_lost_3_times[-1] - draws_odd_lost_3_times[
                                    -2]) * 75) / 60
                                times_odd_lost_3_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_3} mins since the last time Odd lost 3 times\n'
                                    f'Overall Odd has lost 3 times {times_odd_lost_3_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(odd_stakes.keys())[times_odd_lost - trigger_line])} Bet placed on odd. New Balance:{initial_balance - odd_amounts[times_odd_lost - trigger_line]}')
                            elif times_odd_lost == 4:  # Bet 4: 450 (200 + 200 + 50 = 450)
                                for i in range(3):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (200)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                time.sleep(1)
                                # Select the sum odd option
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                                time.sleep(0.5)
                                for i in range(3):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (200 + 200)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                time.sleep(1)
                                # Select the sum odd option
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                                # Click on confirm and place bet (200 + 200 + 50)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_odd_lost_4_times.append(draw_no)
                                prev_time_odd_lost_4 = ((draws_odd_lost_4_times[-1] - draws_odd_lost_4_times[
                                    -2]) * 75) / 60
                                times_odd_lost_4_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_4} mins since the last time Odd lost 4 times\n'
                                    f'Overall Odd has lost 4 times {times_odd_lost_4_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(odd_stakes.keys())[times_odd_lost - trigger_line])} Bet placed on odd. New Balance:{initial_balance - odd_amounts[times_odd_lost - trigger_line]}')
                            elif times_odd_lost == 5:  # Bet 5: 950 (500 + 200 + 200 + 50 = 950)
                                for i in range(5):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (500)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                time.sleep(1)
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
                                # Click on confirm and place bet (500 + 200 + 200 = 900)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_odd_lost_5_times.append(draw_no)
                                prev_time_odd_lost_5 = ((draws_odd_lost_5_times[-1] - draws_odd_lost_5_times[
                                    -2]) * 75) / 60
                                times_odd_lost_5_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_5} mins since the last time Odd lost 5 times\n'
                                    f'Overall Odd has lost 5 times {times_odd_lost_5_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(odd_stakes.keys())[times_odd_lost - trigger_line])} Bet placed on odd. New Balance:{initial_balance - odd_amounts[times_odd_lost - trigger_line]}')
                            elif times_odd_lost == 6:
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
                                draws_odd_lost_6_times.append(draw_no)
                                prev_time_odd_lost_6 = ((draws_odd_lost_6_times[-1] - draws_odd_lost_6_times[
                                    -2]) * 75) / 60
                                times_odd_lost_6_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_6} mins since the last time Odd lost 6 times\n'
                                    f'Overall Odd has lost 6 times {times_odd_lost_6_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(odd_stakes.keys())[times_odd_lost - trigger_line])} Bet placed on odd. New Balance:{initial_balance - odd_amounts[times_odd_lost - trigger_line]}')
                            elif times_odd_lost == 7:
                                draws_odd_lost_7_times.append(draw_no)
                                prev_time_odd_lost_7 = ((draws_odd_lost_7_times[-1] - draws_odd_lost_7_times[
                                    -2]) * 75) / 60
                                times_odd_lost_7_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_7} mins since the last time Odd lost 7 times\n'
                                    f'Overall Odd has lost 7 times {times_odd_lost_7_time} in the last {time_spent} mins')
                            elif times_odd_lost == 8:
                                draws_odd_lost_8_times.append(draw_no)
                                prev_time_odd_lost_8 = ((draws_odd_lost_8_times[-1] - draws_odd_lost_8_times[
                                    -2]) * 75) / 60
                                times_odd_lost_8_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_8} mins since the last time Odd lost 8 times\n'
                                    f'Overall Odd has lost 8 times {times_odd_lost_8_time} in the last {time_spent} mins')
                            elif times_odd_lost == 9:
                                draws_odd_lost_9_times.append(draw_no)
                                prev_time_odd_lost_9 = ((draws_odd_lost_9_times[-1] - draws_odd_lost_9_times[
                                    -2]) * 75) / 60
                                times_odd_lost_9_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_9} mins since the last time Odd lost 9 times\n'
                                    f'Overall Odd has lost 9 times {times_odd_lost_9_time} in the last {time_spent} mins')
                            elif times_odd_lost == 10:
                                draws_odd_lost_10_times.append(draw_no)
                                prev_time_odd_lost_10 = ((draws_odd_lost_10_times[-1] - draws_odd_lost_10_times[
                                    -2]) * 75) / 60
                                times_odd_lost_10_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_10} mins since the last time Odd lost 10 times\n'
                                    f'Overall Odd has lost 10 times {times_odd_lost_10_time} in the last {time_spent} mins')
                            elif times_odd_lost == 11:
                                draws_odd_lost_11_times.append(draw_no)
                                prev_time_odd_lost_11 = ((draws_odd_lost_11_times[-1] - draws_odd_lost_11_times[
                                    -2]) * 75) / 60
                                times_odd_lost_11_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_11} mins since the last time Odd lost 11 times\n'
                                    f'Overall Odd has lost 11 times {times_odd_lost_11_time} in the last {time_spent} mins')
                            elif times_odd_lost == 12:
                                draws_odd_lost_12_times.append(draw_no)
                                prev_time_odd_lost_12 = ((draws_odd_lost_12_times[-1] - draws_odd_lost_12_times[
                                    -2]) * 75) / 60
                                times_odd_lost_12_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_12} mins since the last time Odd lost 12 times\n'
                                    f'Overall Odd has lost 12 times {times_odd_lost_12_time} in the last {time_spent} mins')
                            elif times_odd_lost == 13:
                                draws_odd_lost_13_times.append(draw_no)
                                prev_time_odd_lost_13 = ((draws_odd_lost_13_times[-1] - draws_odd_lost_13_times[
                                    -2]) * 75) / 60
                                times_odd_lost_13_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_13} mins since the last time Odd lost 13 times\n'
                                    f'Overall Odd has lost 13 times {times_odd_lost_13_time} in the last {time_spent} mins')
                            elif times_odd_lost == 14:
                                draws_odd_lost_14_times.append(draw_no)
                                prev_time_odd_lost_14 = ((draws_odd_lost_14_times[-1] - draws_odd_lost_14_times[
                                    -2]) * 75) / 60
                                times_odd_lost_14_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_14} mins since the last time Odd lost 14 times\n'
                                    f'Overall Odd has lost 14 times {times_odd_lost_14_time} in the last {time_spent} mins')
                            elif times_odd_lost == 15:
                                draws_odd_lost_15_times.append(draw_no)
                                prev_time_odd_lost_15 = ((draws_odd_lost_15_times[-1] - draws_odd_lost_15_times[
                                    -2]) * 75) / 60
                                times_odd_lost_15_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_odd_lost_15} mins since the last time Odd lost 15 times\n'
                                    f'Overall Odd has lost 15 times {times_odd_lost_15_time} in the last {time_spent}')
                    elif even_value - prev_even_percent < 0:
                        if times_odd_lost > int(highest_time_lost):
                            highest_time_lost = times_odd_lost
                            # Open the loss log file in read only
                            with open('loss-log.txt', 'r') as file:
                                data = file.read()  # Read the contents of the file
                                data = data.replace(f'{highest_time_lost}', f'{times_even_lost}')  # Replace the previous highest time with the new highest
                        if times_even_lost + 1 > 6:
                            stake = 0
                            profit = 0
                            print(f'Even has lost more than 6 times. {times_even_lost} times exactly.')
                        elif times_odd_lost >= trigger_line and times_even_lost == 0:
                            stake = int(list(odd_stakes.keys())[times_odd_lost - trigger_line])
                            profit = int(list(odd_stakes.values())[times_odd_lost - trigger_line])
                            initial_balance = initial_balance + profit
                            print(f'#{stake} Bet on odd won. New Balance is {initial_balance}. Total profit is {initial_balance - capital}')
                        times_even_lost += 1
                        times_odd_lost = 0
                        print(f'Even has lost {times_even_lost} times.')
                        if times_even_lost >= trigger_line:  # Check if the trigger line has been passed
                            # Select the even or odd tab
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[5]/div/div[2]/div[5]').click()
                            # Select the sum even option
                            driver.find_element(By.XPATH,
                                                '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[1]').click()
                            # Get the stake value inputted
                            stake = driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[2]').text
                            if times_even_lost == 0:
                                pass
                            elif times_even_lost == 1:  # Bet 1: 50 (50)
                                # Click on confirm and place bet (50)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_even_lost_1_times.append(draw_no)
                                prev_time_even_lost_1 = ((draws_even_lost_1_times[-1] - draws_even_lost_1_times[-2]) * 75) / 60
                                times_even_lost_1_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_1} mins since the last time Even lost 1 times\n'
                                    f'Overall Even has lost 1 times {times_even_lost_1_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(even_stakes.keys())[times_even_lost - trigger_line])} Bet placed on even. New Balance:{initial_balance - even_amounts[times_even_lost - trigger_line]}')
                            elif times_even_lost == 2:  # Bet 2: 100 (100)
                                # Increase the stake
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (100)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_even_lost_2_times.append(draw_no)
                                prev_time_even_lost_2 = ((draws_even_lost_2_times[-1] - draws_even_lost_2_times[-2]) * 75) / 60
                                times_even_lost_2_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_2} mins since the last time even lost 2 times\n'
                                    f'Overall even has lost 2 times {times_even_lost_2_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(even_stakes.keys())[times_even_lost - trigger_line])} Bet placed on even. New Balance:{initial_balance - even_amounts[times_even_lost - trigger_line]}')
                            elif times_even_lost == 3:  # Bet 3: 200 (200)
                                for i in range(3):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (200)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_even_lost_3_times.append(draw_no)
                                prev_time_even_lost_3 = ((draws_even_lost_3_times[-1] - draws_even_lost_3_times[-2]) * 75) / 60
                                times_even_lost_3_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_3} mins since the last time even lost 3 times\n'
                                    f'Overall even has lost 3 times {times_even_lost_3_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(even_stakes.keys())[times_even_lost - trigger_line])} Bet placed on even. New Balance:{initial_balance - even_amounts[times_even_lost - trigger_line]}')
                            elif times_even_lost == 4:  # Bet 4: 450 (200 + 200 + 50 = 450)
                                for i in range(3):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (200)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                time.sleep(1)
                                # Select the sum even option
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                                time.sleep(0.5)
                                for i in range(3):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (200 + 200)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                time.sleep(1)
                                # Select the sum even option
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                                # Click on confirm and place bet (200 + 200 + 50)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_even_lost_4_times.append(draw_no)
                                prev_time_even_lost_4 = ((draws_even_lost_4_times[-1] - draws_even_lost_4_times[-2]) * 75) / 60
                                times_even_lost_4_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_4} mins since the last time even lost 4 times\n'
                                    f'Overall even has lost 4 times {times_even_lost_4_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(even_stakes.keys())[times_even_lost - trigger_line])} Bet placed on even. New Balance:{initial_balance - even_amounts[times_even_lost - trigger_line]}')
                            elif times_even_lost == 5:  # Bet 5: 950 (500 + 200 + 200 + 50 = 950)
                                for i in range(5):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (500)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                time.sleep(1)
                                # Select the sum even option
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                                for i in range(3):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (500 + 200 = 700)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                # Select the sum even option
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                                # Click on confirm and place bet (500 + 200 + 200 = 900)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_even_lost_5_times.append(draw_no)
                                prev_time_even_lost_5 = ((draws_even_lost_5_times[-1] - draws_even_lost_5_times[-2]) * 75) / 60
                                times_even_lost_5_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_5} mins since the last time even lost 5 times\n'
                                    f'Overall even has lost 5 times {times_even_lost_5_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(even_stakes.keys())[times_even_lost - trigger_line])} Bet placed on even. New Balance:{initial_balance - even_amounts[times_even_lost - trigger_line]}')
                            elif times_even_lost == 6:
                                for i in range(5):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (500)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                # Select the sum even option
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                                for i in range(3):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (500 + 200 = 700)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                # Select the sum even option
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                                for i in range(3):
                                    # Increase the stake
                                    driver.find_element(By.XPATH,
                                                        '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[4]/div[2]/div[3]').click()
                                # Click on confirm and place bet (500 + 200 + 200 = 900)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                # Select the sum even option
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[2]/div[2]').click()
                                # Click on confirm and place bet (500 + 200 + 200 + 50 = 950)
                                driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div/div[1]/div[6]/div[3]/div[7]/div[2]').click()
                                draws_even_lost_6_times.append(draw_no)
                                prev_time_even_lost_6 = ((draws_even_lost_6_times[-1] - draws_even_lost_6_times[-2]) * 75) / 60
                                times_even_lost_6_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_6} mins since the last time even lost 6 times\n'
                                    f'Overall even has lost 6 times {times_even_lost_6_time} in the last {time_spent} mins')
                                print(
                                    f'#{int(list(even_stakes.keys())[times_even_lost - trigger_line])} Bet placed on even. New Balance:{initial_balance - even_amounts[times_even_lost - trigger_line]}')
                            elif times_even_lost == 7:
                                draws_even_lost_7_times.append(draw_no)
                                prev_time_even_lost_7 = ((draws_even_lost_7_times[-1] - draws_even_lost_7_times[-2]) * 75) / 60
                                times_even_lost_7_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_7} mins since the last time even lost 7 times\n'
                                    f'Overall even has lost 7 times {times_even_lost_7_time} in the last {time_spent} mins')
                            elif times_even_lost == 8:
                                draws_even_lost_8_times.append(draw_no)
                                prev_time_even_lost_8 = ((draws_even_lost_8_times[-1] - draws_even_lost_8_times[-2]) * 75) / 60
                                times_even_lost_8_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_8} mins since the last time even lost 8 times\n'
                                    f'Overall even has lost 8 times {times_even_lost_8_time} in the last {time_spent} mins')
                            elif times_even_lost == 9:
                                draws_even_lost_9_times.append(draw_no)
                                prev_time_even_lost_9 = ((draws_even_lost_9_times[-1] - draws_even_lost_9_times[-2]) * 75) / 60
                                times_even_lost_9_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_9} mins since the last time even lost 9 times\n'
                                    f'Overall even has lost 9 times {times_even_lost_9_time} in the last {time_spent} mins')
                            elif times_even_lost == 10:
                                draws_even_lost_10_times.append(draw_no)
                                prev_time_even_lost_10 = ((draws_even_lost_10_times[-1] - draws_even_lost_10_times[-2]) * 75) / 60
                                times_even_lost_10_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_10} mins since the last time even lost 10 times\n'
                                    f'Overall even has lost 10 times {times_even_lost_10_time} in the last {time_spent} mins')
                            elif times_even_lost == 11:
                                draws_even_lost_11_times.append(draw_no)
                                prev_time_even_lost_11 = ((draws_even_lost_11_times[-1] - draws_even_lost_11_times[-2]) * 75) / 60
                                times_even_lost_11_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_11} mins since the last time even lost 11 times\n'
                                    f'Overall even has lost 11 times {times_even_lost_11_time} in the last {time_spent} mins')
                            elif times_even_lost == 12:
                                draws_even_lost_12_times.append(draw_no)
                                prev_time_even_lost_12 = ((draws_even_lost_12_times[-1] - draws_even_lost_12_times[-2]) * 75) / 60
                                times_even_lost_12_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_12} mins since the last time even lost 12 times\n'
                                    f'Overall even has lost 12 times {times_even_lost_12_time} in the last {time_spent} mins')
                            elif times_even_lost == 13:
                                draws_even_lost_13_times.append(draw_no)
                                prev_time_even_lost_13 = ((draws_even_lost_13_times[-1] - draws_even_lost_13_times[-2]) * 75) / 60
                                times_even_lost_13_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_13} mins since the last time even lost 13 times\n'
                                    f'Overall even has lost 13 times {times_even_lost_13_time} in the last {time_spent} mins')
                            elif times_even_lost == 14:
                                draws_even_lost_14_times.append(draw_no)
                                prev_time_even_lost_14 = ((draws_even_lost_14_times[-1] - draws_even_lost_14_times[-2]) * 75) / 60
                                times_even_lost_14_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_14} mins since the last time even lost 14 times\n'
                                    f'Overall even has lost 14 times {times_even_lost_14_time} in the last {time_spent} mins')
                            elif times_even_lost == 15:
                                draws_even_lost_15_times.append(draw_no)
                                prev_time_even_lost_15 = ((draws_even_lost_15_times[-1] - draws_even_lost_15_times[-2]) * 75) / 60
                                times_even_lost_15_time += 1
                                time_spent = (draw_no * 75) / 60
                                print(
                                    f'It has been {prev_time_even_lost_15} mins since the last time even lost 15 times\n'
                                    f'Overall even has lost 15 times {times_even_lost_15_time} in the last {time_spent}')

