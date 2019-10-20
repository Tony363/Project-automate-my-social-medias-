from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()
    
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)
        email = bot.find_element_by_class_name("js-username-field")
        password = bot.find_element_by_class_name('js-password-field')
        
        email.clear()
        password.clear()
        
        time.sleep(3)
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
            like_button = bot.find_element_by_tag_name('g')
            like_button.click()
            # for button in like_button:
            #     print(button)
            #     button.click()
                

         
            # print(bot.current_url())
            



ed = TwitterBot('thefool363@gmail.com', 'y53637133!A')
ed.login()
ed.like_tweet('datascience')