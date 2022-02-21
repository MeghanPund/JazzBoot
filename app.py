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


def login():
    '''Open browser (default is Chrome), navigate to Instagram, input username and password, click "Log In"'''
    browser.implicitly_wait(3)
    browser.get("http://www.instagram.com")
    print(browser.title)

    # we sleep randomly throughout the program to emulate human interaction and evade bot detection
    sleep(random.randint(2, 4))

    username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")

    # input your name and password into the parenthesis as string surrounded by quotes
    username_input.send_keys(secure_info.username)
    password_input.send_keys(secure_info.password)

    login_button = browser.find_element(By.XPATH, "//div[text()='Log In']")
    login_button.click()

    sleep(random.randint(4, 5))


def search(tag):
    '''Appends randomly selected hashtag (passed into function as "tag" argument) to address and navigates to page'''
    address = 'https://www.instagram.com/explore/tags/'
    browser.get(address + tag)
    sleep(random.randint(4, 5))
    # program locates most recent post with hashtag and clicks it
    browser.find_elements(By.CLASS_NAME, '_9AhH0')[10].click()
    sleep(random.randint(2, 4))


def like():
    '''Likes the post if possible. If already liked, prints "Post already liked!"'''
    # Like post (click heart)
    heart_button = browser.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")

    try:
        heart_button.click()
    except NoSuchElementException:
        print("Post already liked!")


def comment():
    '''Tries to comment a random silly comment on the post. If commenting is disabled, user of program gets alert.'''
    # an array of silly comments from which we randomly choose one
    comments = ["Can't stop, won't stop!", "Yaaaaass!!", "Get in there!!",
                "Get it!", "You're on fire!", "That's the way to do it!", "You're absolutely killing it!", ]
    silly_comment = random.choice(comments)
    comment.silly_comment = silly_comment

    # program attempts to post comment. If commenting is disabled on post, program alerts user with message.
    try:
        text_box = browser.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form')
        text_box.click()
        browser.find_element(By.XPATH, '//*[@aria-label="Add a comment…"]').send_keys(silly_comment)
        sleep(random.randint(1, 2))
        comment_button = browser.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button')
        comment_button.click()
        sleep(random.randint(3, 4))
    except NoSuchElementException:
        print('User has disabled comments on this post.')


# need to update to prepend to log instead of append, and also update caption to deal with non utf-8 encodable text
def writeLogToFile():
    '''
    Logs all of the bot's commenting on the posts by
    recording the username of the account and the comment that was posted by the bot
    '''
    # username = browser.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/span/a').text
    # username xpath needs updating after IG update
    with open('IG_log.txt', 'a') as IG_log:
        IG_log.write(f'\n{datetime.now().strftime("%Y/%m/%d %H:%M:%S ")}@ comment: {str(comment.silly_comment)}')


def follow():
    '''If a user is not yet followed, bot begins following them'''
    username = browser.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/h2/div/span/a').text
    caption = browser.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/span').text
    follow_button = browser.find_element(By.LINK_TEXT, 'Follow')
    unfollow_button = browser.find_element(By.LINK_TEXT, 'Unfollow')

    # need to fix if else statement in follow criteria
    if follow_button:
        try:
            if "jazz" in username or "#jazz" or "#music" in caption:
                follow_button.click()
                sleep(random.randint(1, 2))
            else:
                return print(username + " not jazzy enough to follow.")
        except NoSuchElementException:
            return
    elif unfollow_button:
        return(print("already following " + username))


def run_bot(num_of_interactions=int):
    '''
    We pass in the number of posts with which we want to interact as an integer
    and this function searches for a hashtag, then executes like, comment, and follow
    on recent posts while keeping track of each interaction by logging it in IG_log.txt
    '''
    # jazz-adjacent hashtags from which the program will randomly choose and search
    tags = ['jazz', 'bebop', 'hardbop', 'transcribe', 'bigband', 'jazzband', 'saxophone', 'jazzsax', 'charlieparker', 'dizzygillespie',
            'jazztrumpet', 'jazzdrums', 'jazztrombone', 'jazzorgan', 'jazzpiano', 'jazzbass', 'cooljazz', 'jazzmusic', 'transcription', ]
    tag = random.choice(tags)

    # initiate like_count at 0 so we keep track of the number of posts interacted with
    like_count = 0

    login()
    search(tag)

    # contiue liking and commenting on posts and then following the user until the prescribed number (passed into run_bot function) is reached
    while like_count < num_of_interactions:
        like()
        comment()
        # follow() is currently broken (IG made an update that broke it)
        like_count += 1
        # page right to next post with arrow
        browser.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div[2]/button').click()
        sleep(random.randint(1, 2))
        writeLogToFile()
    print("You've liked and commented on", like_count, "posts. All done!")
    # closes the browser at the end of the program
    browser.quit()


# the most important function call in the whole program. Also where we pass in how many accounts with which the bot will interact.
run_bot(5)
