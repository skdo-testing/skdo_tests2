from selenium import webdriver
from selenium.webdriver.common.by import By


class Autorization():

    def __init__(self, driver):
        self.driver = driver

    def testLogin(self, telephone, password):
        #телефон
        self.driver.find_element_by_xpath('//p-inputmask[@id="add_user_login"]/input').send_keys(telephone)
        #пароль
        self.driver.find_element_by_id('add_user_password').send_keys(password)
        #продолжить
        self.driver.find_elements_by_xpath('//button[@label="Продолжить"]')[0].click()
        #выход
        self.driver.find_element_by_xpath('//*[@id="topbar-menu-button"]').click()
        self.driver.find_element_by_xpath('/html/body/app-root/div/div/app-topbar/div/div[2]/ul/li[1]/a/span').click()
        self.driver.find_element_by_xpath('/html/body/app-root/div/div/app-topbar/div/div[2]/ul/li[1]/ul/li[3]/a/span').click()
