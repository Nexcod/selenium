import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tabulate import tabulate

from utils import wait_for

browser = webdriver.Chrome()

# Открываем главную страницу google
browser.get('https://google.ru')

# Набираем в поиске Урфу и переходим по первой ссылке
search = browser.find_element_by_name('q')
search.send_keys('Урфу')
search.send_keys(Keys.ENTER)

search_list = browser.find_elements_by_tag_name('h3')
search_list[0].click()

# Меняем фокус на новую вкладку
browser.switch_to.window(browser.window_handles[1])

# Отрываем расписание занятий
wait_for(lambda: browser.find_element_by_link_text('Студентам')).click()
wait_for(lambda: browser.find_element_by_link_text('Расписание занятий')).click()

# Вводим название группы в поле поиска
search = wait_for(lambda: browser.find_element_by_name('group_number'))
search.send_keys('РИВ-470027у')

# Парсинг полученных результатов
table = wait_for(lambda: browser.find_element_by_class_name('shedule-group-table'))
rows = table.find_elements_by_tag_name('tr')

data = []

for row in rows:
    if not row.text:
        continue

    if re.match(r'^[0-9]+[\w]+', row.text):
        print('--------')

    print(row.text)



# + Написать скрипт на селениуме: открыть гугл, набрать "урфу", перейти на сайт "урфу",
# перейти "Студентам" -> "Расписание занятий", набрать в поисковом инпуте "РИВ-470027",
# выбрать результат, распарсить полученное расписание в произвольной форме.
# Отправлять на почту Зелёному.
