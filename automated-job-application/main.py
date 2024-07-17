from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

ACCOUNT_EMAIL = "email@gmail.com"
ACCOUNT_PASSW = "PASSWORD"
PHONE_NUMBER = "YOUR PHONE NUMBER"

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_option)
driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer"
    "&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0"
)

time.sleep(2)
reject_button = driver.find_element(By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()


# Click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSW)
password_field.send_keys(Keys.ENTER)

input("Press Enter when you have solved the Captcha")

time.sleep(5)
apply = driver.find_element(By.CSS_SELECTOR, value=".jobs-a-apply button")
apply.click()

time.sleep(5)
phone_no = driver.find_element(By.CSS_SELECTOR, value="input[id*=phoneNumber]")
if phone_no.text == "":
    phone_no.send_keys(PHONE_NUMBER)

submit_btn= driver.find_element(by=By.CSS_SELECTOR, value="footer button")
submit_btn.click()
