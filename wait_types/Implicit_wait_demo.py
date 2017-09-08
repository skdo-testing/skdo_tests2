from selenium import webdriver
from selenium.webdriver.common.by import By

class ImplicitWaitDemo():
    def test(self):
        baseUrl = "http://94.130.75.130"
        driver = webdriver.Firefox()
        #driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        loginLink = driver.find_element(By.XPATH, "html/body/app-root/div/div/div[1]/div/div[1]/app-menu/ul/li[1]/a/span")
        #loginLink = driver.find_element(By.ID, "add_user__login")
        loginLink.click()

        emailField = driver.find_element(By.ID, "add_user__login")
        emailField.send_keys("test@test")


ff = ImplicitWaitDemo()
ff.test()
