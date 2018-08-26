#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 20:33:17 2018
Automation of Twitter Login
@author: rohit
"""
from selenium import webdriver
import hashlib
url = 'https://twitter.com/login'
username = str(input('Please enter username_or_email:\n'))
pwd = str(input('Please enter a Password:\n'))
#hashlib.sha256(pwd.encode('utf8')).hexdigest()
tweet = str(input('Please enter your tweet: '))
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input').send_keys(username)
print('Username Entered')
driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input').send_keys(pwd)
print('Password Entered')
driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button').click()
print('Button click')
driver.find_element_by_xpath('//*[@id="global-new-tweet-button"]/span').click()
print('Twitter Button Click')
driver.find_element_by_xpath('//*[@id="Tweetstorm-tweet-box-0"]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]').send_keys(tweet)
driver.find_element_by_xpath('//*[@id="Tweetstorm-tweet-box-0"]/div[2]/div[2]/div[2]/span/button[2]').click()