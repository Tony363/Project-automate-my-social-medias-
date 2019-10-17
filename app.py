from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()
    
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')  
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        
    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + hashtag + '&src=typed_query')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            bot.find_element_by_css_selector('.css-1dbjc4n[data-testid="tweet"]').click()
            print(bot.current_url)
            



ed = TwitterBot('thefool363@gmail.com', 'y53637133!A')
ed.login()
ed.like_tweet('datascience')