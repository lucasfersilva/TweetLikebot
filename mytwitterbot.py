from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time 


class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password 
        self.bot = webdriver.Firefox()
        
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(6)
        email= bot.find_element_by_class_name('e-mail-input')
        password = bot.find_element_by_name("session[password]")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)



ed = TwitterBot("EMAIL","password")
ed.login