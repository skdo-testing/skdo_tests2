import unittest

from selenium import webdriver

from SKDO.classes.autorization_class import Autorization


class AutorizationTests(unittest.TestCase):

    def test_autorization(self):

        baseUrl = "http://i.skdo.ru"
        driver = webdriver.Chrome()
        #driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        at = Autorization(driver)

        #csro
        at.testLogin("1111111111", "111")
        #sro
        at.testLogin("2222222222", "222")
        #ko
        at.testLogin("3333333333", "333")
        #zak
        at.testLogin("4444444444", "444")


# if __name__ == '__main__':
#     unittest.main(verbosity=2)
