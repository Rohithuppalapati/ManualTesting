# link for more info on selenium webdriver http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/

from selenium import webdriver

chrome_browser=webdriver.Chrome()

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
chrome_browser.maximize_window()

print('Selenium Easy' in chrome_browser.title)

assert 'Show Message'in chrome_browser.page_source

show_button = chrome_browser.find_element_by_class_name('btn-default')
#print(show_button.get_attribute('innerHTML'))


user_message=chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('hello prnds my name is rohith')

show_button.click()

