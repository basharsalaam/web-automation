from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
username = 'pulverine'
password = 'Abdulsalam1'

arbitrary_green_values = [0, 0, 0, 0, 0, 0]
arbitrary_red_values = [0, 0, 0, 0, 0, 0]
arbitrary_blue_values = [0, 0, 0, 0, 0, 0]

bet_numbers = []


last_draws_red = []
last_draws_blue = []
last_draws_green = []

def read_last_draws(file_path, values_array):
    try:
        with open(file_path, "r") as file:
            # Read each line and convert to numbers
            for line in file:
                try:
                    number = int(line.strip())  # Assuming numbers are floating-point
                    values_array.append(number)
                except ValueError:
                    pass

    except FileNotFoundError:
        print(f"File not found: {file_path}")


read_last_draws('values_blue.txt', last_draws_blue)
read_last_draws('values_red.txt', last_draws_red)
read_last_draws('values_green.txt', last_draws_green)


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

        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[4]/div[1]/div[5]/a').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div[4]/div[1]/div[5]/div/div[3]/div').click()
        time.sleep(2)

        green_values = []
        red_values = []
        blue_values = []

        for i in range(1, 7):
            green_values.append(int(driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[{i}]/td[4]').text))
        print(green_values)
        for i in range(7, 13):
            red_values.append(int(driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[{i}]/td[4]').text))
        print(red_values)
        for i in range(13, 19):
            blue_values.append(int(driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[{i}]/td[4]').text))
        print(blue_values)

        def update_last_draws(file_path, value_array):
            # Create a Python list with new lines of text

            try:
                with open(file_path, 'w') as file:
                    # Write each line from the list to the file
                    for line in value_array:
                        file.write(str(line) + '\n')

            except FileNotFoundError:
                print(f"File not found: {file_path}")

        for i in range(0, 6):
            if green_values[i] > last_draws_green[i]:
                last_draws_green[i] = green_values[i]

            if blue_values[i] > last_draws_blue[i]:
                last_draws_blue[i] = blue_values[i]

            if red_values[i] > last_draws_red[i]:
                last_draws_red[i] = red_values[i]

        update_last_draws('values_green.txt', last_draws_green)
        update_last_draws('values_red.txt', last_draws_red)
        update_last_draws('values_blue.txt', last_draws_blue)

        del green_values, blue_values, red_values





