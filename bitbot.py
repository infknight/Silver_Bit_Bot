from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/Users/jasonjia/Documents/personal_project/Silver_Bit_Bot/chromedriver')
driver.get("https://www.ea.com/fifa/ultimate-team/web-app/")
time.sleep(10)

login_button_class = "btn-standard call-to-action"
elem = driver.find_element_by_class_name("")