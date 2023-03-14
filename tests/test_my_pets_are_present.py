import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_my_pets_are_present(go_to_my_pets):
   '''Проверка того, что на странице со списком моих питомцев присутствуют все питомцы'''

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))
   # Сохраняем в переменную card_pets карточки питомцев
   card_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Получаем количество карточек питомцев
   number_of_card_pets = len(card_pets)

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
   # Сохраняем в переменную statist элементы статистики
   statist = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')

   # Настраиваем неявные ожидания:
   pytest.driver.implicitly_wait(5)

   # Получаем количество питомцев из данных статистики
   number = statist[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

   assert number_of_card_pets == number
   print(f'\t {number_of_card_pets} = {number}')  # для наглядности выведем количество питомцев пользователя