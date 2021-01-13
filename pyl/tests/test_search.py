from build_print_list import print_list

def test_search(py):
    srch_str = input('Enter item to search for: ')
    py.visit('https://google.com')
    py.get("[name='q']").type(srch_str)
    py.get("[name='btnK']").submit()
    
    results = py.findx('//div[contains(@class, "yuRUbf")]')
    results_list = [['Name', 'URL']]
    for site in results:
        results_list.append([site.find('span').first().get_property('innerHTML'), site.find('a').first().get_property('href')])

    print_list(results_list)