import pytest
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from datasett import valid_email,valid_password,invalid_email,invalid_password,invalid_phone,valid_login,valid_phone

# Проверка №1 "Переход на основную страницу", Продуктовый слоган ЛК "Ростелеком ID" 
def test_main_page(Chrome_drv_auth_page):
   logo_page=pytest.driver.find_element(By.CLASS_NAME, "what-is__desc").text #Поиск слогана на странице ЛК "Ростелеком ID"
   # Ожидаемые результат надпись
   assert logo_page=="Персональный помощник в цифровом мире Ростелекома"
 
# Проверка №2 "Авторизация", проверка перехода на Tab "Телефон" в форме авторизации появилась мобильный телефон     
def test_auth_form_tab_phone(Chrome_drv_auth_page):
   auth_form=pytest.driver.find_element(By.CLASS_NAME, "card-container__title").text #Поиск заголовка формы "Авторизация" на странице
   pytest.driver.find_element(By.ID,'t-btn-tab-phone').click() # Выбор Tab "Телефон"
   # Получение текста из формы ввода
   auth_form_phone=pytest.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text
   #Ожидаемые результаты надпись "Авторизация" и "Телефон"
   assert auth_form=="Авторизация"
   assert auth_form_phone=="Мобильный телефон"

# Проверка №3 "Авторизация", проверка перехода на Tab "Почта" в форме авторизации появилась надпись Электронная почта  
def test_auth_form_tab_mail(Chrome_drv_auth_page):
   auth_form=pytest.driver.find_element(By.CLASS_NAME, "card-container__title").text #Поиск заголовка формы "Авторизация" на странице
   pytest.driver.find_element(By.ID,'t-btn-tab-mail').click() # Выбор Tab "Почта"
   # Получение текста из формы ввода 
   auth_form_mail=pytest.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text
   #Ожидаемые результаты надпись "Авторизация" и "Электронная почта"
   assert auth_form=="Авторизация"
   assert auth_form_mail=="Электронная почта"

# Проверка №4 "Авторизация", проверка перехода на Tab "Логин" в форме авторизации появилась надпись логин  
def test_auth_form_tab_login(Chrome_drv_auth_page):
   auth_form=pytest.driver.find_element(By.CLASS_NAME, "card-container__title").text #Поиск заголовка формы "Авторизация" на странице
   pytest.driver.find_element(By.ID,'t-btn-tab-login').click() # Выбор Tab "Логин"
   # Получение текста из формы ввода 
   auth_form_login=pytest.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text
   #Ожидаемые результаты надпись "Авторизация" и "Логин"
   assert auth_form=="Авторизация"
   assert auth_form_login=="Логин"       

# Проверка №5 "Авторизация", проверка перехода на Tab "Лицевой счёт" в форме авторизации появилась надпись лицевой счет
def test_auth_form_tab_account(Chrome_drv_auth_page):
   auth_form=pytest.driver.find_element(By.CLASS_NAME, "card-container__title").text #Поиск заголовка формы "Авторизация" на странице
   pytest.driver.find_element(By.ID,'t-btn-tab-ls').click() # Выбор Tab "Лицевой счёт"
   # Получение текста из формы ввода 
   auth_form_account=pytest.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text
   #Ожидаемые результаты надпись "Авторизация" и "Лицевой счёт"
   assert auth_form=="Авторизация"
   assert auth_form_account=="Лицевой счёт"  

# Проверка №6 "Авторизация", проверка если неверный номер телефона
def test_auth_form_wrong_pnone_number_warning(Chrome_drv_auth_page,invphone=invalid_phone):
   auth_form=pytest.driver.find_element(By.CLASS_NAME, "card-container__title").text #Поиск заголовка формы "Авторизация" на странице
   pytest.driver.find_element(By.ID,'t-btn-tab-phone').click() # Выбор Tab телефон
   pytest.driver.find_element(By.ID,'username').send_keys(invphone) # Вводим телефон в неправильном формате
   pytest.driver.find_element(By.ID,'password').click() #Переход на свободное поле
   # Получение текста сообщения об ошибке
   wrong_phone=pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text
   #Ожидаемые результаты надпись "Авторизация" и текст ошибки под формой "Данные для входа"
   assert auth_form=="Авторизация"
   assert wrong_phone=="Неверный формат телефона"

# Проверка №7 "Авторизация", происходит авторизация при вводе корректного email и пароля
def test_auth_by_mail(Chrome_drv_auth_page,email=valid_email,password=valid_password):
   pytest.driver.find_element(By.ID,'username').send_keys(email)# Вводим email
   pytest.driver.find_element(By.ID,'password').send_keys(password)# Вводим пароль
   pytest.driver.find_element(By.ID,'kc-login').click() # Нажимаем на кнопку входа в аккаунт
   #Проверка что на новой странице содержится заголовок Учетные данные
   account_data=pytest.driver.find_element(By.CLASS_NAME, "card-title").text
   time.sleep(2) #задержка перед скриншотом
   if account_data=="Учетные данные":
        # Make the screenshot of browser window:
      pytest.driver.save_screenshot('auth_by_mail.png')
   else:
        raise Exception("login_error") # Если результат "Учетные данные" выдать Исключения, ошибка логина
   assert account_data=="Учетные данные" # Ожидаемый результат учетные данные

# Проверка №8 "Авторизация", проверка если неверный лицевой счет
def test_auth_form_wrong_account_warning(Chrome_drv_auth_page,invphone=invalid_phone):
   auth_form=pytest.driver.find_element(By.CLASS_NAME, "card-container__title").text #Поиск заголовка формы "Авторизация" на странице
   pytest.driver.find_element(By.ID,'t-btn-tab-ls').click() # Выбор Tab лицевой счет
   pytest.driver.find_element(By.ID,'username').send_keys(invphone)# Вводим лицевой счет в неправильном формате
   pytest.driver.find_element(By.ID,'password').click() #Переход на свободное поле
   # Получение текста сообщения об ошибке
   wrong_phone=pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text
   #Ожидаемые результаты надпись "Авторизация" и текст ошибки под формой "Данные для входа"
   assert auth_form=="Авторизация"
   assert wrong_phone=="Проверьте, пожалуйста, номер лицевого счета"

# Проверка №9 "Авторизация", происходит авторизация при вводе корректного логина и пароля
def test_auth_by_login(Chrome_drv_auth_page,login=valid_login,password=valid_password):
   pytest.driver.find_element(By.ID,'username').send_keys(login)# Вводим логин
   pytest.driver.find_element(By.ID,'password').send_keys(password) # Вводим пароль
   pytest.driver.find_element(By.ID,'kc-login').click()# Нажимаем на кнопку входа в аккаунт
   #Проверка что на новой странице содержится заголовок Учетные данные
   account_data=pytest.driver.find_element(By.CLASS_NAME, "card-title").text
   time.sleep(2) #задержка перед скриншотом
   if account_data=="Учетные данные":
        # Make the screenshot of browser window:
      pytest.driver.save_screenshot('auth_by_login.png')
   else:
        raise Exception("login_error") # Если результат "Учетные данные" выдать Исключения, ошибка логина
   assert account_data=="Учетные данные" # Ожидаемый результат учетные данные

# Проверка №10 "Авторизация", происходит авторизация при вводе корректного телефона и пароля
def test_auth_by_phone(Chrome_drv_auth_page,phone=valid_phone,password=valid_password):
   pytest.driver.find_element(By.ID,'username').send_keys(phone) # Вводим телефон
   pytest.driver.find_element(By.ID,'password').send_keys(password) # Вводим пароль
   pytest.driver.find_element(By.ID,'kc-login').click() # Нажимаем на кнопку входа в аккаунт
   #Проверка что на новой странице содержится заголовок Учетные данные
   account_data=pytest.driver.find_element(By.CLASS_NAME, "card-title").text
   time.sleep(2)# задержка перед скриншотом
   if account_data=="Учетные данные": # Если надпись есть надпись Учетные данные, делаем скриншот
        # Make the screenshot of browser window:
      pytest.driver.save_screenshot('auth_by_phone.png')
   else:
        raise Exception("login_error")  # Если результат "Учетные данные" выдать Исключения, ошибка логина
   assert account_data=="Учетные данные" # Ожидаемый результат учетные данные

# Проверка №11 "Авторизация", при вводе неправильной почты выдается предупреждение "Неверный логин или пароль"
def test_wrong_mail(Chrome_drv_auth_page,invmail=invalid_email,password=valid_password):
   pytest.driver.find_element(By.ID,'username').send_keys(invmail)# Вводим неправильный email
   pytest.driver.find_element(By.ID,'password').send_keys(password)  # Вводим пароль
   pytest.driver.find_element(By.ID,'kc-login').click() # Нажимаем на кнопку входа в аккаунт
   # Получение текста сообщения об ошибке
   wrong_login_or_password=pytest.driver.find_element(By.ID,'form-error-message').text
   assert wrong_login_or_password=="Неверный логин или пароль" #Ожидаемый результат Неверный логин или пароль

# Проверка №12 "Авторизация", при вводе неправильного пароля выдается предупреждение "Неверный логин или пароль"
def test_wrong_password(Chrome_drv_auth_page,mail=valid_email,invpassword=invalid_password):
   pytest.driver.find_element(By.ID,'username').send_keys(mail) # Вводим email
   pytest.driver.find_element(By.ID,'password').send_keys(invpassword) # Вводим пароль
   pytest.driver.find_element(By.ID,'kc-login').click() # Нажимаем на кнопку входа в аккаунт
   # Получение текста сообщения об ошибке
   wrong_login_or_password=pytest.driver.find_element(By.ID,'form-error-message').text
   assert wrong_login_or_password=="Неверный логин или пароль" #Ожидаемый результат Неверный логин или пароль

# Проверка №13 "Авторизация", Tab "Телефон" меняется на Tab "Почта" если в поле телефон ввести данные в формате почты 
def test_tab_phone_changing_to_mail(Chrome_drv_auth_page,mail=valid_email):
   auth_form=pytest.driver.find_element(By.CLASS_NAME, "card-container__title").text #Поиск заголовка формы "Авторизация" на странице
   pytest.driver.find_element(By.ID,'t-btn-tab-phone').click() #Поиск кнопки Tab телефон на стартовой странице и нажатие на нее
   pytest.driver.find_element(By.ID,'username').send_keys(mail) #Поиск поля ввода данных и ввод в формате почта
   pytest.driver.find_element(By.ID,'password').click() #Переход на свободное поле
   #Получение атрибута класса чтобы проверить, что Tab почта активный
   mail_tab_active=pytest.driver.find_element(By.ID,'t-btn-tab-mail').get_attribute('class')
   if "active" in mail_tab_active: #Если Tab Почта активный(содержание Active в атрибуте класса)
         assert "mail_tab_active"=="mail_tab_active" #Ожидаемый результат почта активный
   else:
      raise Exception('Tab_mail_is_not_active') # Если результат не Tab почта выдать Исключения, Tab почта не активен
   #Ожидаемый результат надпись авторизация на странице
   assert auth_form == "Авторизация" 


# Проверка №14 "Авторизация", Tab "Почта" меняется на Tab "Логин" если в поле почты ввести данные в формате телефона
def test_tab_mail_changing_to_phone(Chrome_drv_auth_page,phone=valid_phone):
   auth_form=pytest.driver.find_element(By.CLASS_NAME, "card-container__title").text #Поиск заголовка формы "Авторизация" на странице
   pytest.driver.find_element(By.ID,'t-btn-tab-mail').click() #Поиск кнопки Tab почта на стартовой странице и нажатие на нее
   pytest.driver.find_element(By.ID,'username').send_keys(phone) #Поиск поля ввода данных и ввод в формате Телефон
   pytest.driver.find_element(By.ID,'password').click() #Переход на свободное поле
   #Получение атрибута класса чтобы проверить, что Tab Телефон активный
   phone_tab_active=pytest.driver.find_element(By.ID,'t-btn-tab-phone').get_attribute('class')
   if "active" in phone_tab_active: #Если Tab Телефон активный(содержание Active в атрибуте класса)
         assert "phone_tab_active"=="phone_tab_active" #Ожидаемый результат телефон активный
   else:
      raise Exception('Tab_phone_is_not_active') # Если результат не Tab телефон выдать Исключения, Tab телефон не активен
   #Ожидаемый результат надпись авторизация на странице
   assert auth_form == "Авторизация"


# Проверка №15 "Авторизация", Tab "Почта" меняется на Tab "Логин" если в поле почты ввести данные в формате логина
def test_tab_mail_changing_to_login(Chrome_drv_auth_page):
   auth_form=pytest.driver.find_element(By.CLASS_NAME, "card-container__title").text #Поиск заголовка формы "Авторизация" на странице
   pytest.driver.find_element(By.ID,'t-btn-tab-mail').click() #Поиск кнопки Tab почта на стартовой странице и нажатие на нее
   pytest.driver.find_element(By.ID,'username').send_keys(valid_login) #Поиск поля ввода данных и ввод в формате логин
   pytest.driver.find_element(By.ID,'password').click() #Переход на свободное поле
   #Получение атрибута класса чтобы проверить, что Tab Логин активный
   ls_tab_active=pytest.driver.find_element(By.ID,'t-btn-tab-login').get_attribute('class')
   if "active" in ls_tab_active: #Если Tab Логин активный(содержание Active в атрибуте класса)
         assert "ls_tab_active"=="ls_tab_active" #Ожидаемый результат логин активный
   else:
      raise Exception('Tab_login_is_not_active') # Если результат не Tab Логин выдать Исключения, Tab логин не активен
   #Ожидаемый результат надпись авторизация на странице
   assert auth_form == "Авторизация"
 
