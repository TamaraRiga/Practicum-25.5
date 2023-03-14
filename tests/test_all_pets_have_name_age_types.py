import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_all_pets_have_name_age_types(go_to_my_pets):
   '''Проверка наличия у всех моих питомцев имени, возраста и типа'''

   element = WebDriverWait(pytest.driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))
   # Сохраняем в переменную pet_data все элементы с данными о питомцах
   pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Вычисляем количество карточек своих питомцев
   number_of_card_pets = len(pet_data)
   print(f'\nКоличество карточек моих питомцев: {number_of_card_pets}')

   # Настраиваем переменную явного ожидания:
   wait = WebDriverWait(pytest.driver, 5)

   # Ожидаем, что данные всех питомцев, найденных локатором CSS_SELECTOR = '.table.table-hover tbody tr', видны на странице:
   for i in range(number_of_card_pets):
      assert wait.until(EC.visibility_of(pet_data[i]))

   # Сохраняем в переменную names все элементы с именами и ожидаем увидеть их на странице:
   names = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[1]')
   for i in range(len(names)):
      assert wait.until(EC.visibility_of(names[i]))

   # Находим количество моих питомцев с именами
   number_with_name = 0
   for i in range(len(names)):
      if names[i].text != '':
         number_with_name += 1
      else:
         number_with_name += 0
   print(f'Количество питомцев с именем: {number_with_name}')

   # Сохраняем в переменную animal_types все элементы с типами животных и ожидаем увидеть их на странице:
   animal_types = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[2]')
   for i in range(len(animal_types)):
      assert wait.until(EC.visibility_of(animal_types[i]))

   # Находим количество моих питомцев с указанием типа
   number_with_types = 0
   for i in range(len(animal_types)):
      if animal_types[i].text != '':
         number_with_types += 1
      else:
         number_with_types += 0
   print(f'Количество питомцев с указанием типа: {number_with_types}')

   # # Сохраняем в переменную ages все элементы с возрастом животных и ожидаем увидеть их на странице:
   ages = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[3]')
   for i in range(len(ages)):
      assert wait.until(EC.visibility_of(ages[i]))

   # Находим количество моих питомцев с указанием возраста
   number_with_age = 0
   for i in range(len(ages)):
      if ages[i].text != '':
         number_with_age += 1
      else:
         number_with_age += 0
   print(f'Количество питомцев с указанием возраста: {number_with_age}')


   try:
      for i in range(len(names)):
         assert names[i].text != ''
         assert animal_types[i].text != ''
         assert ages[i].text != ''
   except AssertionError:
      print(f'Питомец {i} имеет пустое поле')

