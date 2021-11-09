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
        browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button').click()
        sleep(random.randint(3, 4))
        browser.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div[2]/button').click()
        sleep(random.randint(1, 2))
        # like_count += 1
    except:
        print('Error Occurred While Liking')
        sleep(5)
        return 

tags = ['jazz','bebop','hardbop','swing', 'transcribe', 'bigband', 'jazzband']

like_count = 0
begin = datetime.today()
tag = random.choice(tags)

login()
search(tag)

like()

while like_count < 15:
    like()

browser.quit()
end = datetime.today()