# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://i.skdo.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled(self):
        driver = self.driver
        driver.get(self.base_url + "/#/add/reg_main")
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("+7(282) 838-28-28")
        driver.find_element_by_id("add_user__password").clear()
        driver.find_element_by_id("add_user__password").send_keys("99999999")
        driver.find_element_by_id("add_user__lastname").clear()
        driver.find_element_by_id("add_user__lastname").send_keys(u"фам1")
        driver.find_element_by_id("add_user__firstname").clear()
        driver.find_element_by_id("add_user__firstname").send_keys(u"имя1")
        driver.find_element_by_id("add_user__secondname").clear()
        driver.find_element_by_id("add_user__secondname").send_keys(u"отч1")
        driver.find_element_by_id("add_user_email").clear()
        driver.find_element_by_id("add_user_email").send_keys("asasa@skdo.ru")
        driver.find_element_by_xpath("//p-dropdown[@id='add_user__roles']/div/div[2]/span").click()
        driver.find_element_by_xpath("//p-dropdown[@id='add_user__roles']/div/div[3]/div/ul/li[2]/span").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//p-dropdown[@id='dropdown']/div/div[2]/span").click()
        driver.find_element_by_xpath("//p-dropdown[@id='dropdown']/div/div[3]/div/ul/li[2]/span").click()
        driver.find_element_by_id("add_full_orgName").clear()
        driver.find_element_by_id("add_full_orgName").send_keys(u"ООО \"Рога и копыта\"")
        driver.find_element_by_id("add_orgName").clear()
        driver.find_element_by_id("add_orgName").send_keys(u"Рога и копыта")
        driver.find_element_by_xpath("(//input[@type='text'])[4]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys("22222 22222")
        driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys("222222222")
        driver.find_element_by_xpath("(//input[@type='text'])[6]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys("22222 2222 2222")
        Select(driver.find_element_by_css_selector("select.ui-datepicker-year.ng-tns-c9-5")).select_by_visible_text(
            "2003")
        driver.find_element_by_link_text("4").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//p-dropdown[@id='add_accountType']/div/label").click()
        driver.find_element_by_xpath("//p-dropdown[@id='add_accountType']/div/div[3]/div/ul/li[2]/span").click()
        driver.find_element_by_xpath("(//input[@type='text'])[9]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[9]").send_keys("33333 33333 33333 33333")
        driver.find_element_by_id("add_bankName").clear()
        driver.find_element_by_id("add_bankName").send_keys(u"Банк1")
        driver.find_element_by_xpath("(//input[@type='text'])[11]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[11]").send_keys("333333333")
        driver.find_element_by_xpath("(//input[@type='text'])[12]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[12]").send_keys("33333 33333 33333 33333")
        driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_xpath("//p-dropdown[@id='add_addressType']/div/label").click()
        driver.find_element_by_xpath("//p-dropdown[@id='add_addressType']/div/div[3]/div/ul/li[2]/span").click()
        driver.find_element_by_xpath("//p-dropdown[@id='addr_postcode']/div/label").click()
        driver.find_element_by_xpath("//p-dropdown[@id='addr_postcode']/div/div[3]/div[2]/ul/li[3]").click()
        driver.find_element_by_xpath("//p-dropdown[@id='addr_country']/div/label").click()
        driver.find_element_by_xpath("//p-dropdown[@id='addr_country']/div/div[3]/div/ul/li[2]/span").click()
        driver.find_element_by_xpath("//p-dropdown[@id='addr_subjectRF']/div/label").click()
        driver.find_element_by_xpath("//p-dropdown[@id='addr_subjectRF']/div/div[3]/div[2]/ul/li[4]/span").click()
        driver.find_element_by_xpath("//p-dropdown[@id='addr_city']/div/label").click()
        driver.find_element_by_xpath("//p-dropdown[@id='addr_city']/div/label").click()
        driver.find_element_by_xpath("//p-dropdown[@id='addr_city']/div/label").click()
        driver.find_element_by_xpath("//p-dropdown[@id='addr_city']/div/div[3]/div[2]/ul/li[3]/span").click()
        driver.find_element_by_id("addrstreet").clear()
        driver.find_element_by_id("addrstreet").send_keys(u"Улица1")
        driver.find_element_by_id("addrhouse").clear()
        driver.find_element_by_id("addrhouse").send_keys("22")
        driver.find_element_by_id("addrbuilding").clear()
        driver.find_element_by_id("addrbuilding").send_keys("222")
        driver.find_element_by_id("addrfloor").clear()
        driver.find_element_by_id("addrfloor").send_keys("3")
        driver.find_element_by_id("addrroom").clear()
        driver.find_element_by_id("addrroom").send_keys(u"Офис1")
        driver.find_element_by_xpath("(//button[@type='button'])[8]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        driver.find_element_by_xpath("//p-dropdown[@id='add_phoneType']/div/label").click()
        driver.find_element_by_xpath("//p-dropdown[@id='add_phoneType']/div/div[3]/div/ul/li[2]/span").click()
        driver.find_element_by_xpath("//p-dropdown[@id='add_country']/div/label").click()
        driver.find_element_by_xpath("//p-dropdown[@id='add_country']/div/div[3]/div/ul/li[2]/span").click()
        driver.find_element_by_xpath("(//input[@type='text'])[28]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[28]").send_keys("+7(234) 322-42-34")
        driver.find_element_by_xpath("(//button[@type='button'])[11]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//p-dropdown[@id='dropdown']/div/label").click()
        driver.find_element_by_xpath("//p-dropdown[@id='dropdown']/div/div[3]/div/ul/li[2]/span").click()
        driver.find_element_by_id("add_user__lastname").clear()
        driver.find_element_by_id("add_user__lastname").send_keys(u"Орда")
        driver.find_element_by_id("add_user__firstname").clear()
        driver.find_element_by_id("add_user__firstname").send_keys(u"Имя22")
        driver.find_element_by_xpath("(//input[@type='text'])[10]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[10]").send_keys("+7(422) 545-45-44")
        driver.find_element_by_id("add_user_email").clear()
        driver.find_element_by_id("add_user_email").send_keys("sdfd@skdo.ru")
        driver.find_element_by_id("doc_type").clear()
        driver.find_element_by_id("doc_type").send_keys(u"дока11")
        driver.find_element_by_id("doc_name").clear()
        driver.find_element_by_id("doc_name").send_keys(u"Дока222")
        driver.find_element_by_id("doc_num").clear()
        driver.find_element_by_id("doc_num").send_keys("34235235")
        Select(driver.find_element_by_css_selector("select.ui-datepicker-year.ng-tns-c9-22")).select_by_visible_text(
            "2007")
        driver.find_element_by_link_text("12").click()
        driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
