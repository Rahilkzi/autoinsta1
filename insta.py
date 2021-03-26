from selenium import webdriver
import schedule
import time
import os

URL = "https://increasefollower.com/giriss"


def job():
    option = webdriver.ChromeOptions()
    option.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    option.add_argument('--headless')
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-dev-sh-usage")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=option)

    driver.get(URL)
    time.sleep(20)

    username = driver.find_element_by_id("username")
    time.sleep(30)

    username.send_keys("bookmysmoky")
    time.sleep(30)

    submit = driver.find_element_by_id("gonder")
    submit.click()
    time.sleep(30)

    password = driver.find_element_by_id("password")
    password.send_keys("bookmyshow")
    time.sleep(30)
    submit = driver.find_element_by_id("gonder")
    submit.click()
    time.sleep(30)

    sendF = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[1]/div/div[2]/a/div/button")
    sendF.click()
    time.sleep(30)

    username = driver.find_element_by_id("username")
    time.sleep(10)
    username.send_keys("rahil_kzi")
    time.sleep(30)

    submit = driver.find_element_by_id("gonder")
    submit.click()
    time.sleep(30)

    no = driver.find_element_by_id("adet")
    no.send_keys('30')
    time.sleep(30)

    submit = driver.find_element_by_id("gonder")
    submit.click()
    time.sleep(10)

    driver.quit()


# schedule.every().day.at("10:30").do(job)
schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
