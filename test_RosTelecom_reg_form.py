import pytest
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# Проверка №18 "Регистрация", при нажатии на кнопку регистрация осуществляется переход к форме регистрации
def test_button_reg_working(Chrome_drv_auth_page):
   pytest.driver.find_element(By.ID,'kc-register').click() #Поиск кнопки "Регистрация" на стартовой странице и нажатие на нее
   reg_page=pytest.driver.find_element(By.CLASS_NAME, "card-container__title").text #Поиск заголовка формы "Регистрация" на странице
   assert reg_page == "Регистрация" #Ожидаемый результат надпись формы"Регистрация"
   time.sleep(2) # Задержка перед скриншотом
   if reg_page=="Регистрация":
      # Make the screenshot of browser window:
      pytest.driver.save_screenshot('reg_page.png')
   else:
      raise Exception("Button_reg_error") # Если результат не "Регистрация" выдать Исключение с предупреждением  
 

# Проверка №19 "Регистрация",выдается сообщение: "Необходимо заполнить поле кириллицей...", если Фамилия введена НЕ кирилицей
def test_reg_firstname_Cyrillic_only(Chrome_drv_auth_page):
   pytest.driver.find_element(By.ID,'kc-register').click() #Поиск кнопки "Регистрация" на стартовой странице и нажатие на нее
   reg_page=pytest.driver.find_element(By.CLASS_NAME, "card-container__title").text #Поиск заголовка формы "Регистрация" на странице
   pytest.driver.find_element(By.NAME,'firstName').send_keys('AAAAAAAAAA') #Поиск поля "Фамилия" на странице и ввод 
   pytest.driver.find_element(By.NAME,'lastName').click() #Переход на другое поле, чтобы появилось сообщение о мета ошибке
   #Получение текста сообщения содержащегося в ошибке
   wrong_firsname_format=pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span').text
    #Ожидаемые результаты надпись "Регистрация" и "Текст ошибки под формой Имя"
   assert reg_page == "Регистрация"
   assert wrong_firsname_format == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

# Проверка №20 "Регистрация",выдается сообщение: "Необходимо заполнить поле кириллицей...", если Фамилия введена НЕ кирилицей
def test_reg_lastName_Cyrillic_only(Chrome_drv_auth_page):
   pytest.driver.find_element(By.ID,'kc-register').click() #Поиск кнопки "Регистрация" на стартовой странице и нажатие на нее
   reg_page=pytest.driver.find_element(By.CLASS_NAME, "card-container__title").text #Поиск заголовка формы "Регистрация" на странице
   pytest.driver.find_element(By.NAME,'lastName').send_keys('11111') #Поиск поля "Фамилия" на странице и ввод 
   pytest.driver.find_element(By.NAME,'firstName').click() #Переход на другое поле, чтобы появилось сообщение о мета ошибке
   #Получение текста сообщения содержащегося в ошибке
   wrong_lastName_format=pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text
   #Ожидаемые результаты надпись "Регистрация" и "Текст ошибки под формой Фамилия"
   assert reg_page == "Регистрация"
   assert wrong_lastName_format == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Проверка №21 "Регистрация",выдается сообщение: "Телефон и email в определенном формате", если введены некорректно
def test_reg_login_details_wrong_format(Chrome_drv_auth_page):
   pytest.driver.find_element(By.ID,'kc-register').click() #Поиск кнопки "Регистрация" на стартовой странице и нажатие на нее
   reg_page=pytest.driver.find_element(By.CLASS_NAME, "card-container__title").text #Поиск заголовка формы "Регистрация" на странице
   pytest.driver.find_element(By.ID,'address').send_keys('11111') #Поиск поля "Данные для входа" на странице и ввод 
   pytest.driver.find_element(By.NAME,'firstName').click() #Переход на другое поле, чтобы появилось сообщение о мета ошибке
   #Получение текста сообщения содержащегося в ошибке
   wrong_login_details_format=pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/span').text
   #Ожидаемые результаты надпись "Регистрация" и текст ошибки под формой "Данные для входа"
   assert reg_page == "Регистрация"
   assert wrong_login_details_format == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"


# Проверка №22 "Регистрация",выдается сообщение: "Длина пароля должна быть не менее 8 символов", если введеный пароль короче установленной длины
def test_reg_password_length(Chrome_drv_auth_page):
   pytest.driver.find_element(By.ID,'kc-register').click() #Поиск кнопки "Регистрация" на стартовой странице и нажатие на нее
   reg_page=pytest.driver.find_element(By.CLASS_NAME, "card-container__title").text #Поиск заголовка формы "Регистрация" на странице
   pytest.driver.find_element(By.ID,'password').send_keys('11111') #Поиск поля "Пароль" на странице и ввод 
   pytest.driver.find_element(By.NAME,'firstName').click() #Переход на другое поле, чтобы появилось сообщение о мета ошибке
   #Получение текста сообщения содержащегося в ошибке
   password_length=pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text
   #Ожидаемые результаты надпись "Регистрация" и "Текст ошибки под формой задания пароля"
   assert reg_page == "Регистрация"
   assert password_length == "Длина пароля должна быть не менее 8 символов"
