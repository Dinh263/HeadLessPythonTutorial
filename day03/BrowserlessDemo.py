from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.headless = True
assert opt.headless
browser = Chrome(options=opt,executable_path="/Users/dinhnguyen/Documents/Driver/chromedriver")
browser.get("https://duckduckgo.com/")
txt_search = browser.find_element_by_id("search_form_input_homepage")
txt_search.send_keys("Real python")
txt_search.submit()
results = browser.find_elements_by_class_name('result')
print(results[0].text)
browser.close()
quit()
print("test done")

