# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageObject(object):
    """A base class for all page objects.
    Attributes:
        driver: The Parakeetdriver instance.
    """

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator_type, locator_value, wait_element=False):
        if (wait_element):
            try:
                elemento = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator_type, locator_value )))
            finally:
                pass
        else:
            try:
                elemento = self.driver.find_element(locator_type, locator_value)
            finally:
                pass
        return elemento