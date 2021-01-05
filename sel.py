from selenium import webdriver
import time

if __name__ == '__main__':
    driver = webdriver.Chrome('C:/Users/lpang/Code/chromedriver_win32/chromedriver')
    driver.get('https://google.com')
    time.sleep(4)
    driver.quit()