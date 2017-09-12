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

        driver = webdriver.Firefox()
        #driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        #Авторизация чсро
        #телефон
        driver.find_element(By.XPATH, ".//*[@id='add_user_login']/input").send_keys(login1)
        #пароль
        driver.find_element(By.XPATH, ".//*[@id='add_user_password']").send_keys(pass1)
        #продолжить
        driver.find_element(By.XPATH, "html/body/app-root/div/div/div[2]/ng-component/div/div/div[2]/button[2]").click()
        #выход
        driver.find_element(By.XPATH, "html/body/app-root/div/div/app-topbar/div/div[2]/ul/li[1]/a/i").click()
        driver.find_element(By.XPATH, "html/body/app-root/div/div/app-topbar/div/div[2]/ul/li[1]/ul/li[3]/a").click()


        #Авторизация сро
        #телефон
        driver.find_element(By.XPATH, ".//*[@id='add_user_login']/input").send_keys(login2)
        #пароль
        driver.find_element(By.XPATH, ".//*[@id='add_user_password']").send_keys(pass2)
        #продолжить
        driver.find_element(By.XPATH, "html/body/app-root/div/div/div[2]/ng-component/div/div/div[2]/button[2]").click()
        #выход
        driver.find_element(By.XPATH, "html/body/app-root/div/div/app-topbar/div/div[2]/ul/li[1]/a/i").click()
        driver.find_element(By.XPATH, "html/body/app-root/div/div/app-topbar/div/div[2]/ul/li[1]/ul/li[3]/a").click()


        #Авторизация ко
        #телефон
        driver.find_element(By.XPATH, ".//*[@id='add_user_login']/input").send_keys(login3)
        #пароль
        driver.find_element(By.XPATH, ".//*[@id='add_user_password']").send_keys(pass3)
        #продолжить
        driver.find_element(By.XPATH, "html/body/app-root/div/div/div[2]/ng-component/div/div/div[2]/button[2]").click()
        #выход
        driver.find_element(By.XPATH, "html/body/app-root/div/div/app-topbar/div/div[2]/ul/li[1]/a/i").click()
        driver.find_element(By.XPATH, "html/body/app-root/div/div/app-topbar/div/div[2]/ul/li[1]/ul/li[3]/a").click()


        #Авторизация zak
        #телефон
        driver.find_element(By.XPATH, ".//*[@id='add_user_login']/input").send_keys(login4)
        #пароль
        driver.find_element(By.XPATH, ".//*[@id='add_user_password']").send_keys(pass4)
        #продолжить
        driver.find_element(By.XPATH, "html/body/app-root/div/div/div[2]/ng-component/div/div/div[2]/button[2]").click()
        #выход
        driver.find_element(By.XPATH, "html/body/app-root/div/div/app-topbar/div/div[2]/ul/li[1]/a/i").click()
        driver.find_element(By.XPATH, "html/body/app-root/div/div/app-topbar/div/div[2]/ul/li[1]/ul/li[3]/a").click()

        driver.execute_script("")

        #driver.quit()

ff = Autorization()
ff.test_auth()
