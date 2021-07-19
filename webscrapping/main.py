from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import os
import wget
import time
import json
import random

driver = webdriver.Chrome(
    r"C:\Users\ptrud\Documents\chromedriver_win32\chromedriver.exe")
driver.get('https://signifly.com/team/')

URL = 'https://signifly.com/team/'
CARD_XPATH = '//div[contains(@class,"swiper-slide")]'

CARD_NAME = './/div[contains(@class,"name")]'
CARD_TITLE = './/div[contains(@class,"jobtitle")]'
CARD_IMAGE = './/div[contains(@class,"image")]/img[2]/@src'

def get_cards():
    return driver.find_elements_by_xpath(CARD_XPATH)


def find_element(xpath):
    return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))

def find_elements(xpath):
    return WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))

def click_button(id):
    element = find_element('//*[@id="__layout"]/div/div[1]/div/div[3]/div/div/div/div[{}]/div[3]/div/div/div/div/div[3]'.format(id))
    element.click()
    return element


def get_image_link(xpath):
    return find_element(xpath).get_attribute('src')

def parse_card(card):
    try:
        return {
            'name' : card.find_element_by_class_name("name").text,
            'title' : card.find_element_by_class_name("jobtitle").text,
            'image': card.find_element_by_class_name('img').get_attribute('src'),

        }
    except:
        return {}

def parse_cards(cards):
    kek = []
    for card in cards:
        kek.append(parse_card(card))
        time.sleep(0.1)
    return kek

def scroll_to_bottom():

    SCROLL_PAUSE_TIME = 0.25  # wait 1 seconds
    while True:
        # Scroll down by 300px
        driver.execute_script("window.scrollBy(0, 300);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        #check if at the bottom of the page
        if driver.execute_script('return document.documentElement.scrollTop + document.documentElement.clientHeight === document.documentElement.scrollHeight'):
            break


if __name__ == "__main__":
    scroll_to_bottom()
    for i in range(1, 9):
        for j in range(15):
            click_button(i)

    time.sleep(5)

    cards = get_cards()
    cards = parse_cards(cards)

    with open("team.json", "w") as outfile:
        json.dump(cards, outfile)
    driver.quit()

    # login_routine()
    # # scrap_profile_posts()

    # with open('myibsdiary_posts.json') as f:
    #     data = json.load(f)

    # posts = data['posts']
    # recipes = {
    #     'recipes': []
    # }
    # for post in posts:
    #     try:
    #         wait_out()
    #         navigate_to(post)
    #         text = get_text_tag(
    #             '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/div[1]/ul/div/li/div/div/div[2]/span')
    #         image = get_image_link(
    #             '//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/div/div/div[1]/div[1]/img')
    #         value_dict = {
    #             "title": None,
    #             "ingredients": None,
    #             "instructions": None,
    #             'image': image
    #         }

    #         value = text.split(':')

    #         value_dict['title'] = value[1].split('\n')[0].strip()
    #         value_dict['ingredients'] = parse_text_arr(value[2].split('\n'))
    #         value_dict['ingredients'] = value_dict['ingredients'][:len(
    #             value_dict['ingredients']) - 1]
    #         value_dict['instructions'] = parse_text_arr(
    #             value[3].split('#')[0].split('\n'))
    #         recipes['recipes'].append(value_dict)
    #     except:
    #         continue

    # with open("recipes.json", "w") as outfile:
    #     json.dump(recipes, outfile)

    # driver.quit()
