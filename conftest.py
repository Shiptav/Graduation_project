
import pytest
from selenium import webdriver


@pytest.fixture()
def Chrome_drv_auth_page():
   pytest.driver = webdriver.Chrome('C:/Users/Antony/OneDrive/Desktop/QAP/LS30/driver/chromedriver.exe')
   pytest.driver.implicitly_wait(10)
   # Переходим на страницу авторизации Ростелеком
   pytest.driver.get('https://b2c.passport.rt.ru/auth/')

   yield

   pytest.driver.quit()
