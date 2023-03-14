import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_all_pets_have_different_names(go_to_my_pets):
   '''Проверка то, что у всех моих питомцев разные имена'''

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   # Сохраняем в переменную names элементы с именами питомцев
   names = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Активируем неявные ожидания:
   pytest.driver.implicitly_wait(10)

   # Создаем список из имен питомцев
   list_names = []
   for n in range(len(names)):
      list_names.append(names[n].text)

   # Узнаем общеее количество имен своих питомцев
   number_all = len(list_names)

   # Создаем из списка множество неповторяющихся имен и вычисляем его размер
   number_uniq = len(set(list_names))

   # Сравниваем длину списков
   if number_all == number_uniq:
      print('\nУ всех моих питомцев разные имена')
   else:
      print('\nВ списке есть повторяющиеся имена')
   print('Всего питомцев:', number_all)
   print('Уникальных имен:', number_uniq)