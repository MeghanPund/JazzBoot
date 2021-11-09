from time import sleep
from selenium import webdriver
import secure_info
import random
from datetime import datetime
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)

def login():

    browser.implicitly_wait(5)
    browser.get("http://www.instagram.com")
    print(browser.title)

    sleep(2)

    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys(secure_info.username)
    password_input.send_keys(secure_info.password)

    login_button = browser.find_element_by_xpath("//div[text()='Log In']")
    login_button.click()

    sleep(3)

    not_now_button = browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
    not_now_button.click()
    sleep(3)

def search(tag):
    address = 'https://www.instagram.com/explore/tags/'
    browser.get(address + tag)
    sleep(random.randint(3, 4))
    browser.find_elements_by_class_name('_9AhH0')[10].click()
    sleep(random.randint(3, 4))

def like():
    global like_count
    try:
        browser.find_element_by_class_name('wpO6b  ').click()
        sleep(random.randint(3, 4))
        browser.find_element_by_class_name('_8-yf5').click()
        sleep(random.randint(1, 2))
        like_count += 1
    except:
        print('Error Occurred While Liking')
        sleep(5)
        return 

login()

tags = ['jazz','bebop','hardbop','swing', 'transcribe', 'bigband']

like_count = 0
begin = datetime.datetime.today()
tag = random.choice(tags)

search(tag)

while like_count < 15:
    like()

browser.quit()
end = datetime.datetime.today()