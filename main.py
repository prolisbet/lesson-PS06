import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


def is_404_page(driver):
    try:
        error_element = driver.find_element(By.CSS_SELECTOR, "h1.riN8D").text
        return "Страница не найдена" in error_element
    except NoSuchElementException:
        return False


driver = webdriver.Chrome()
url = "https://www.divan.ru/"
driver.get(url)

time.sleep(3)

categories = driver.find_elements(By.CSS_SELECTOR, ".ui-GPFV8.mjE7U")

parsed_data = []

for index in range(len(categories)):
    try:
        # Перезапрашиваем элементы категорий, чтобы избежать ошибки StaleElementReferenceException
        driver.get(url)
        categories = driver.find_elements(By.CSS_SELECTOR, ".ui-GPFV8.mjE7U")
        category = categories[index]

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

                if is_404_page(driver):
                    print(f"Страница {page} не найдена, переходим к следующей категории.")
                    break

                items = driver.find_elements(By.CLASS_NAME, "wYUX2")

                if not items:
                    break

                for item in items:
                    item_name = item.find_element(By.TAG_NAME, "span").text
                    # print(item_name)
                    item_price = item.find_element(By.CSS_SELECTOR, "span.ui-LD-ZU.KIkOH").text
                    # print(item_price)
                    item_link = item.find_element(
                        By.CSS_SELECTOR, "a.ui-GPFV8.qUioe.ProductName.ActiveProduct").get_attribute("href")
                    # print(item_link)

                    parsed_data.append([category_name, item_name, item_price, item_link])

                i += 1

        except NoSuchElementException:
            print(f"Не достает элементов в категории {category_name}")
            break

    except StaleElementReferenceException:
        print("Ошибка StaleElementReferenceException, перезапрашиваем элементы категорий...")

    except KeyboardInterrupt:
        print("Программа прервана пользователем")

# Закрываем подключение браузер
driver.quit()

with open("divan_ru_catalogue.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Категория товара", "Название товара", "Цена товара", "Ссылка на товар"])
    for row in parsed_data:
        writer.writerow(row)
