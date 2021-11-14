# Jazz Bot
## Program Description
A foray into browser automation, featuring selenium. Created purely for my own amusement.

## Note
If you intend to clone this and run it with your own account, you will need to find 
```
    username_input.send_keys(secure_info.username) 
    password_input.send_keys(secure_info.password)
```
and replace `secure_info.username` with your own username, as well as `secure_info.password` with your own password, as 'string'.
You will also need to install Google Chrome's chromedriver, or the webdriver for your browser of choice. After doing that, you'll need to reconfigure the PATH variable to the correct filepath.

## Functionality
As of 14 November 2021, this bot logs in, searches for a hashtag (randomly chosen from a list), and comments and likes a set number of posts (the parameter passed to the runbot() function) with that hashtag.

## Future Functionality
1. Refine criteria for interaction with accounts
2. Streamline the code so it is more efficient and can run faster
3. Follow users who match the criteria
