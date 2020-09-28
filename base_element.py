from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(object):

    def __init__(self, driver, value, by):
        self.driver = driver
        self.value = value
        self.by = by
        self.locator = (self.by, self.value)

        self.web_element = None
        #self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def find_many(self):
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(locator=self.locator))
        self.web_element = elements
        return elements

    def find_all_presence(self):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator=self.locator))
        self.web_element = elements
        return elements

    def input_text(self, txt):
        self.find() #TEST
        self.web_element.send_keys(txt)
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    @property
    def text(self):
        self.find() #TEST
        text = self.web_element.text
        return text
