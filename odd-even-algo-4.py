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


times_odd_won_after_1 = 0
times_even_won_after_1 = 0
times_even_won_after_2 = 0
times_odd_won_after_2 = 0

draws_odd_won_after_1 = [0]
draws_odd_won_after_2 = [0]
draws_even_won_after_1 = [0]
draws_even_won_after_2 = [0]

overall_times_won = 0
overall_times_lost = 0

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
                                data = data.replace(f'{highest_time_lost}',
                                                    f'{times_even_lost}')  # Replace the previous highest time with the new highest
                        if times_even_lost == 1:
                            draws_even_won_after_1.append(draw_no)
                            last_time_even_won_after_1 = draws_even_won_after_1[-1] - draws_even_won_after_1[-2]
                            time_spent = (draw_no * 75) / 60
                            times_even_won_after_1 += 1
                            overall_times_won += 1
                            print(
                                f'Even has won after the first trial, {times_even_won_after_1} times. \nIt has been {last_time_even_won_after_1} mins since it last won'
                                f'\nOverall, Even has won after the first trial {times_even_won_after_1} times in {time_spent} mins'
                                f'Bet was won after 1 times {overall_times_won} times so far.')
                        elif times_even_lost > 1:
                            draws_even_won_after_2.append(draw_no)
                            last_time_even_won_after_2 = draws_even_won_after_2[-1] - draws_even_won_after_2[-2]
                            time_spent = (draw_no * 75) / 60
                            times_even_won_after_2 += 1
                            overall_times_lost += 1
                            print(
                                f'Even has won after the more than the first trial,{times_even_won_after_2} times. \nIt has been {last_time_even_won_after_2} since it last won'
                                f'\nOverall, Even has won after more than the first trial {times_even_won_after_2} times in {time_spent} mins'
                                f'Bet was won after more than 1 times {overall_times_lost} times so far.')
                        times_odd_lost += 1
                        times_even_lost = 0
                        print(f'Odd has lost {times_odd_lost} times.')
                    elif even_value < prev_even_percent:  # Odd won
                        if times_odd_lost > int(highest_time_lost):
                            highest_time_lost = times_odd_lost
                            # Open the loss log file in read only
                            with open('loss-log.txt', 'r') as file:
                                data = file.read()  # Read the contents of the file
                                data = data.replace(f'{highest_time_lost}',
                                                    f'{times_odd_lost}')  # Replace the previous highest time with the new highest
                        if times_odd_lost == 1:
                            draws_odd_won_after_1.append(draw_no)
                            last_time_odd_won_after_1 = draws_odd_won_after_1[-1] - draws_odd_won_after_1[-2]
                            time_spent = (draw_no * 75) / 60
                            times_odd_won_after_1 += 1
                            overall_times_won += 1
                            print(
                                f'Odd has won after the first trial, {times_odd_won_after_1} times. \nIt has been {last_time_odd_won_after_1} mins since it last won'
                                f'\nOverall, Odd has won after the first trial {times_odd_won_after_1} times in {time_spent} mins'
                                f'Bet was won after 1 times {overall_times_won} times so far.')
                        elif times_odd_lost > 1:
                            draws_odd_won_after_2.append(draw_no)
                            last_time_odd_won_after_2 = draws_odd_won_after_2[-1] - draws_odd_won_after_2[-2]
                            time_spent = (draw_no * 75) / 60
                            times_odd_won_after_2 += 1
                            overall_times_lost += 1
                            print(
                                f'Odd has won after more than the first trial, {times_odd_won_after_2} times. \nIt has been {last_time_odd_won_after_2} mins since it last won'
                                f'\nOverall, Odd has won after more than the first trial {times_odd_won_after_2} times in {time_spent} mins'
                                f'Bet was won after more than 1 times {overall_times_lost} times so far.')
                        times_even_lost += 1
                        times_odd_lost = 0
                        print(f'Even has lost {times_even_lost} times.')
                    elif even_value - prev_even_percent > 0:  # Even won
                        if times_even_lost > int(highest_time_lost):
                            highest_time_lost = times_even_lost
                            # Open the loss log file in read only
                            with open('loss-log.txt', 'r') as file:
                                data = file.read()  # Read the contents of the file
                                data = data.replace(f'{highest_time_lost}',
                                                    f'{times_even_lost}')  # Replace the previous highest time with the new highest
                        if times_even_lost == 1:
                            draws_even_won_after_1.append(draw_no)
                            last_time_even_won_after_1 = draws_even_won_after_1[-1] - draws_even_won_after_1[-2]
                            time_spent = (draw_no * 75) / 60
                            times_even_won_after_1 += 1
                            overall_times_won += 1
                            print(
                                f'Even has won after the first trial, {times_even_won_after_1} times. \nIt has been {last_time_even_won_after_1} mins since it last won'
                                f'\nOverall, Even has won after the first trial {times_even_won_after_1} times in {time_spent} mins'
                                f'Bet was won after 1 times {overall_times_won} times so far.')
                        elif times_even_lost > 1:
                            draws_even_won_after_2.append(draw_no)
                            last_time_even_won_after_2 = draws_even_won_after_2[-1] - draws_even_won_after_2[-2]
                            time_spent = (draw_no * 75) / 60
                            times_even_won_after_2 += 1
                            overall_times_lost += 1
                            print(
                                f'Even has won after the more than the first trial,{times_even_won_after_2} times. \nIt has been {last_time_even_won_after_2} since it last won'
                                f'\nOverall, Even has won after more than the first trial {times_even_won_after_2} times in {time_spent} mins'
                                f'Bet was won after more than 1 times {overall_times_lost} times so far.')
                        times_odd_lost += 1
                        times_even_lost = 0
                        print(f'Odd has lost {times_odd_lost} times.')
                    elif even_value - prev_even_percent < 0:
                        if times_odd_lost > int(highest_time_lost):
                            highest_time_lost = times_odd_lost
                            # Open the loss log file in read only
                            with open('loss-log.txt', 'r') as file:
                                data = file.read()  # Read the contents of the file
                                data = data.replace(f'{highest_time_lost}',
                                                    f'{times_odd_lost}')  # Replace the previous highest time with the new highest
                        if times_odd_lost == 1:
                            draws_odd_won_after_1.append(draw_no)
                            last_time_odd_won_after_1 = draws_odd_won_after_1[-1] - draws_odd_won_after_1[-2]
                            time_spent = (draw_no * 75) / 60
                            times_odd_won_after_1 += 1
                            overall_times_won += 1
                            print(
                                f'Odd has won after the first trial, {times_odd_won_after_1} times. \nIt has been {last_time_odd_won_after_1} mins since it last won'
                                f'Bet was won after 1 times {overall_times_won} times so far.')
                        elif times_odd_lost > 1:
                            draws_odd_won_after_2.append(draw_no)
                            last_time_odd_won_after_2 = draws_odd_won_after_2[-1] - draws_odd_won_after_2[-2]
                            time_spent = (draw_no * 75) / 60
                            times_odd_won_after_2 += 1
                            overall_times_lost += 1
                            print(
                                f'Odd has won after the more than the first trial, {times_odd_won_after_2} times. \nIt has been {last_time_odd_won_after_2} mins since it last won'
                                f'\nOverall, Odd has won after more than the first trial {times_odd_won_after_2} times in {time_spent} mins'
                                f'Bet was won after more than 1 times {overall_times_lost} times so far.')
                        times_even_lost += 1
                        times_odd_lost = 0
                        print(f'Even has lost {times_even_lost} times.')
                time_spent = (draw_no * 75)/60
                print(f'Overall bet was won after 1 times {overall_times_won} times in the last {time_spent} mins'
                      f'\nOverall bet was won after more than 1 times {overall_times_lost} times in the last {time_spent} mins')
