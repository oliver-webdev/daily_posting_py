import sys
from random import random

from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException


# 자동 로그인 진행 함수
def login(driver):
    id_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    id_input.send_keys('boredchallenger')
    password_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    password_input.send_keys('todwhs$8450')
    password_input.submit()
    time.sleep(3)


# 자동화 작업 진행 함수
def work(driver):
    hash_tag = '홈트'
    while True:
        # 인스타그램 태그 검색 페이지로 이동
        driver.get("https://www.instagram.com/explore/tags/" + hash_tag)
        time.sleep(5)
        element = driver.find_elements_by_class_name("_9AhH0")[9]
        element.click()
        print('게시물 클릭')
        time.sleep(5)
        # 좋아요 클릭
        driver.find_elements_by_class_name("wpO6b ")[1].click()
        print('좋아요 클릭')


def main():
    driver = webdriver.Chrome(r'chromedriver.exe')
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')  # 로그인 페이지로 이동
    time.sleep(2.5)
    login(driver)
    time.sleep(3)
    work(driver)


main()
