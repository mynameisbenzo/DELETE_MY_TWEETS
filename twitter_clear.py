import selenium

from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.twitter.com/login")

un_input = driver.find_element_by_class_name("js-username-field")
pw_input = driver.find_element_by_class_name("js-password-field")

print(un_input)
print(pw_input)
