from selenium import webdriver
from selenium.webdriver.common.by import By
import utilities.mssql_wrappers

import time

class Registration():
    def test(self):
        baseUrl = "http://94.130.75.130"
        tel = "9264403480"
        driver = webdriver.Firefox()
        #driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        #регистрация
        regLink = driver.find_element(By.XPATH, "html/body/app-root/div/div/div[2]/ng-component/div/div/div[2]/button[1]")
        regLink.click()

        #телефон
        driver.find_element(By.ID, "add_user__login").send_keys(tel)
        driver.find_element(By.XPATH, "html/body/app-root/div/div/div[2]/ng-component/div/ng-component/div/div/div[1]/div/span/button").click()

        #получаем код из базы sql

        sms_code = utilities.mssql_wrappers.get_sms()

        #пароль
        driver.find_element(By.ID, "add_user__password").send_keys("123456")

        #lastname field
        driver.find_element(By.ID, "add_user__lastname").send_keys("lastname1")

        #firstname field
        driver.find_element(By.ID, "add_user__firstname").send_keys("firstname1")

        #secondname field
        driver.find_element(By.ID, "add_user__secondname").send_keys("secondname1")

        #phone field
        driver.find_element(By.XPATH, ".//*[@id='add_user__phone']/input").send_keys("9265555555")


ff = Registration()
ff.test()
