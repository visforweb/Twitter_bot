from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import os
URL = "https://bhagavadgita.io/verse-of-the-day/"
USER_ID = "vishalkumar.mit@gmail.com"
USER_NAME ="VishalTheDarer"
USER_PASSWORD = "PASSWORD"
TWITTER_URL = "https://twitter.com/i/flow/login"
chromium_driver_path = "C:\Development\chromedriver.exe"
service = Service(chromium_driver_path)


class Scaper():
    """reads and scrapes datas from a live website"""
    def __init__(self, url):
        self.webpage = requests.get(url).text
        self.soup = BeautifulSoup(self.webpage, "html.parser")


    def scrape_data(self):
        """returns shloka scraped from live webpage"""
        bhagwat_sloka = self.soup.find(name="p", class_="verse-sanskrit").text
        shloka_meaning = self.soup.find(name="p", class_="verse-meaning").text
        final_text = f"The Geeta Shloka of the Day is:\n{bhagwat_sloka}\nIts meaning is:\n{shloka_meaning}"
        return final_text


# scrp.scrape_data()
# print(scrp.scrape_data())

class AutoTwit:
    """logins into twitter and twits """
    def __init__(self, scraped_message: Scaper):
        self.driver = webdriver.Chrome(service=service)
        self.sloka = scraped_message


    def login(self,login_url):
        self.driver.maximize_window()
        self.driver.get(login_url)
        self.wait = WebDriverWait(self.driver, 30)
        userid_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="text"]')))
        userid_input.send_keys(USER_ID)
        userid_input.send_keys(Keys.ENTER)
        try:
            username_input = self.wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                          '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')))
            username_input.send_keys(USER_NAME)
            username_input.send_keys(Keys.ENTER)
        except:
            user_password_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            user_password_input.send_keys(USER_PASSWORD)
            user_password_input.send_keys(Keys.ENTER)
    def tweet(self):
        self.sloka = scrp.scrape_data()
        tweet_message = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Tweet text"]')))
        tweet_message.send_keys(f"#DailyBhagwatgitaSloka\n{self.sloka}")
        tweet_button = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-testid="tweetButtonInline"]')))
        tweet_button.click()


scrp =Scaper(URL)
do_tweet = AutoTwit(scrp)
do_tweet.login(TWITTER_URL)
do_tweet.tweet()
