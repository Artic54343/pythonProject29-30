# Page Object (Model) Pattern
# https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/

#Разделение реализации теста и логики сайта
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os


# driver = webdriver.Chrome()
# driver.get('https://test.mensa.no/')
# WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', 'dumskaya_xpath.main_button_enter')))
# # driver.set_window_position(1900,300)
# driver.maximize_window()


class BasePage:
    path = f'{os.getcwd()}/drivers/chromedriver'
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)
    url = 'https://myshows.me/'

    def start(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
    def finish(self):
        self.driver.quit()

class MainPage(BasePage):
    xpath_serial = '//ul[contains(@class,"Header-nav")]/li/a[@href="/search/all/"]'
    xpath_movies = '/html/body/div/div/div/div/div[1]/div/div[1]/ul/li[2]/a'

    xpath_news = '/html/body/div/div/div/div/div[1]/div/div[1]/ul/li[3]/a'
    xpath_ratings = '/html/body/div/div/div/div/div[1]/div/div[1]/ul/li[4]/a'
    xpath_communities = '/html/body/div/div/div/div/div[1]/div/div[1]/ul/li[5]/a'


    def open_serials_page(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(('xpath', self.xpath_serial)))
        self.menu_serial_button = self.driver.find_element('xpath', self.xpath_serial)
        self.menu_serial_button.click()

    def open_movies_page(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(('xpath', self.xpath_movies)))
        self.menu_movies_button = self.driver.find_element('xpath', self.xpath_movies)
        self.menu_movies_button.click()


    def open_news_page(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(('xpath', self.xpath_news)))
        self.menu_news_button = self.driver.find_element('xpath', self.xpath_news)
        self.menu_news_button.click()

    def open_ratings_page(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(('xpath', self.xpath_ratings)))
        self.menu_ratings_button = self.driver.find_element('xpath', self.xpath_ratings)
        self.menu_ratings_button.click()

    def open_communities_page(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(('xpath', self.xpath_communities)))
        self.menu_communities_button = self.driver.find_element('xpath', self.xpath_communities)
        self.menu_communities_button.click()



class SerialPage(MainPage):
    pass