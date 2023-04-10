from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import re

import pandas as pd 

with open('pwrd.txt') as f:
    pwrd = f.readline() # extracting password from txt file 
    
# Creating a webdriver instance to log into LinkedIn

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r'C:\path\to\chromedriver.exe',options=options)

# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")

# waiting for the page to load
time.sleep(5)

username = driver.find_element(By.ID, "username")
username.send_keys("duyap@uci.edu")
pword = driver.find_element(By.ID, "password")
pword.send_keys(pwrd)	
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Opening TKH's Profile
profile_url = "https://www.linkedin.com/school/theknowledgehouse/posts/?feedView=all"
driver.get(profile_url)  

# Scroll to the bottom 
start = time.time()
 
# will be used in the while loop
initialScroll = 0
finalScroll = 1000
 
while True:
    driver.execute_script(f"window.scrollTo({initialScroll}, {finalScroll})")
    # this command scrolls the window starting from
    # the pixel value stored in the initialScroll
    # variable to the pixel value stored at the
    # finalScroll variable
    initialScroll = finalScroll
    finalScroll += 1000
 
    # we will stop the script for 3 seconds so that
    # the data can load
    time.sleep(3)

    end = time.time()
 
    # We will scroll for 120 seconds.
    if round(end - start) > 120:
        break
    
# Extract data from the profile 
src = driver.page_source

# Beautiful soup instance 
soup = BeautifulSoup(src, 'lxml') 

likes = []
comments = []
reposts = []

# Find likes 
likes_bs4tags = soup.find_all("span", attrs = {"class" : "social-details-social-counts__social-proof-text"})
for tag in likes_bs4tags:
    strtag = str(tag)
    # accounts for commas in the number
    list_of_matches = re.findall('[,0-9]+', strtag)
    # converts the last element in the list to int, appends to list
    last_string = list_of_matches.pop()
    without_comma = last_string.replace(',','')
    likes_int = int(without_comma)
    likes.append(likes_int)

# Find comments 
comments_bs4tags = soup.find_all("li", attrs = {"class" : "social-details-social-counts__item social-details-social-counts__comments social-details-social-counts__item--with-social-proof"})
for tag in comments_bs4tags:
    strtag = str(tag)
    list_of_matches = re.findall('[,0-9]+', strtag)
    last_string = list_of_matches.pop()
    without_comma = last_string.replace(',','')
    comments_int = int(without_comma)
    comments.append(comments_int)
    
# Find reposts count 
reposts_bs4tags = soup.find_all("li", attrs = {"class" : "social-details-social-counts__item social-details-social-counts__item--with-social-proof"})
for tag in reposts_bs4tags:
    strtag = str(tag)
    list_of_matches = re.findall('[,0-9]+', strtag)
    last_string = list_of_matches.pop()
    without_comma = last_string.replace(',','')
    reposts_int = int(without_comma)
    reposts.append(reposts_int)
    
    
# convert into pandas DataFrame
likes_df = pd.DataFrame(likes, columns = ['Likes'])
comments_df = pd.DataFrame(comments, columns =['Comments'])
reposts_df = pd.DataFrame(reposts, columns = ['Reposts'])

# Should I combine this into one DF? 

likes_df.to_csv('data/linkedin_likes.csv')
comments_df.to_csv('data/linkedin_comments.csv')
reposts_df.to_csv('data/linkedin_reposts.csv')