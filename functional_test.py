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

# She is invited to enter a to-do item straight away
# She types "Buy peacock feathers" into a text box (Edith's hobby
# is tying fly-fishing lures)
# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list
# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly" (Edith is very methodical)
# The page updates again, and now shows both items on her list

# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.
# She visits that URL - her to-do list is still there.
# Satisfied, she goes back to sleep
browser.quit()
