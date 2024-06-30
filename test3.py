import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import pprint

driver = webdriver.Chrome()
url = "https://tomsk.hh.ru/vacancies/programmist"
driver.get(url)

time.sleep(3)

# vacancies = driver.find_elements(By.CLASS_NAME, "vacancy-card--H8LvOiOGPll0jZvYpxIF")

vacancies = driver.find_elements(By.CLASS_NAME, "vacancy-card--z_UXteNo7bRGzxWVcL7y")
# pprint.pprint(vacancies)

parsed_data = []


# Перебираем коллекцию вакансий
# Используем конструкцию try-except, чтобы "ловить" ошибки, как только они появляются
for vacancy in vacancies:
    # pprint.pprint(vacancy)
    try:
        # Находим элементы внутри вакансий по значению
        # Находим названия вакансии
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--c1Lay3KouCl7XasYakLk').text
        print(title)
        # Находим названия компаний
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--vgvZouLtf8jwBmaD1xgp').text
        print(company)
        # Находим зарплаты
        try:
            salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-text--kTJ0_rp54B2vNeZ3CTt2').text
        except:
            salary = "не указана"
        print(salary)
        # Находим ссылку с помощью атрибута 'href'
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
        print(link)
        # Вносим найденную информацию в список
        parsed_data.append([title, company, salary, link])

    except:
        # Вставляем блок except на случай ошибки - в случае ошибки программа попытается продолжать
        print("произошла ошибка при парсинге")
        continue


# pprint.pprint(parsed_data)
# print(len(parsed_data))

# Закрываем подключение браузер
driver.quit()

with open("hh.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Название вакансии", "Название компании", "Зарплата", "Ссылка на вакансию"])
    for row in parsed_data:
        writer.writerow(row)
