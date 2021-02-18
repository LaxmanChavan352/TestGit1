from selenium.webdriver.common.by import By


class CheckOut:

    def __init__(self,driver):
        self.driver=driver
    CardTitle=(By.CSS_SELECTOR, ".card-title a")
    CardFooter=(By.CSS_SELECTOR, ".card-footer button")
    CheckoutButton=(By.CSS_SELECTOR,"a[class='nav-link btn btn-primary']")
    ConfirmCheckOut=(By.CSS_SELECTOR,"button[class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOut.CardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOut.CardFooter)

    def clickCheckOut(self):
        return self.driver.find_element(*CheckOut.CheckoutButton)
    def ConfirmCheckOutButton(self):
        return self.driver.find_element(*CheckOut.ConfirmCheckOut)
