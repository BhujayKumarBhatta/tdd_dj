from selenium import webdriver
#driverLocation = "/mnt/c/mydev/tdd_dj/chromedriver"
#driverLocation = "/mnt/c/mydev/tdd_dj"
browser = webdriver.Firefox()

# sumanta goes to check his new website
browser.get('http://localhost')

# can see 'info ops' in the browser title
assert 'django' in browser.title

