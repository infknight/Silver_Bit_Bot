from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

password = input("Enter Password for FUT WebApp: \n")

# start of the file
driver = webdriver.Chrome(executable_path='/Users/jasonjia/Documents/personal_project/Silver_Bit_Bot/chromedriver')
driver.get("https://www.ea.com/fifa/ultimate-team/web-app/")
# wait for EA to load
time.sleep(10)

# find the login button
login_button_class = "btn-standard.call-to-action"
elem = driver.find_element_by_class_name(login_button_class)
elem.click()

time.sleep(5)

user_name = "zixuan.jia0616@gmail.com"

input_un = driver.find_element_by_id("email")
input_pd = driver.find_element_by_id("password")
input_un.send_keys(user_name)
input_pd.send_keys(password)






