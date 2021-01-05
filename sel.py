from selenium import webdriver
import time

if __name__ == '__main__':
    srch_str = input('Enter desired item to search for: ')
    driver = webdriver.Chrome('C:/Users/lpang/Code/chromedriver_win32/chromedriver')
    driver.get('https://google.com/search?q={}'.format(srch_str))
    time.sleep(4)
    driver.quit()