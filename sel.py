from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

def scrape():
    srch_str = input('Enter desired item to search for: ')
    driver = webdriver.Chrome('C:/Users/lpang/Code/chromedriver_win32/chromedriver')
    driver.get('https://google.com')
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(srch_str)
    search_box.send_keys(Keys.RETURN)
    html = driver.page_source
    time.sleep(2)
    driver.quit()
    return BeautifulSoup(html, features='html.parser')
    
def build_list(soup):
    results = soup.find_all('div', class_='yuRUbf')
    results_list = [['Site', 'URL']]
    for item in results:
        x = item.find('a')
        results_list.append([x.find('span').get_text(), x.get('href')])
    return results_list
    
def print_list(lst):
    length_list = [len(element) for row in lst for element in row]
    column_width = max(length_list)
    for row in lst:
        row = ''.join(element.ljust(column_width + 2) for element in row)
        print(row)

if __name__ == '__main__':
    page_soup = scrape()
    results_lst = build_list(page_soup)
    print_list(results_lst)