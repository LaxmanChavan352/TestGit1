from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):
        self.driver=driver


    shop = (By.XPATH, "//a[text()='Shop']")


    submit=(By.CSS_SELECTOR,"input[type='submit']")

    def itemInHome(self):
        return self.driver.find_element(*Homepage.shop) # here this method return driver object we need to catch it thats way we craete a constructor