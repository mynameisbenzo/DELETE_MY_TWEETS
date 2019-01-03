import selenium

from selenium import webdriver
import os, json, time
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "username.json"), "r") as f:
    info = json.loads(f.read())


driver = webdriver.Chrome()
driver.get("https://www.twitter.com/login")

un_input = driver.find_element_by_class_name("js-username-field")
pw_input = driver.find_element_by_class_name("js-password-field")

un_input.send_keys(info["un"])
pw_input.send_keys(info["pw"])

# gotta figure out how I'm gonna click fake/js elements
# a change

submit.click()

time.sleep(3)
driver.close()
