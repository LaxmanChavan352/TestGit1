from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver=driver
    SelectCountry = (By.ID, "country")
    country=(By.LINK_TEXT,"India")
    def getCountries(self):
        return self.driver.find_element(*ConfirmPage.SelectCountry)
    def getAppropriateCountry(self):
        return self.driver.find_element(*ConfirmPage.country)