from selenium import webdriver
import schedule
import time

URL = "https://increasefollower.com/giriss"


def job():
    GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
    # CHROMEDRIVER_PATH = r'/app/.chromedriver/bin/chromedriver'
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.binary_location = GOOGLE_CHROME_PATH
    driver = webdriver.Chrome(r'/app/.chromedriver/bin/chromedriver', options=option)
    # driver = webdriver.Chrome('chromedriver', options=option)

    driver.get(URL)

    username = driver.find_element_by_id("username")

    username.send_keys("bookmysmoky")
    time.sleep(1)

    submit = driver.find_element_by_id("gonder")
    submit.click()
    time.sleep(5)

    password = driver.find_element_by_id("password")
    password.send_keys("bookmyshow")
    submit = driver.find_element_by_id("gonder")
    submit.click()
    time.sleep(10)

    sendF = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[1]/div/div[2]/a/div/button")
    sendF.click()
    time.sleep(5)

    username = driver.find_element_by_id("username")
    time.sleep(2)
    username.send_keys("rahil_kzi")
    time.sleep(4)

    submit = driver.find_element_by_id("gonder")
    submit.click()
    time.sleep(5)

    no = driver.find_element_by_id("adet")
    no.send_keys('30')
    time.sleep(2)

    submit = driver.find_element_by_id("gonder")
    submit.click()

    driver.quit()


# schedule.every().day.at("10:30").do(job)
schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
