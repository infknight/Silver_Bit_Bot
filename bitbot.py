from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

password = input("Enter Password for FUT WebApp: \n")
# adding to my default browser


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/Users/jasonjia/Library/ApplicationSupport/Google/Chrome")


# start of the file
driver = webdriver.Chrome(executable_path='/Users/jasonjia/Documents/personal_project/Silver_Bit_Bot/chromedriver', chrome_options=options)
driver.get("https://www.ea.com/fifa/ultimate-team/web-app/")
# wait for EA to load
time.sleep(10)

# find the login button
login_button_class = "btn-standard.call-to-action"
elem = driver.find_element_by_class_name(login_button_class)
if(elem!=None):
    elem = driver.find_element_by_class_name(login_button_class)
    elem.click()

time.sleep(5)

user_name = "zixuan.jia0616@gmail.com"
em_elem = driver.find_element_by_id("email")
if(em_elem != None):
    print("find it")
    input_un = driver.find_element_by_id("email")
    input_pd = driver.find_element_by_id("password")
    input_un.send_keys(user_name)
    input_pd.send_keys(password)

    # login button
    sec_login = driver.find_element_by_id("btnLogin")
    sec_login.click()


def silver_bit(driver):
    transfer = driver.find_element_by_class("ut-tab-bar-item.icon-transfer")
    transfer.click()

# silver_bit(driver)


# driver.close()



