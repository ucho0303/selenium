from selenium import webdriver
import os

def main():
    path = os.getcwd() + '/chromedriver'

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(path,options=options)

    driver.get('https://qiita.com/tags/python?page=1')
    driver.maximize_window()

    trend_tag = driver.find_element_by_class_name('p-tagShow_mainMiddle')
    trends = trend_tag.find_elements_by_class_name('tst-ArticleBody_title')
    for trend in trends:
        print(trend.text)
        print(trend.get_attribute('href'))

    driver.quit()

if __name__ == "__main__":
    main()