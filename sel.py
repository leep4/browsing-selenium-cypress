from selenium import webdriver
import time
from bs4 import BeautifulSoup

def scrape():
    srch_str = input('Enter desired item to search for: ')
    driver = webdriver.Chrome('C:/Users/lpang/Code/chromedriver_win32/chromedriver')
    driver.get('https://google.com/search?q={}'.format(srch_str))
    html = driver.page_source
    driver.quit()
    return BeautifulSoup(html, features='html.parser')

if __name__ == '__main__':
    page_soup = scrape()
    results = page_soup.find_all('div', class_='yuRUbf')
    link = results[1].find('a').get('href')
    title = results[1].find('a').find('span').get_text()
    print(link)
    print(title)