from selenium import webdriver
from tesco_login import Login
import argparse

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
else:
    weeks_tab[1].click()
    available_slots_2 = []
    all_week2_slots = browser.find_elements_by_xpath((
        "//button[@class='button button-secondary small available-slot--button']"))
    if len(available_slots_2) > 0:
        available_slots_2[0].click()
        # Have to account for if slots disappears before you click or some other problem.
    else:
        weeks_tab[2].click()
        available_slots_3 = []
        all_week3_slots = browser.find_elements_by_xpath((
            "//button[@class='button button-secondary small available-slot--button']"))
        if len(available_slots_3) > 0:
            # Have to account for if slots disappears before you click or some other problem.
            available_slots_3[0].click()


if __name__ == '__main__':
    email = args.email
    password = args.password
