from selenium import webdriver
import os

def main():
    url = 'https://www.google.com/'
    path = os.getcwd() + '/chromedriver'

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(path,options=options)

    driver.get(url)
    driver.maximize_window()
    driver.execute_script('document.body.style.overflow = "hidden";')

    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()

    next_page = driver.find_element_by_id('pnnext')
    next_page.click()
    driver.save_screenshot('screenshot.png')

    driver.quit()

if __name__ == "__main__":
    main()