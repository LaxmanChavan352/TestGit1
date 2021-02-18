from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import inspect
import logging

from PageObjectMexhanishm.CheckOutPage import CheckOut
from PageObjectMexhanishm.ConfirmPage import ConfirmPage
from PageObjectMexhanishm.Homepage import Homepage
from utility.BaseClass import BaseClass


class TestProjectEndToEnd(BaseClass):
    def test_endToEndP(self):
        log=self.getLoggerInfo()
        homepage=Homepage(self.driver) # Object created
        homepage.itemInHome().click()
        checkOut=CheckOut(self.driver)
        log.info("getting card title")
        carts=checkOut.getCardTitles()
        i=-1
        for card in carts:
            i=i+1
            cardText=card.text
            log.info(cardText)
            if cardText=="Blackberry":
                checkOut.getCardFooter()[i].click()



        check=checkOut.clickCheckOut()
        check.click()
        checkOut.ConfirmCheckOutButton().click()
        confirmPage=ConfirmPage(self.driver)
        log.info("Entering country name")
        confirmPage.getCountries().send_keys("Ind")
        self.VerifyLinkPresence("India")
        confirmPage.getAppropriateCountry().click()
        self.driver.find_element_by_css_selector("label[for=checkbox2]").click()
        self.driver.find_element_by_css_selector("input[type='submit']").click()
        ValidateText = self.driver.find_element_by_css_selector("div[class*='alert-success']").text
        log.info("Textreciving from application"+ValidateText)
        assert "Success! Thank you!" in ValidateText

        self.driver.get_screenshot_as_file("Snap.png")
