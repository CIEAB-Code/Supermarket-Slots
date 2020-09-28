import time
from selenium import webdriver
from tesco_login import Login
import argparse
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from driver_wait_altered import WebDriverWaitChange

parser = argparse.ArgumentParser(description="Check for available delivery slots on your Tesco's account")
parser.add_argument('-e', '--email', required=True, type=str, metavar='',
                    help="Enter your full email address to your Tesco's account")
parser.add_argument('-pw', '--password', required=True, type=str, metavar='', nargs='+',
                    help="Enter password to your Tesco's account.")
args = parser.parse_args()

email = args.email
password = args.password

print(email)
print(password)

browser = webdriver.Chrome()

# Login

login_page = Login(driver=browser)
login_page.go()

# login_page.email_input.find() # TEST
login_page.email_input.input_text(email)

# login_page.password_input.find() # TEST
login_page.password_input.input_text(password)

# login_page.sign_in_button.find() # TEST
login_page.sign_in_button.click()

# Check home delivery

# Get access to tabs for week 1-3
weeks_tab = login_page.home_week_tab.find_many()

# Week 1

all_week1_slots = browser.find_elements_by_xpath((
    "//button[@class='button button-secondary small available-slot--button']"))
available_slots_1 = []
for each_slot in all_week1_slots:
    if 'Between' in each_slot.text:
        available_slots_1.append(each_slot)

if len(available_slots_1) > 0:
    # Have to account for if slots disappears before you click or some other problem.
    available_slots_1[0].click()
    # text = available_slots_1[0].text
    # text = text.splitlines()
    # text = text[0]
    # slot = browser.find_element_by_xpath("//button/span[text()='%s']" %text)
    # slot.click()
else:
    weeks_tab[1].click()
    available_slots_2 = []
    all_week2_slots = browser.find_elements_by_xpath((
        "//button[@class='button button-secondary small available-slot--button']"))
    if len(available_slots_2) > 0:
        available_slots_2[0].click()
        # Have to account for if slots disappears before you click or some other problem.
        # text = available_slots_2[0].text
        # text = text.splitlines()
        # text = text[0]
        # slot = browser.find_element_by_xpath("//button/span[text()='%s']" % text)
        # slot.click()
    else:
        weeks_tab[2].click()
        available_slots_3 = []
        all_week3_slots = browser.find_elements_by_xpath((
            "//button[@class='button button-secondary small available-slot--button']"))
        if len(available_slots_3) > 0:
            # Have to account for if slots disappears before you click or some other problem.
            available_slots_3[0].click()
            # text = available_slots_3[0].text
            # text = text.splitlines()
            # text = text[0]
            # slot = browser.find_element_by_xpath("//button/span[text()='%s']" % text)
            # slot.click()


# #weeks_tab[0].click()
# # Make variable 'available_slot' out side of ifs/loops if one is available break loop and click on slot
# available_slots_1 = browser.find_elements_by_css_selector(
#     'button[class="button button-secondary small available-slot--button"]')
# # locate = (By.CSS_SELECTOR, 'button[class="button button-secondary small available-slot--button"]')
# # available_slots_1 = WebDriverWaitChange(browser, 5).until(
# #     EC.visibility_of_all_elements_located(locator=locate))
# if len(available_slots_1) <= 0:
#     weeks_tab[1].click()
#     available_slots_2 = browser.find_elements_by_css_selector(
#         'button[class="button button-secondary small available-slot--button"]')
#     if len(available_slots_2) > 0:
#         # Week 2 has slots
#         time.sleep(3)
#         available_slots_2[0].click()
#     elif len(available_slots_2) <= 0:
#         weeks_tab[2].click()
#         available_slots_3 = browser.find_elements_by_css_selector(
#             'button[class="button button-secondary small available-slot--button"]')
#         if len(available_slots_3 > 0):
#             # Week 3 has slots
#             available_slots_3[0].click()
#             slot = browser.find_element_by_xpath(("//button[@class='button button-secondary small available-slot--button']/span")[0])
#
#
# elif len(available_slots_1) > 0:
#     # Week 1 has slots


if __name__ == '__main__':
    email = args.email
    password = args.password
