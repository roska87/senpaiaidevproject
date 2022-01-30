import os
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


subreddit = input('Enter subreddit name: ')
save_dir = input('Enter name of folder to save images in: ')

if not os.path.isdir(save_dir):
    os.makedirs(save_dir)

pages = 1000
img_n = 511
browser = webdriver.Chrome(executable_path='./chromedriver')
browser.get('https://old.reddit.com/r/{}'.format(subreddit))

saved_images = 0

for i in range(pages):
    print("Step 0")
    icons = WebDriverWait(browser, 300).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "expando-button")
        )
    )
    print("Step 1")
    try:
        for icon in icons:
            icon.click()
    except:
        browser.execute_script("window.history.go(-1)")
    print("Step 2")
    links = WebDriverWait(browser, 1000).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "may-blank"))
    )
    print("Step 3")
    links = list(set([a.get_attribute('href') for a in links if a.get_attribute('href').endswith('.jpg')]))
    print("Step 4")
    for link in links:
        image = requests.get(link)
        with open('{}/img_{}.jpg'.format(save_dir, img_n), 'wb') as f:
            f.write(image.content)
        img_n += 1
    print("Step 5")
    if i != pages - 1:
        next_button = WebDriverWait(browser, 1000).until(
            EC.presence_of_element_located((By.CLASS_NAME, "next-button"))
        )
        next_button.click()
    print("Step 6")
    saved_images += len(links)
    print('page: {}, images: {}, total: {}'.format(i, len(links), saved_images))
