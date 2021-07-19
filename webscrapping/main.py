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


def get_cards():
    return find_element(CARD_XPATH)


def find_element(xpath):
    return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))


def get_image_link(xpath):
    return find_element(xpath).get_attribute('src')


def scroll_to_bottom():
    # document.documentElement.scrollHeight
    # document.documentElement.scrollTop + document.documentElement.clientHeight
    def check_if_bottom():
        return driver.execute_script('document.documentElement.scrollTop + document.documentElement.clientHeight')

    SCROLL_PAUSE_TIME = 2  # wait 2 seconds
    while True:
        # Scroll down by 300px
        driver.execute_script("window.scrollBy(0, 300);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        if check_if_bottom:
            break


def fill_input(value, xpath):
    element = find_element(xpath)
    element.clear()
    element.send_keys(value)
    return element


def get_text_tag(xpath):
    return find_element(xpath).text


def click_button(xpath):
    element = find_element(xpath)
    element.click()
    return element


def navigate_to(full_path="", query=""):
    if(query == ""):
        driver.get(full_path)
    else:
        driver.get("{}{}/".format(URL, query))


def scrap_profile_posts(profile):
    navigate_to(query=profile)
    links = scroll_to_bottom()
    return links


def remove_front_indicators(text):
    return text[1:].strip()


def wait_out(min_time=0.25, max_time=1.25):
    wait_out_tome: float = min_time + random.random()
    time.sleep(wait_out_tome) if wait_out_tome < max_time else time.sleep(
        max_time)


def parse_text_arr(arr):
    return [i for i in [remove_front_indicators(instruction) for instruction in arr] if i != ""]


def login_routine():

    CREDENTIALS = {
        'username': 'patricktrudel48',
        'password': 'V:25VLMQkMQmJJf'
    }

    XPATH = {
        'input_username': '//*[@id="loginForm"]/div/div[1]/div/label/input',
        'input_password': '//*[@id="loginForm"]/div/div[2]/div/label/input',
        'button_connection': '//*[@id="loginForm"]/div/div[3]/button',
        'button_not_now': '//*[@id="react-root"]/section/main/div/div/div/div/button',
        'button_notifications': '/html/body/div[4]/div/div/div/div[3]/button[2]'
    }

    fill_input(CREDENTIALS['username'], XPATH['input_username'])
    fill_input(CREDENTIALS['password'], XPATH['input_password'])
    click_button(XPATH['button_connection'])
    click_button(XPATH['button_not_now'])
    click_button(XPATH['button_notifications'])


if __name__ == "__main__":
    scroll_to_bottom()
    print(len(get_cards()))
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
