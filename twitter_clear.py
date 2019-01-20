import selenium

from selenium import webdriver
from selenium.webdriver.common import  keys
from selenium.webdriver import ActionChains
import os, json, time
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "username.json"), "r") as f:
    info = json.loads(f.read())


driver = webdriver.Chrome()
ac = ActionChains(driver)
driver.get("https://www.twitter.com/login")

un_input = driver.find_element_by_class_name("js-username-field")
pw_input = driver.find_element_by_class_name("js-password-field")

un_input.send_keys(info["un"])
pw_input.send_keys(info["pw"])
pw_input.send_keys(keys.Keys.ENTER)
# gotta figure out how I'm gonna click fake/js elements
# a change

driver.get("https://www.twitter.com/" + info["un"])
time.sleep(0.5)
i, tweet_amt = -1, 0
while i < tweet_amt:
    if i == -1:
        i = 0
    dropdowns = driver.find_elements_by_class_name("dropdown-toggle")
    if tweet_amt == 0:
        tweet_amt = len(dropdowns)
    print(tweet_amt, i, dropdowns[i])
    try:
        dropdowns[i].click()
    except:
        i += 1
        continue

    delete = driver.find_elements_by_css_selector("li.js-actionDelete > button.dropdown-link")
    try:
        print("oof")
        delete[i].click()
        delete_btns = driver.find_elements_by_css_selector("button.delete-action")
        delete_btns[0].click()

    except:
        dropdowns[i].click()
        print("bing")
        i += 1

driver.close()
