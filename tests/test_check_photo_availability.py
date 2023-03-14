import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_check_photo_availability(go_to_my_pets):
    '''Проверяем, что хотя бы у половины моих питомцев есть фото'''

    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'th>img')))
    # Записываем в переменную images все существующие элементы с img
    images = pytest.driver.find_elements(By.CSS_SELECTOR, 'th>img')

    pytest.driver.implicitly_wait(5)
    # Находим количество моих питомцев с фотографией
    number_with_photo = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            number_with_photo += 1
        else:
            number_with_photo += 0
    print('\nКоличество питомцев с фото:', number_with_photo)

    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))
    # Вычисляем количество карточек своих питомцев
    number_of_card_pets = len(pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr'))
    print(f'Общее количество моих питомцев: {number_of_card_pets}')
    
    # Сравниваем количество питомцев с фото и количество карточек
    if number_with_photo == number_of_card_pets:
        print('Все мои питомцы имеют фото')
    elif number_with_photo < number_of_card_pets:
        if number_with_photo >= (number_of_card_pets) // 2:
            print('Больше половины моих питомцев имеют фото')
        else:
            print('Меньше половины моих питомцев имеют фото')
