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