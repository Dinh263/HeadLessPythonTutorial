from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/Users/dinhnguyen/Documents/Driver/chromedriver")
driver.maximize_window()
driver.get("http://facebook.com")
driver.find_element_by_name("email").send_keys("xxxx@gmail.com")
driver.find_element_by_name("pass").send_keys("xxxx")
driver.find_element_by_xpath("//label[@id='loginbutton']/input").click()
print("Test done")
driver.quit()