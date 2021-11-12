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

    username_input.send_keys(secure_info.username2)
    password_input.send_keys(secure_info.password2)

    login_button = browser.find_element_by_xpath("//div[text()='Log In']")
    login_button.click()

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
        # Like post (click heart)
        browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button').click()
        sleep(random.randint(3, 4))
                
    except:
        print('Error Occurred While Liking')
        sleep(5)
        return 

def comment():
    comments = ["Can't stop, won't stop!",'Yaaaaass!!', 'Get in there!!', '🔥🔥🔥', ''] 
    comment = random.choice(comments)
    text_box = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
    browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]')
    text_box.click()
    sleep(random.randint(3, 4))
    browser.find_element_by_tag_name('textbox').send_keys(comment)
    browser.find_element_by_tag_name('textbox').send_keys(Keys.ENTER)
    sleep(random.randint(3, 4))
    comment_button = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button[2]')
    comment_button.click()
    sleep(random.randint(3, 4))

def run_bot(num_of_interactions=int):

    tags = ['jazz','bebop','hardbop','swing', 'transcribe', 'bigband', 'jazzband', 'saxophone', 'jazzsax']

    like_count = 0
    tag = random.choice(tags)

    login()
    search(tag)
    
    while like_count < num_of_interactions:
        like()
        # comment()
        # Page to the right with arrow
        browser.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div[2]/button').click()
        sleep(random.randint(1, 2))
        like_count += 1
    print("You've liked", like_count, "posts. All done!")
    browser.quit()

run_bot(3)

def follow():
    keywords = []
    keyword = random.choice(keywords)
    address = 'https://www.instagram.com/explore/people/'
    browser.get(address + keyword)
    sleep(random.randint(3, 4))
    browser.find_elements_by_class_name('_9AhH0')[10].click()
    sleep(random.randint(3, 4))