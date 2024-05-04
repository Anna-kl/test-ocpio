# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import random
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from  datetime import datetime

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
ChromeDriverManager().install()
drive = uc.Chrome()
i = 0
result = []
dt = datetime.today()  # Get timezone naive now
seconds = dt.timestamp()

while i<10000:
    try:

        drive = uc.Chrome()
        drive.get('https://ocpio.ru')
        time.sleep(2)
        a = drive.find_element(By.CLASS_NAME, 'gb-st1')
        a.click()
        inputElement = drive.find_element(By.CLASS_NAME, 'input-text')
        inputElement.send_keys('9268341417')
        enter = drive.find_element(By.CLASS_NAME, 'button-text')
        enter.click()
        time.sleep(5)
        code = drive.find_element(By.CLASS_NAME, 'margin-bottom25')
        codes = code.find_elements(By.TAG_NAME, 'input')
        time.sleep(2)
        i+=1

        for c in codes:
            c.send_keys('1')
        time.sleep(1)
        button = drive.find_element(By.CLASS_NAME, 'margin-bottom40')
        time.sleep(1)
        button.click()


    except Exception as ex:
        print(ex.args)
        continue

df = pd.DataFrame(result)
df.plot(x="date", y=["count"])
plt.savefig("output_plot.png")
