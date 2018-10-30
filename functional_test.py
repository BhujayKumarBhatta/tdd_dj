from selenium import webdriver
#driverLocation = "/mnt/c/mydev/tdd_dj/chromedriver"
#driverLocation = "/mnt/c/mydev/tdd_dj"
#driverLocation = "/mnt/c/mydev/tdd_dj"  , not required when driver is in path 
# the driver for firefox is here 
# https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux32.tar.gz
#https://github.com/SeleniumHQ/selenium/blob/master/py/docs/source/index.rst
#
browser = webdriver.Firefox()

# sumanta goes to check his new website
browser.get('http://localhost:8000')

# can see 'info ops' in the browser title
assert 'Django' in browser.title

