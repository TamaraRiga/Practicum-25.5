import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_check_duplicate_pets(go_to_my_pets):
    '''Проверяем, есть ли в списке повторяющиеся питомцы'''

    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))
    # Сохраняем в переменную my_pets элементы с данными о питомцах
    my_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Настраиваем неявные ожидания:
    pytest.driver.implicitly_wait(10)

    # Проверяем, что в списке нет повторяющихся питомцев:
    list_my_pets = []
    for i in range(len(my_pets)):
        list_data = my_pets[i].text.split("\n")  # отделяем от данных питомца значок удаления питомца "х"
        list_my_pets.append(list_data[0])  # выбираем элемент с данными питомца и добавляем его в список

    # Преобразовываем список в множество
    set_my_pets = set(list_my_pets)

    # Сравниваем длину списков
    if len(list_my_pets) == len(set_my_pets):
        print('\nВ списке нет повторяющихся питомцев')
    else:
        print('\nВ списке есть повторяющиеся питомцы')
    print('Всего питомцев:', len(list_my_pets))
    print('Уникальных питомцев:', len(set_my_pets))
