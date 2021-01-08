from bs4 import BeautifulSoup
from build_print_list import (build_list, print_list)

def test_search(py):
    srch_str = input('Enter desired item to search for: ')
    py.visit('https://google.com')
    py.get("[name='q']").type(srch_str)
    py.get("[name='btnK']").submit()
    html = py.findx('//*[@id="rso"]').first().get_property('innerHTML')

    page_soup = BeautifulSoup(html, features='html.parser')
    results_lst = build_list(page_soup)
    print_list(results_lst)