from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from datetime import datetime
import time

# import math
percentage_increment = 2
cycle = 0
expected_profit = 0
red_balls_amount = 50
blue_balls_amount = 50
green_balls_amount = 50
red_losses = 0
blue_losses = 0
green_losses = 0
original_amount = 50
trigger = 0

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)


# user_account_name = input('Enter your username: \n')
# user_password = input('Enter your password: \n')

# Login to Betnaija Account
def login_b9():
    driver.get('https://sports.bet9ja.com/mobile/login')
    time.sleep(2)
    username = driver.find_element(By.XPATH,
                                   "/html/body/div[1]/div/div/div[1]/main/div/div/div/div[2]/div/input")
    username.send_keys('YayaScott')
    password = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div/div[1]/main/div/div/div/div[3]/div/input')
    password.send_keys('Subaruboys11', '\ue006')
    # Click on submit
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/main/div/div/div/button').click()
    time.sleep(4)
    # Close deposit prompt
    # driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/main/div[2]/div[1]/div/div/div/a').click()
    # Click on casino button
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[3]/div[2]').click()
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
    time.sleep(15)
    # driver.find_element(By.XPATH, '/html/body/div[2]/section/main/div/div[1]/button').click()
    time.sleep(10)
    # Click on popular tab
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[1]/div[2]/div[1]/div/div[2]/div[2]/div').click()
    time.sleep(3)
    # Click Game Ribbons Class
    driver.find_element(By.CLASS_NAME, 'game-ribbons').click()
    # Click on play demo
    # driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]'
    #                     '/div[1]/div/div[3]/button[2]').click()

    # Click on live game
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div'
                                  '[1]/div/div[3]/button[1]').click()

    driver.close()


def start_49():
    global red_balls_amount, green_balls_amount, blue_balls_amount, cycle, expected_profit, red_losses, blue_losses, green_losses
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    initial_balance = float(driver.find_element(By.XPATH,
                                          '/html/body/div[1]/div/div/div/header/div/div[2]/div[1]/span').text)
    # Click on Rainbow Tab
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div/div/div/main/div[2]/div[1]/a[4]').click()
    while expected_profit < 10000:
        balance = float(driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/header/div/div[2]/div[1]/span').text)
        print(balance)
        if balance >= initial_balance + 5000:
            expected_profit = 10000

        # Time to sleep
        time_sec = int(driver.find_element(By.XPATH,
                                           '/html/body/div[1]/div/div/div/footer/div[2]/div[4]/div/div/div').text)
        print(f'Next in {time_sec} seconds')
        time.sleep(time_sec + 18)

        # Click on the Statistics Tab again to go back to the Rainbow Panel
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div/div/main/div[1]/div[1]').click()
        time.sleep(2)
        # Check For Red Balls
        red_balls = int(driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/'
                                            'tr[1]/td[5]/div/div[1]').text)
        # Check For Green Balls
        green_balls = int(driver.find_element(By.XPATH,
                                              '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody'
                                              '/tr[1]/td[5]/div/div[2]').text)
        # Check for Blue Balls
        blue_balls = int(driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody'
                                             '/tr[1]/td[5]/div/div[3]').text)
        time.sleep(5)
        # Click on the Statistics Tab again to go back to the Rainbow Panel
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div/div/main/div[1]/div[1]').click()
        if red_balls < 2:
            cycle += 1
            red_losses += 1
            print(f'There were {red_balls} red balls. Lost. Red has lost {red_losses} times.')
            if red_losses > trigger:
                driver.refresh()
                time.sleep(2)
                # Click on Rainbow Tab
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[1]/a[4]').click()
                # For 2+ red balls
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]'
                                    '/div/div[1]/div[2]/div/div').click()

                # Clear the input space
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/'
                                    'div[2]/div[1]/div[1]/input').clear()

                # Input the amount to bet
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]'
                                    '/div[1]/div[1]/input') \
                    .send_keys(red_balls_amount)
                amount_entered_red = int(
                    driver.find_element(By.XPATH, '//html/body/div[1]/div/div/div/main/div[2]/div[2]/'
                                                  'div[3]/div/div[2]/div[2]/div[2]/input').get_attribute(
                        'value').encode('utf-8'))
                if amount_entered_red != red_balls_amount:
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div'
                                        '/div[2]/div[1]/div[1]/input').clear()
                    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]'
                                                  '/div/div[2]/div[1]/div[1]/input') \
                        .send_keys(red_balls_amount)
                    print(f'Changed {amount_entered_red} back to {red_balls_amount}')

                # Click on place bet
                time.sleep(2)
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]'
                                              '/div[2]/div[3]/div/div[2]/div[3]').click()
                time.sleep(1)
                red_balls_amount += int(percentage_increment * red_balls_amount)
            else:
                pass

        else:
            print(f'There were {red_balls} red balls. Won. ')
            red_balls_amount = original_amount
            red_losses = 0

        if blue_balls < 2:
            cycle += 1
            blue_losses += 1
            print(f'There were {blue_balls} blue balls. Lost. Blue has lost {blue_losses} times.')
            if blue_losses > trigger:
                driver.refresh()
                time.sleep(2)
                # Click on Rainbow Tab
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[1]/a[4]').click()
                # For 2+ blue balls
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/'
                                    'div[2]/div[2]/div/div').click()

                # Clear the input space
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/'
                                    'div[2]/div[1]/div[1]/input').clear()

                # Input the amount to bet
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]'
                                    '/div[1]/div[1]/input') \
                    .send_keys(blue_balls_amount)
                amount_entered_blue = int(
                    driver.find_element(By.XPATH, '//html/body/div[1]/div/div/div/main/div[2]/div[2]/'
                                                  'div[3]/div/div[2]/div[2]/div[2]/input').get_attribute(
                        'value').encode('utf-8'))
                if amount_entered_blue != blue_balls_amount:
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div'
                                        '/div[2]/div[1]/div[1]/input').clear()
                    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]'
                                                  '/div/div[2]/div[1]/div[1]/input') \
                        .send_keys(blue_balls_amount)
                    print(f'Changed {amount_entered_blue} back to {blue_balls_amount}')

                # Click on place bet
                time.sleep(2)
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]'
                                              '/div[2]/div[3]/div/div[2]/div[3]').click()
                time.sleep(1)
                blue_balls_amount += int(percentage_increment * blue_balls_amount)
            else:
                pass

        else:
            print(f'There were {blue_balls} blue balls. Won. ')
            blue_balls_amount = original_amount
            blue_losses = 0

        if green_balls < 2:
            cycle += 1
            green_losses += 1
            print(f'There were {green_balls} green balls. Lost. Green has lost {green_losses} times.')
            if green_losses > trigger:
                driver.refresh()
                time.sleep(2)
                # Click on Rainbow Tab
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[1]/a[4]').click()
                # For 2+ green balls
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div'
                                    '/div[3]/div[2]/div/div').click()

                # Clear the input space
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/'
                                    'div[2]/div[1]/div[1]/input').clear()

                # Input the amount to bet
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div/div[2]'
                                    '/div[1]/div[1]/input') \
                    .send_keys(green_balls_amount)
                amount_entered_green = int(
                    driver.find_element(By.XPATH, '//html/body/div[1]/div/div/div/main/div[2]/div[2]/'
                                                  'div[3]/div/div[2]/div[2]/div[2]/input').get_attribute(
                        'value').encode('utf-8'))
                if amount_entered_green != green_balls_amount:
                    driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]/div'
                                        '/div[2]/div[1]/div[1]/input').clear()
                    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[3]'
                                                  '/div/div[2]/div[1]/div[1]/input') \
                        .send_keys(green_balls_amount)
                    print(f'Changed {amount_entered_green} back to {green_balls_amount}')

                # Click on place bet
                time.sleep(2)
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]'
                                              '/div[2]/div[3]/div/div[2]/div[3]').click()
                time.sleep(1)
                green_balls_amount += int(percentage_increment * green_balls_amount)
            else:
                pass

        else:
            print(f'There were {green_balls} green balls. Won. ')
            green_balls_amount = original_amount
            green_losses = 0


login_b9()
start_49()





