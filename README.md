# Jazz Bot
## Program Description
A foray into browser automation, featuring selenium.

## Note
If you intend to clone this and run it with your own account:
1) you will need to find 
```
    username_input.send_keys(secure_info.username) 
    password_input.send_keys(secure_info.password)
```
and replace `secure_info.username` with your own username, as well as `secure_info.password` with your own password, as 'string'.
2) You will also need to install Google Chrome's chromedriver, or the webdriver for your browser of choice. After doing that, you'll need to reconfigure the PATH variable to the correct filepath.
3) Finally, pip install selenium.

## Functionality
As of 21 November 2021, this bot logs in, searches for a hashtag (randomly chosen from a list), and comments, likes, & subscribes to a set number of posts/accounts (the parameter passed to the runbot() function) with that hashtag. After this, the bot writes a log in a text file that shows the date/timestamps and the comments posted (and to which accounts).

## Future Functionality
1. Refine criteria for interaction with accounts
2. Streamline the code so it is more efficient and can run faster (research Instagram's automation detection)
3. Update log.write to include post's caption - FIX FOR NON-UTF8 ENCODABLE TEXT - AND to prepend to the file instead of append.
4. (More intense) Use sentiment analysis to more accurately comment on posts
5. (More intense) Use a translation API to determine the language of a post, read the caption, and translate the comment posted to the correct language.
