from os import close
from time import sleep
from selenium import webdriver
import selenium
import secure_info
import random
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

PATH = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)

def login():

    browser.implicitly_wait(3)
    browser.get("http://www.instagram.com")
    print(browser.title)

    sleep(2)

    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys(secure_info.username2)
    password_input.send_keys(secure_info.password2)

    login_button = browser.find_element_by_xpath("//div[text()='Log In']")
    login_button.click()

    sleep(2.5)

def search(tag):
    address = 'https://www.instagram.com/explore/tags/'
    browser.get(address + tag)
    sleep(random.randint(3, 4))
    browser.find_elements_by_class_name('_9AhH0')[10].click()
    sleep(random.randint(2, 4))

def like():
    # Like post (click heart)
    heart_button = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
    # heart_button_unclicked = browser.find_element_by_xpath('//*[@aria-label="Like"]')
    # heart_button_clicked = browser.find_element_by_xpath('//*[@aria-label="Unlike"]')
    heart_button.click()
    sleep(random.randint(1, 4))



def comment():
    
    comments = ["Can't stop, won't stop!", "Yaaaaass!!", "Get in there!!", "It always seems impossible until it’s done!", "Enjoy every moment of the journey!", 
    "Believe you can and you’re halfway there!", "You’re on fire!", "That’s the way to do it!", "You're absolutely killing it!"]
    silly_comment = random.choice(comments)
    comment.silly_comment = silly_comment

    # try except for disabled comments !! update this to not catch every error !!
    try:
        text_box = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
        text_box.click()
        browser.find_element_by_xpath('//*[@aria-label="Add a comment…"]').send_keys(silly_comment)
        sleep(random.randint(1, 2))
        comment_button = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button[2]')
        comment_button.click()
        sleep(random.randint(3, 4))
    except:
        NoSuchElementException
        print('User has disabled comments on this post.')  
      

# update line_prepender, and also update caption to deal with non utf-8 encodable text
def writeLogToFile():
    # def line_prepender(filename, line):
    #     with open(filename, 'r+') as IG_log:
    #         content = IG_log.read()
    #         IG_log.seek(0, 0)
    #         IG_log.write(line.rstrip('\r\n') + '\n' + content)
    #         IG_log.close()
    username = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/span/a').text
    
    # def getCaption():
    #     try:
    #         caption = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/span').text
    #         getCaption.caption = caption
    #     except UnicodeEncodeError:
    #         caption = "This caption is not encoded with utf-8"
    #         getCaption.caption = caption

    caption = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/span').text
    IG_log = open('IG_log.txt', 'a')
    IG_log.write(('\n' + datetime.now().strftime("%Y/%m/%d %H:%M:%S ") + "@" + username + " comment: " + str(comment.silly_comment)))
    IG_log.close()
    # username = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/span/a').getText()
    # line_prepender('IG_log.txt', (datetime.now().strftime("%Y/%m/%d, %H:%M:%S") + str(comment.silly_comment)))
    

def run_bot(num_of_interactions=int):

    tags = ['jazz','bebop','hardbop','swing', 'transcribe', 'bigband', 'jazzband', 'saxophone', 'jazzsax', 'charlieparker', 'dizzygillespie',
    'jazztrumpet', 'jazzdrums',]
    tag = random.choice(tags)
    
    like_count = 0
    
    login()
    search(tag)
    
    while like_count < num_of_interactions:
        like()
        comment()
        like_count += 1
        # page right to next post with arrow
        browser.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div[2]/button').click()
        sleep(random.randint(1, 2))
        writeLogToFile()
    print("You've liked and commented on", like_count, "posts. All done!")
    browser.quit()

run_bot(5)


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx UNDER CONSTRUCTION xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def follow():
    keywords = ['jazz', 'bebop']
    keyword = random.choice(keywords)
    address = 'https://www.instagram.com/explore/search/keyword/?q=jazz'
    browser.get(address)
    sleep(random.randint(2, 4))
    # open first post
    browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/div/div[1]/div[2]/div/a/div/div[2]').click()
    sleep(random.randint(2, 4))
    username = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/span/a').text
    caption = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/span').text
    follow_button = browser.find_element_by_xpath('//*[@aria-label="Follow"]')
    already_followed = browser.find_element_by_xpath('//*[@aria-label="Following"]')
    
    if "jazz" in username:
        follow_button.click()
    elif "#jazz" in caption:
        follow_button.click()