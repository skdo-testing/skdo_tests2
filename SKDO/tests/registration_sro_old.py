from selenium import webdriver
import time
from random import randint
import unittest

class RegistrationSro1(unittest.TestCase):
    def test(self):
        tel = randint(1, 9999999999)

        driver=webdriver.Chrome()
        driver.get('http://i.skdo.ru/#/add/reg_main')


        driver.find_element_by_xpath('//p-inputmask[@id="add_user_login"]/input').send_keys(tel)
        driver.find_element_by_id('add_user__password').send_keys("99999999")
        driver.find_element_by_id('add_user__lastname').send_keys("Zubar")
        driver.find_element_by_id('add_user__firstname').send_keys("Aleksey")
        driver.find_element_by_id('add_user__secondname').send_keys("Olegovich")
        driver.find_element_by_id('add_user_email').send_keys("lesha9615@gmail.com")

        #Выбор роли
        driver.find_element_by_xpath('//span[@class="fa fa-fw fa-caret-down ui-clickable"]').click()
        time.sleep(4)
        driver.find_element_by_xpath('//div[@class="ui-dropdown-items-wrapper"]/ul/li[2]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//span[@class="ui-button-text ui-clickable"]').click()
        time.sleep(10)
        driver.find_elements_by_xpath('//span[@class="ui-button-text ui-clickable"]')[5].click()
        time.sleep(3)

        driver.find_element_by_id('add_full_orgName').send_keys("Invest")
        driver.find_element_by_id('add_orgName').send_keys("In")
        driver.find_element_by_xpath('//p-dropdown[@id="dropdown"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//div[@class="ui-dropdown-items-wrapper"]/ul/li[2]/span').click()
        driver.find_element_by_xpath('//p-inputmask[@id="add_inn10"]/input').send_keys("1234567890")
        driver.find_element_by_xpath('//p-inputmask[@id="add_kpp"]/input').send_keys("098765432")
        driver.find_element_by_xpath('//p-inputmask[@id="add_ogrn13"]/input').send_keys("1234567890123")
        driver.find_element_by_xpath('//p-calendar[@id="calendar"]/span/input').send_keys("07.08.2016")
        driver.find_elements_by_xpath('//span[@class="ui-button-text ui-clickable"]')[0].click()
        time.sleep(2)
        driver.find_element_by_xpath('//p-dropdown[@id="add_accountType"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//div[@class="ui-dropdown-items-wrapper"]/ul/li[2]/span').click()
        driver.find_element_by_xpath('//p-inputmask[@id="add_checkingAccount"]/input').send_keys("12345678901234567890")
        driver.find_element_by_xpath('//input[@id="add_bankName"]').send_keys("Sberbank")
        driver.find_element_by_xpath('//p-inputmask[@id="add_bic"]/input').send_keys("213546879")
        driver.find_element_by_xpath('//p-inputmask[@id="add_correspondentAccount"]/input').send_keys(
            "09876543210987654321")
        driver.find_elements_by_xpath('//button[@icon="fa-check"]')[0].click()
        time.sleep(2)
        driver.find_elements_by_xpath('//span[@class="ui-button-text ui-clickable"]')[1].click()
        time.sleep(2)
        driver.find_element_by_xpath('//p-dropdown[@id="add_addressType"]').click()
        driver.find_element_by_xpath('//div[@class="ui-dropdown-items-wrapper"]/ul/li[2]/span').click()
        driver.find_element_by_xpath('//p-dropdown[@id="addr_postcode"]').click()
        driver.find_element_by_xpath('//div[@class="ui-dropdown-items-wrapper"]/ul/li[2]/span').click()
        driver.find_element_by_xpath('//p-dropdown[@id="addr_country"]').click()
        driver.find_element_by_xpath('//div[@class="ui-dropdown-items-wrapper"]/ul/li[2]/span').click()
        driver.find_element_by_xpath('//p-dropdown[@id="addr_subjectRF"]').click()
        driver.find_element_by_xpath('//div[@class="ui-dropdown-items-wrapper"]/ul/li[2]/span').click()
        driver.find_element_by_xpath('//p-dropdown[@id="addr_city"]').click()
        driver.find_element_by_xpath('//div[@class="ui-dropdown-items-wrapper"]/ul/li[2]/span').click()
        driver.find_element_by_id('addrstreet').send_keys("Vasnecova")
        driver.find_element_by_id('addrhouse').send_keys("60")
        driver.find_element_by_id('addrbuilding').send_keys("2")
        driver.find_element_by_id('addrfloor').send_keys("5")
        driver.find_element_by_id('addrroom').send_keys("1")
        time.sleep(2)
        print(len(driver.find_elements_by_xpath('//button[@icon="fa-check"]')))
        driver.find_elements_by_xpath('//button[@icon="fa-check"]')[1].click()
        time.sleep(2)
        driver.find_elements_by_xpath('//span[@class="ui-button-text ui-clickable"]')[2].click()
        driver.find_element_by_xpath('//p-dropdown[@id="add_phoneType"]').click()
        driver.find_element_by_xpath('//div[@class="ui-dropdown-items-wrapper"]/ul/li[2]/span').click()
        driver.find_element_by_xpath('//p-dropdown[@id="add_country"]').click()
        driver.find_element_by_xpath('//div[@class="ui-dropdown-items-wrapper"]/ul/li[2]/span').click()
        driver.find_element_by_xpath('//p-inputmask[@id="add_number"]/input').send_keys("8585857484")
        driver.find_element_by_id('add_phoneextention').send_keys("80298076628")
        print(len(driver.find_elements_by_xpath('//button[@icon="fa-check"]')))
        driver.find_elements_by_xpath('//button[@icon="fa-check"]')[2].click()
        time.sleep(2)
        driver.find_elements_by_xpath('//span[@class="ui-button-text ui-clickable"]')[3].click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 0)")
        print(len(driver.find_elements_by_xpath('//button[@label="Редактировать"]')))
        driver.find_elements_by_xpath('//button[@label="Редактировать"]')[0].click()
        driver.find_element_by_xpath('//p-dropdown[@id="dropdown"]').click()
        driver.find_element_by_xpath('//div[@class="ui-dropdown-items-wrapper"]/ul/li[2]/span').click()
        driver.find_element_by_id('add_user__lastname').send_keys("Zubar")
        driver.find_element_by_id('add_user__firstname').send_keys("Aleksey")
        driver.find_element_by_id('add_user__secondname').send_keys("Olegovich")
        driver.find_element_by_xpath('//p-inputmask[@id="add_user_phone"]/input').send_keys("4225857684")
        driver.find_element_by_id('add_user_email').send_keys("lesha9515@gmail.com")
        driver.find_element_by_id('doc_type').send_keys("passport")
        driver.find_element_by_id('doc_name').send_keys("sadsdxsxsasxasxa")
        driver.find_element_by_xpath('//p-calendar[@id="dir1_bd"]/span/input').send_keys("07.08.2016")
        driver.find_element_by_id('doc_num').send_keys("1235468")
        print(len(driver.find_elements_by_xpath('//button[@icon="fa-check"]')))
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        driver.find_elements_by_xpath('//button[@icon="fa-check"]')[1].click()
        time.sleep(2)
        driver.find_elements_by_xpath('//button[@label="Продолжить"]')[0].click()


# ch = RegistrationSro1()
# ch.test()

if __name__ == '__main__':
    unittest.main(verbosity=2)





