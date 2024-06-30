import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.divan.ru/"
driver.get(url)

time.sleep(3)

categories = driver.find_elements(By.CSS_SELECTOR, ".ui-GPFV8.mjE7U")

parsed_data = []

print(len(categories))

for category in categories:
    category_link = category.get_attribute("href")
    category_name = category.find_element(By.CSS_SELECTOR, "div.lylNH").text
    # print(category_link, category_name)

    driver.get(category_link)

    time.sleep(3)

    try:
        i = 1
        while True:
            page = f"{category_link}/page-{i}"
            print(page)
            driver.get(page)

            time.sleep(3)

            items = driver.find_elements(By.CLASS_NAME, "wYUX2")

            for item in items:
                item_name = item.find_element(By.CSS_SELECTOR, "a.span").text
                print(item_name)
                item_price = item.find_element(By.CSS_SELECTOR, "span.ui-LD-ZU.KIkOH").text
                print(item_price)
                item_link = item.find_element(By.CSS_SELECTOR, "a.ui-GPFV8").get_attribute("href")
                print(item_link)
            break

    except:
        continue



