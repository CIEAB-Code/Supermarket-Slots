from selenium import webdriver
from tesco_login import Login
import argparse
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

parser = argparse.ArgumentParser(description="Check for available delivery slots on your Tesco's account")
parser.add_argument('-e', '--email', required=True, type=str, metavar='',
                    help="Enter your full email address to your Tesco's account")
parser.add_argument('-pw', '--password', required=True, type=str, metavar='',  nargs='+',
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

#login_page.email_input.find() # TEST
login_page.email_input.input_text(email)

#login_page.password_input.find() # TEST
login_page.password_input.input_text(password)

#login_page.sign_in_button.find() # TEST
login_page.sign_in_button.click()

# Check home delivery

# Get access to tabs for week 1-3
weeks_tab = login_page.home_week_tab.find_many()

# Week 1
#weeks_tab[0].click()
# Make variable 'available_slot' out side of ifs/loops if one is available break loop and click on slot
available_slots_1 = browser.find_elements_by_css_selector(
    'button[class="button button-secondary small available-slot--button"]')
if len(available_slots_1) <= 0:
    weeks_tab[1].click()
    available_slots_2 = browser.find_elements_by_css_selector(
        'button[class="button button-secondary small available-slot--button"]')
    if len(available_slots_2) > 0:
        available_slots_2[0].click()
    elif len(available_slots_2) <= 0:
        weeks_tab[2].click()
        available_slots_3 = browser.find_elements_by_css_selector(
            'button[class="button button-secondary small available-slot--button"]')
        if len(available_slots_3 > 0):
            available_slots_3[0].click()

elif len(available_slots_1) > 0:
    available_slots_1[1].click()

if __name__ == '__main__':
    email = args.email
    password = args.password

    print(email)
    print(password)
