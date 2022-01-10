from time import sleep
from selenium import webdriver
import secure_info
import random
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# direct the program to the correct webdriver location
PATH = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)


# open browser (default is Chrome), navigate to Instagram, input username and password, click "Log In"
def login():

    browser.implicitly_wait(3)
    browser.get("http://www.instagram.com")
    print(browser.title)

    # we sleep randomly throughout the program to emulate human interaction and evade bot detection 
    sleep(random.randint(2, 4))

    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    # input your name and password as string surrounded by quotes
    username_input.send_keys(secure_info.username2)
    password_input.send_keys(secure_info.password2)

    login_button = browser.find_element_by_xpath("//div[text()='Log In']")
    login_button.click()

    sleep(random.randint(4, 5))


# search function appends randomly selected hashtag (passed into function as "tag") to address and navigates to page
def search(tag):
    address = 'https://www.instagram.com/explore/tags/'
    browser.get(address + tag)
    sleep(random.randint(4, 5))
    # program locates most recent post with hashtag and clicks it
    browser.find_elements_by_class_name('_9AhH0')[10].click()
    sleep(random.randint(2, 4))


# likes the post if possible. If already liked, prints "Post already liked!"
def like():
    # Like post (click heart)
    heart_button = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')

    try:
        heart_button.click()
    except:
        NoSuchElementException
        print("Post already liked!")


# tries to comment a random silly comment on the post. If commenting is disabled, user of program gets alert.
def comment():
    
    # an array of silly comments from which we randomly choose one
    comments = ["Can't stop, won't stop!", "Yaaaaass!!", "Get in there!!", "It always seems impossible until it’s done!", "Enjoy every moment of the journey!", 
    "Get it!", "You’re on fire!", "That’s the way to do it!", "You're absolutely killing it!",]
    silly_comment = random.choice(comments)
    comment.silly_comment = silly_comment

    # program attempts to post comment. If commenting is disabled on post, program alerts user with message.
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
      

# this funciton logs all of the bot's commenting on the posts by recording the username of the account and the comment that was posted by the bot
# need to update to prepend to log instead of append, and also update caption to deal with non utf-8 encodable text
def writeLogToFile():

    username = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/span/a').text  
    IG_log = open('IG_log.txt', 'a')
    IG_log.write(('\n' + datetime.now().strftime("%Y/%m/%d %H:%M:%S ") + "@" + username + " comment: " + str(comment.silly_comment)))
    IG_log.close()


# if a user is not yet followed, bot begins following them
def follow():
    username = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/span/a').text
    caption = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/span').text
    follow_button = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button')
    
    # need to fix if else statement in follow criteria
    if follow_button.text == "Follow":
        try:
            if "jazz" in username or "#jazz" or "#music" in caption:
                follow_button.click()
                sleep(random.randint(1, 2))
            else:
                return print(username + " not jazzy enough to follow.")  
        except NoSuchElementException:
            return
    elif follow_button.text == "Following":
        return(print("already following " + username))


# we pass in the number of posts with which we want to interact as an integer and this function searches for a hashtag, then executes like, comment, and follow on recent 
# posts while keeping track of each interaction by logging it in IG_log.txt
def run_bot(num_of_interactions=int):

    # jazz-adjacent hashtags from which the program will randomly choose and search
    tags = ['jazz','bebop','hardbop', 'transcribe', 'bigband', 'jazzband', 'saxophone', 'jazzsax', 'charlieparker', 'dizzygillespie',
    'jazztrumpet', 'jazzdrums', 'jazztrombone', 'jazzorgan', 'jazzpiano', 'jazzbass', 'cooljazz', 'jazzmusic', 'transcription',]
    tag = random.choice(tags)
    
    # initiate like_count at 0 so we keep track of the number of posts interacted with
    like_count = 0
    
    login()
    search(tag)
    
    # contiue liking and commenting on posts and then following the user until the prescribed number (passed into run_bot function) is reached
    while like_count < num_of_interactions:
        like()
        comment()
        follow()
        like_count += 1
        # page right to next post with arrow
        browser.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div[2]/button').click()
        sleep(random.randint(1, 2))
        writeLogToFile()
    print("You've liked and commented on", like_count, "posts. All done!")
    # closes the browser at the end of the program
    browser.quit()


# the most important function call in the whole program. Also where we pass in how many accounts with which the bot will interact.
run_bot(5)


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx UNDER CONSTRUCTION xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# def getCaption():
#     try:
#         caption = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/span').text
#         getCaption.caption = caption
#     except UnicodeEncodeError:
#         caption = "This caption is not encoded with utf-8"
#         getCaption.caption = caption

# caption = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/span').text