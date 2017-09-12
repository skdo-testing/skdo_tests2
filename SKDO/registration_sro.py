from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import utilities.mssql_wrappers

import time

class Registration_sro():
    def test(self):
        tel = "8888888881"
        baseUrl = "http://i.skdo.ru/#/add/reg_main"

        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.implicitly_wait(30)

        #кнопка регистрация
        #driver.find_element(By.XPATH, "html/body/app-root/div/div/div[2]/ng-component/div/div/div[2]/button[1]").click()
        #получаем код из базы sql
        #sms_code = utilities.mssql_wrappers.get_sms()

        ### Раздел Общие данные
        #телефон
        driver.find_element(By.XPATH, "//*[@id='add_user_login']").click()
        driver.find_element(By.XPATH, "//*[@id='add_user_login']").send_keys(tel)
        #пароль
        driver.find_element(By.XPATH, "//*[@id='add_user__password']").send_keys("99999999")
        #фамилия
        driver.find_element(By.XPATH, "//*[@id='add_user__lastname']").send_keys("фамилия1")
        #имя
        driver.find_element(By.XPATH, "//*[@id='add_user__firstname']").send_keys("имя1")
        #отчество
        driver.find_element(By.XPATH, "//*[@id='add_user__secondname']").send_keys("отчество1")
        #почта
        driver.find_element(By.XPATH, "//*[@id='add_user_email']").send_keys("itdev4@skdo.ru")
        #выбрать роль СРО
        driver.find_element(By.XPATH, ".//*[@id='add_user__roles']/div/label").click()
        driver.find_element(By.XPATH, ".//*[@id='add_user__roles']/div/div[3]/div/ul/li[2]/span").click()
        #продолжить
        driver.find_element(By.XPATH, "html/body/app-root/div/div/div[2]/ng-component/div/ng-component/div/div/div[5]/button").click()

        ###Раздел Тариф
        #Тариф 1
        driver.find_element_by_xpath("/html/body/app-root/div[@class='layout-wrapper']/div[@class='layout-container menu-layout-static']/div[@class='layout-main']/ng-component/div[@class='ui-g ui-fluid']/ng-component/div[@class='ui-g ui-fluid']/div[@class='ui-g-12 ui-lg-6'][1]/div[@class='card'][1]/div/button[@class='ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only']/span[@class='ui-button-text ui-clickable']").click()

        ### Раздел Организация

        #Тип организации(юр лицо)
        driver.find_element(By.XPATH, ".//*[@id='dropdown']/div/label").click()
        driver.find_element(By.XPATH, ".//*[@id='dropdown']/div/div[3]/div/ul/li[2]/span").click()
        # полное наименование
        driver.find_element(By.XPATH, ".//*[@id='add_full_orgName']").send_keys("ООО Рога-Копыта")
        # сокращенное наименование
        driver.find_element(By.XPATH, ".//*[@id='add_orgName']").send_keys("Рога-Копыта")
        # ИНН
        driver.find_element(By.XPATH, ".//*[@id='add_inn10']/input").click()
        driver.find_element(By.XPATH, ".//*[@id='add_inn10']/input").send_keys("1111111111")
        # КПП
        driver.find_element(By.XPATH, ".//*[@id='add_kpp']/input").click()
        driver.find_element(By.XPATH, ".//*[@id='add_kpp']/input").send_keys("111111111")


ff = Registration_sro()
ff.test()
