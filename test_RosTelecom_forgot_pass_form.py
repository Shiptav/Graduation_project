import pytest
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from datasett import valid_email,invalid_password

# Проверка №16 "Забыл пароль", если введены неверные логин и пароль кнопка "Забыл пароль" перекрашивается в оранжевый цвет
def test_colore_forget_password_orange(Chrome_drv_auth_page,email=valid_email,invpassword=invalid_password):
   pytest.driver.find_element(By.ID,'username').send_keys(email) #Вводим данные аккаунта почта
   pytest.driver.find_element(By.ID,'password').send_keys(invpassword) #Вводим неправильный пароль
   pytest.driver.find_element(By.ID,'kc-login').click() #Нажимаем на кнопку "Войти"
   #  button_colore=pytest.driver.find_element(By.XPATH, '//*[@id="forgot_password"]').value_of_css_property('background-color')
   #Получение атрибута класса чтобы проверить, что кнопка перекрасилась в оранжевый цвет
   button_colore=pytest.driver.find_element(By.XPATH, '//*[@id="forgot_password"]').get_attribute('class')
   #Если в атрибуте класса одновременно содержатся слова "animated" и "orange" будем считать что кнопка перекрасилась
   time.sleep(2)
   if "animated"  in button_colore and "orange" in button_colore: 
         assert "orange"=="orange" #Ожидаемый результат кнопка перекрасилась
   else:
      raise Exception('Incorrect_button_color') # Если кнопка не перекрасилась выдать Исключение некорректный цвет кнопки 

# Проверка №17 "Забыл пароль", при нажатии забыл пароль Tab Телефон выбран по умолчанию
def test_forgot_password_phone_selected_by_default(Chrome_drv_auth_page):
   pytest.driver.find_element(By.ID,'t-btn-tab-mail').click() #Поиск кнопки Tab почта на стартовой странице и нажатие на нее
   pytest.driver.find_element(By.ID,'forgot_password').click() #Поиск кнопки "Забыл пароль" на стартовой странице и нажатие на нее
   #Поиск заголовка формы "Восстановление пароля" на странице
   forgot_password=pytest.driver.find_element(By.CLASS_NAME, "card-container__title").text
   # Ожидаемый результат текс "Восстановление пароля"
   assert forgot_password == "Восстановление пароля"
   
   time.sleep(2)# Задержка перед скриншотом
   if forgot_password=="Восстановление пароля": # Если результат текс "Восстановление пароля"
      # Make the screenshot of browser window:
      pytest.driver.save_screenshot('forgot_password.png') 
   else:
      raise Exception("Forgot_password_button_error")# Если результат не текс "Восстановление пароля" выдать Исключение с предупреждением 
   
   phone_tab_active=pytest.driver.find_element(By.ID,'t-btn-tab-phone').get_attribute('class')
   if "active" in phone_tab_active: # Проверка что выбран Tab Телефон
         assert "phone_tab_active"=="phone_tab_active" # тут не соответсвует требованиям, активна та вкладка с которой был переход на восстановление пароля
   else:
      raise Exception('Another_tab_is_active') # Если результат не Tab Телефон выдать Исключение с предупреждением
   