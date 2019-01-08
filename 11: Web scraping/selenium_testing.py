from selenium import webdriver

browser = webdriver.Chrome()

try:
    browser.get('http://www.google.com')
    browser.find_element_by_name('q').send_keys('ירדן יפת')
    browser.find_element_by_name('btnK').submit()
    browser.find_elements_by_class_name('LC20lb')[1].click()
except Exception as err:
    print(err)

