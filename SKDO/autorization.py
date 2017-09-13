from selenium import webdriver
from selenium.webdriver.common.by import By

class Autorization():
    def test_auth(self):
        baseUrl = "http://i.skdo.ru"
        #csro
        login1 = "1111111111"
        pass1 = "111"
        #sro
        login2 = "2222222222"
        pass2 = "222"
        #ko
        login3 = "3333333333"
        pass3 = "333"
        #zak
        login4 = "4444444444"
        pass4 = "444"

        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        #Авторизация чсро
        #телефон
        driver.find_element_by_xpath('//p-inputmask[@id="add_user_login"]/input').send_keys(login1)
        #пароль
        driver.find_element_by_id('add_user_password').send_keys(pass1)
        #продолжить
        driver.find_elements_by_xpath('//button[@label="Продолжить"]')[0].click()
        #выход
        driver.find_element_by_xpath('//*[@id="topbar-menu-button"]').click()
        driver.find_element_by_xpath('/html/body/app-root/div/div/app-topbar/div/div[2]/ul/li[1]/a/span').click()
        driver.find_element_by_xpath('/html/body/app-root/div/div/app-topbar/div/div[2]/ul/li[1]/ul/li[3]/a/span').click()


        #Авторизация сро
        #телефон
        driver.find_element_by_xpath('//p-inputmask[@id="add_user_login"]/input').send_keys(login2)
        #пароль
        driver.find_element_by_id('add_user_password').send_keys(pass2)
        #продолжить
        driver.find_elements_by_xpath('//button[@label="Продолжить"]')[0].click()
        #выход
        driver.find_element_by_xpath('//*[@id="topbar-menu-button"]').click()
        driver.find_element_by_xpath('/html/body/app-root/div/div/app-topbar/div/div[2]/ul/li[1]/a/span').click()
        driver.find_element_by_xpath('/html/body/app-root/div/div/app-topbar/div/div[2]/ul/li[1]/ul/li[3]/a/span').click()


        #Авторизация ко
        #телефон
        driver.find_element_by_xpath('//p-inputmask[@id="add_user_login"]/input').send_keys(login3)
        #пароль
        driver.find_element_by_id('add_user_password').send_keys(pass3)
        #продолжить
        driver.find_elements_by_xpath('//button[@label="Продолжить"]')[0].click()
        #выход
        driver.find_element_by_xpath('//*[@id="topbar-menu-button"]').click()
        driver.find_element_by_xpath('/html/body/app-root/div/div/app-topbar/div/div[2]/ul/li[1]/a/span').click()
        driver.find_element_by_xpath('/html/body/app-root/div/div/app-topbar/div/div[2]/ul/li[1]/ul/li[3]/a/span').click()


        #Авторизация zak
        #телефон
        driver.find_element_by_xpath('//p-inputmask[@id="add_user_login"]/input').send_keys(login4)
        #пароль
        driver.find_element_by_id('add_user_password').send_keys(pass4)
        #продолжить
        driver.find_elements_by_xpath('//button[@label="Продолжить"]')[0].click()
        #выход
        driver.find_element_by_xpath('//*[@id="topbar-menu-button"]').click()
        driver.find_element_by_xpath('/html/body/app-root/div/div/app-topbar/div/div[2]/ul/li[1]/a/span').click()
        driver.find_element_by_xpath('/html/body/app-root/div/div/app-topbar/div/div[2]/ul/li[1]/ul/li[3]/a/span').click()

#        driver.execute_script("")

        #driver.quit()

ff = Autorization()
ff.test_auth()
