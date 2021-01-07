def test_search(py):
    srch_str = input('Enter desired item to search for: ')
    py.visit('https://google.com')
    py.get("[name='q']").type(srch_str)
    py.get("[name='btnK']").submit()