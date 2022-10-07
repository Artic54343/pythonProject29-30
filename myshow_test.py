from Lesson36 import *
import pytest
import time

'''//h1[@class="title__main"]'''
a = '''Каталог сериалов'''
b = '''Каталог фильмов'''

f = '''Новости сериалов'''
c = '''Рейтинги и премии'''
x ='''Сообщество'''



def test_serial_positive():
    my = MainPage()
    # First
    my.start()
    my.open_serials_page()
    time.sleep(10)
    control = my.driver.find_element('xpath', '//h1[@class="title__main"]')
    result = control.text
    # my.finish()
    assert result == a

def test_movies_positive():
    my = MainPage()
    # First
    my.start()
    my.open_movies_page()
    time.sleep(10)
    control = my.driver.find_element('xpath', '//h1[@class="title__main"]')
    result = control.text
    # my.finish()
    assert result == b


def test_news_positive():
    my = MainPage()
    # First
    my.start()
    my.open_news_page()
    time.sleep(10)
    control = my.driver.find_element('xpath', '//h1[@class="title__main"]')
    result = control.text
    # my.finish()
    assert result == f

def test_ratings_positive():
    my = MainPage()
    # First
    my.start()
    my.open_ratings_page()
    time.sleep(10)
    control = my.driver.find_element('xpath', '//h1[@class="title__main"]')
    result = control.text
    # my.finish()
    assert result == c

def test_communities_positive():
    my = MainPage()
    # First
    my.start()
    my.open_communities_page()
    time.sleep(10)
    control = my.driver.find_element('xpath', '//h1[@class="title__main"]')
    result = control.text
    # my.finish()
    assert result == x