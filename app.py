from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

# def find(bot):
#     element = bot.find_element_by_class_name("g")
#     if element:
#         return element
#     else:
#         return False


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
            time.sleep(3)
            tweets = bot.find_elements_by_css_selector('div[data-testid="like"]')
            for tweet in tweets:
                bot.execute_script("arguments[0].click();", tweet)

        
        # for tweet in tweets:
        #     tweet.click()
        #     print(tweet)
        # for button in like_button:
        #     print(button)
        #     button.click()
            

         
            # print(bot.current_url())
            



ed = TwitterBot('thefool363@gmail.com', 'y53637133!A')
ed.login()
ed.like_tweet('datascience')