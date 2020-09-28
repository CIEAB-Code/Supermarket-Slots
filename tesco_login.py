from selenium.webdriver.common.by import By
from base_element import BaseElement
from base_page import BasePage


class Login(BasePage):

    # Login

    url = 'https://www.tesco.com/groceries/en-GB/slots/delivery'

    @property
    def email_input(self):
        locator = (By.CSS_SELECTOR, 'input#username')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def password_input(self):
        locator = (By.CSS_SELECTOR, 'input#password')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def sign_in_button(self):
        locator = (By.CSS_SELECTOR, 'button[class="ui-component__button"]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    # Home Delivery
    @property
    def no_slot_message(self):
        locator = (By.CSS_SELECTOR, 'p[class="sc-AxiKw sc-oVpqz jydMzo no-slot-msg--delivery"]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def available_slots(self):
        locator = (By.CSS_SELECTOR, 'button[class="button button-secondary small available-slot--button"]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def home_week_tab(self):
        locator = (By.CSS_SELECTOR, 'a[class="slot-selector--week-tabheader-link"]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])
