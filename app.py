from time import sleep
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)
browser.implicitly_wait(5)

browser.get("http://www.instagram.com")
print(browser.title)

sleep(2)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("jazz_boot")
password_input.send_keys("bX$Zl4L23Qbg")

login_button = browser.find_element_by_xpath("//div[text()='Log In']")
login_button.click()

sleep(5)

browser.close()