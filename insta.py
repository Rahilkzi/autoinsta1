from selenium import webdriver
import schedule
import time
import os

URL = "https://increasefollower.com/giriss"

print ("starting")


def job():
    print ("starting job")
    option = webdriver.ChromeOptions()
    option.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    option.add_argument('--headless')
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-dev-sh-usage")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=option)

    print ("Getting Url")
    driver.get(URL)
    time.sleep(15)
     

    print ("Trying To Login")
    print ("Typing Username")
    username = driver.find_element_by_id("username")
    time.sleep(5)
    username.send_keys("booksmok")
    time.sleep(10)
    
    print ("Submit Username")
    submit = driver.find_element_by_id("gonder")
    submit.click()
    time.sleep(20)
 
    print ("Typing Password")
    password = driver.find_element_by_id("password")
    password.send_keys("book10")
    time.sleep(10)

    print ("Submit Password")
    submit = driver.find_element_by_id("gonder")
    submit.click()
    time.sleep(20)

    
    print ("Going to send followers")
    sendF = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[1]/div/div[2]/a/div/button")
    sendF.click()
    time.sleep(20)
 
    print ("Typing Username for sending")
    username = driver.find_element_by_id("username")
    time.sleep(5)
    username.send_keys("rahil_kzi")
    time.sleep(15)
 
    print ("Submit send followers")
    submit = driver.find_element_by_id("gonder")
    submit.click()
    time.sleep(20)
    
    print ("How many follower")
    no = driver.find_element_by_id("adet")
    no.send_keys('30')
    time.sleep(15)

    print ("submit")
    submit = driver.find_element_by_id("gonder")
    submit.click()
    time.sleep(10)

    print ("done")
    time.sleep(2)

    driver.quit()


# schedule.every().day.at("10:30").do(job)
# schedule.every(5).seconds.do(job)
schedule.every(9).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
