import pytest
from settings import valid_email, valid_password
from selenium.webdriver.common.by import By

def test_show_all_pets():
    '''Проверка карточек питомцев - тест из модуля 25.3'''
    '''Тест постоянно проваливается, так как в системе много багов и могут создаваться карточки без имени или других атрибутов'''

    # Вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Активируем неявное ожидание после нажатия кнопки входа
    pytest.driver.implicitly_wait(10)

    # Проверяем, что мы оказались на главной странице пользователя
    # assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'

    # Объявляем три переменные, в которых записываем все найденные элементы на странице:
    # в images — все картинки питомцев, в names — все их имена, в descriptions — все виды и возрасты.
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    try:
        for i in range(len(names)):
            assert images[i].text != ''
            assert names[i].text != ''
            assert descriptions[i].text != ''
    except AssertionError:
        print('\nВ карточке питомца имеется пустое поле')

    # Для перебора элементов организовали цикл, где длину можно взять любую из объявленных выше переменных,
    # так как количество карточек равно количеству имён, картинок и описаний).
    for i in range(len(names)):
        # Для проверки существования фото в карточке проверяем, что путь, указанный в атрибуте src, не пустой.
        assert images[i].get_attribute('src') != ''  # Каждая картинка имеет атрибут src, если была загружена

        # Смотрим, что элемент, который должен содержать имя i-го питомца, имеет не пустой текст
        assert names[i].text != ''  # в системе баг - могут добавляться питомцы без имени

        # Чтобы убедиться, что в данном элементе выводится и возраст, и вид питомца, ищем в тексте этого элемента запятую,
        # так как считаем её разделителем между этими двумя сущностями.
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0  #  каждая из частей разделённой строки будет длиной больше нуля.
        assert len(parts[1]) > 0  # это будет означать, что наша страница в карточке содержит и вид, и возраст питомца



# python3 -m pytest -v --driver Chrome --driver-path /tests/chromedriver tests/test_show_all_pets.py