from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

stakes = ['50', '150', '450', '1350', '4050']
trigger_line = 30
capital = 15000

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
username = 'pulverine'
password = 'Abdulsalam1'

bet_numbers = []
bet_numbers_frequencies = []
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

driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div['
                              '2]/div/div[3]/button[2]').click()
driver.switch_to.window(driver.window_handles[1])

while True:
    try:
        # Find the statistics button
        element = WebDriverWait(driver, 30).until(
            # Find the statistics button
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div[1]/div/div/div/main/div[1]/div[1]')),
            # Find timer
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div[1]/div/div/div/footer/div[2]/div[4]/div/div/div'))
        )
    finally:
        # Get the current time
        curr_time = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/footer/div[2]/div[4]/div/div/div').text
    if curr_time == '40':
        driver.refresh()
        try:
            # Find the statistics button
            element = WebDriverWait(driver, 30).until(
                # Find the statistics button
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[1]/div[1]')),
            )
        finally:
            #  Click on Statistics Tab
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[1]/div[1]').click()

        # Click on the bet49 tab1
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[4]/div[1]/div[2]/a').click()
        # Click on the last 100 draws
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[4]/div[1]/div[2]/div/div[1]/div').click()
        time.sleep(7)
        number_frequency = {
            1: driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[1]/td[4]').text,
            2: driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[2]/td[4]').text,
            3: driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[3]/td[4]').text,
            4: driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[4]/td[4]').text,
            5: driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[5]/td[4]').text,
            6: driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[6]/td[4]').text,
            7: driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[7]/td[4]').text,
            8: driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[8]/td[4]').text,
            9: driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[9]/td[4]').text,
            10: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[10]/td[4]').text,
            11: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[11]/td[4]').text,
            12: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[12]/td[4]').text,
            13: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[13]/td[4]').text,
            14: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[14]/td[4]').text,
            15: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[15]/td[4]').text,
            16: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[16]/td[4]').text,
            17: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[17]/td[4]').text,
            18: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[18]/td[4]').text,
            19: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[19]/td[4]').text,
            20: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[20]/td[4]').text,
            21: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[21]/td[4]').text,
            22: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[22]/td[4]').text,
            23: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[23]/td[4]').text,
            24: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[24]/td[4]').text,
            25: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[25]/td[4]').text,
            26: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[26]/td[4]').text,
            27: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[27]/td[4]').text,
            28: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[28]/td[4]').text,
            29: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[29]/td[4]').text,
            30: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[30]/td[4]').text,
            31: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[31]/td[4]').text,
            32: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[32]/td[4]').text,
            33: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[33]/td[4]').text,
            34: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[34]/td[4]').text,
            35: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[35]/td[4]').text,
            36: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[36]/td[4]').text,
            37: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[37]/td[4]').text,
            38: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[38]/td[4]').text,
            39: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[39]/td[4]').text,
            40: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[40]/td[4]').text,
            41: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[41]/td[4]').text,
            42: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[42]/td[4]').text,
            43: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[43]/td[4]').text,
            44: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[44]/td[4]').text,
            45: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[45]/td[4]').text,
            46: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[46]/td[4]').text,
            47: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[47]/td[4]').text,
            48: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[48]/td[4]').text,
            49: driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[49]/td[4]').text,
        }
        for i in bet_numbers:
            if number_frequency[i] == '0':
                print(f'{i} has won.')
        bet_numbers.clear()
        bet_numbers_frequencies.clear()
        for i in number_frequency:
            number_frequency[i] = int(number_frequency[i])
            if number_frequency[i] >= 30:
                bet_numbers.append(i)
                bet_numbers_frequencies.append(number_frequency[i])
        for i in range(len(bet_numbers)):
            print(f'{bet_numbers[i]} has lost {bet_numbers_frequencies[i]} times')
        print('------------------------------------------------------------------')
        #  Click on Statistics Tab
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[1]/div[1]').click()
        # Click on the Bet49 tab
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[1]/a[1]').click()
        time.sleep(1)
        ball_numbers = {1: driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[1]'),
                        2: driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]'),
                        3: driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[3]'),
                        4: driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[4]'),
                        5: driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[5]'),
                        6: driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[6]'),
                        7: driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[7]'),
                        8: driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[8]'),
                        9: driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[9]'),
                        10: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[10]'),
                        11: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[11]'),
                        12: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[12]'),
                        13: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[1]'),
                        14: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[2]'),
                        15: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[3]'),
                        16: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[4]'),
                        17: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[5]'),
                        18: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[6]'),
                        19: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[7]'),
                        20: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[8]'),
                        21: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[9]'),
                        22: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[10]'),
                        23: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[11]'),
                        24: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[12]'),
                        25: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[1]'),
                        26: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[2]'),
                        27: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[3]'),
                        28: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[4]'),
                        29: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[5]'),
                        30: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[6]'),
                        31: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[7]'),
                        32: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[8]'),
                        33: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[9]'),
                        34: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[10]'),
                        35: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[11]'),
                        36: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[12]'),
                        37: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[1]'),
                        38: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[2]'),
                        39: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[3]'),
                        40: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[4]'),
                        41: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[5]'),
                        42: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[6]'),
                        43: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[7]'),
                        44: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[8]'),
                        45: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[9]'),
                        46: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[10]'),
                        47: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[11]'),
                        48: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[12]'),
                        49: driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div[13]')
                        }
        # Choose the number with the highest amount of losses
        print(max(bet_numbers_frequencies))

    else:
        pass
