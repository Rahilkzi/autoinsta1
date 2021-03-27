from selenium import webdriver
import schedule
import time
import os

URL = "https://increasefollower.com/giriss"

option = webdriver.ChromeOptions()
option.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
option.add_argument('--headless')
option.add_argument("--no-sandbox")
option.add_argument("--disable-dev-sh-usage")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=option)

driver.get(URL)
time.sleep(20)

username = driver.find_element_by_id("username")
time.sleep(5)
username.send_keys("booksmok")
time.sleep(10)
submit = driver.find_element_by_id("gonder")
submit.click()
time.sleep(30)

password = driver.find_element_by_id("password")
time.sleep(5)
password.send_keys("book01")
time.sleep(5)
submit = driver.find_element_by_id("gonder")
submit.click()
time.sleep(30)

sendF = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[1]/div/div[2]/a/div/button")
time.sleep(5)
sendF.click()
time.sleep(30)


def job():
    user = driver.find_element_by_id("username")
    time.sleep(5)
    user.send_keys("rahil_kzi")
    time.sleep(10)
    submit_user = driver.find_element_by_id("gonder")
    submit_user.click()
    time.sleep(30)

    amount = driver.find_element_by_id("adet")
    time.sleep(5)
    amount.send_keys('30')
    time.sleep(10)
    submit_amount = driver.find_element_by_id("gonder")
    submit_amount.click()
    time.sleep(10)


def refresh():
    driver.refresh()


schedule.every(5).seconds.do(refresh)  # for refresh


schedule.every(3).hours.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
