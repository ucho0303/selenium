import time
import urllib.request
from selenium import webdriver
import os
import sys

def main():
    search_for = input('serch for: ')
    derectry_name = input('derectry name is: ')
    url = 'https://www.google.co.jp/imghp?hl=ja&tab=ri&ogbl'
    path = os.getcwd() + '/chromedriver'

    try:
        os.mkdir(derectry_name)
    except FileExistsError:
        print(f'{derectry_name} has already existed')
        s = input('Do you want to continue ? (y/N): ')
        if len(s) == 0 or s[0].lower() != 'y':
            print('stop!')
            time.sleep(2)
            sys.exit()

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(path,options=options)

    driver.get(url)

    search_box = driver.find_element_by_name('q')
    search_box.send_keys(search_for)
    search_box.submit()

    driver.maximize_window()
    height = driver.execute_script('return window.outerHeight;')
    driver.execute_script(f'window.scrollTo(0,{height});')

    time.sleep(10)

    images = driver.find_elements_by_class_name('rg_i')

    scroll = height
    for i, image in enumerate(images,1):
        if i % 10 == 0:
            scroll += height
            driver.execute_script(f'window.scrollTo(0,{scroll});')
        try:
            image_url = image.get_attribute('src')
            urllib.request.urlretrieve(image_url, f'{derectry_name}/image{i}.png')
            time.sleep(2)
        except:
            print(f'error on image{i}')
            continue
    driver.quit()

if __name__ == "__main__":
    main()