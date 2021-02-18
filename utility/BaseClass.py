import pytest
import inspect
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("Setup") # identify the fixture to execute first and then go for test
class BaseClass:

    def getLoggerInfo(self):
        log=loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(__name__)  # which test case run that name of log file or this statement will capture testcase name
        fileHandler = logging.FileHandler('LogFile.log')  # this statement know where the file want ot store or directed
        formater = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : %(message)s")  # Format to print messagelike this
        # 01-02-2021 : 01:02:22 : error : testcasename : file exute error
        fileHandler.setFormatter(formater)  # connection of logger to format
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def VerifyLinkPresence(self,text):
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

