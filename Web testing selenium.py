import time

from selenium import webdriver

chrome_browser=webdriver.Chrome()

chrome_browser.get('https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjQ1MzYzMzk2LCJjYWxsc2l0ZV9pZCI6MjY5NTQ4NDUzMDcyMDk1MX0%3D')

chrome_browser.maximize_window()
print('facebook' in chrome_browser.title)

assert 'facebook' in chrome_browser.page_source

email_field=chrome_browser.find_element_by_id("email")
print(email_field)

password_field=chrome_browser.find_element_by_id('pass')
print(password_field)

login_button=chrome_browser.find_element_by_name('login')
print(login_button)

email_field.clear()
email_field.send_keys('rohithuppalapati77@gmail.com')
time.sleep(5)
password_field.clear()
password_field.send_keys('rohith1414')
time.sleep(5)
login_button.click()

print(login_button.get_attribute('innerHTML'))