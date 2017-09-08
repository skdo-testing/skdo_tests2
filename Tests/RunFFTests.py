from selenium import webdriver

class RunFFTests():

    def test(self):
        # Instantiate FF Browser Command
        driver = webdriver.Firefox()
        # Open the provided URL
        driver.get("http://94.130.75.130")

ff = RunFFTests()
ff.test()