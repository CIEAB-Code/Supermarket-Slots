from selenium import webdriver
from tesco_login import Login
import argparse
from notify_run import Notify
import winsound

# Setting up variable fo notify_run to send notification message to registered phone
notify = Notify()

# Parser to receive email and password input from user from command line
parser = argparse.ArgumentParser(description="Check for available delivery slots on your Tesco's account")
parser.add_argument('-e', '--email', required=True, type=str, metavar='',
                    help="Enter your full email address to your Tesco's account")
parser.add_argument('-pw', '--password', required=True, type=str, metavar='', nargs='+',
                    help="Enter password to your Tesco's account.")
args = parser.parse_args()

email = args.email
password = args.password

# Chrome browser
browser = webdriver.Chrome()

# Login
login_page = Login(driver=browser)
login_page.go()

login_page.email_input.input_text(email)

login_page.password_input.input_text(password)

login_page.sign_in_button.click()

# Check home delivery
# Get access to tabs for week 1-3
weeks_tab = login_page.home_week_tab.find_many()

# All weeks

def check_available():
    # Function to check for available slots
    all_slots = browser.find_elements_by_xpath((
        "//button[@class='button button-secondary small available-slot--button']"))
    available_slots = []
    for each_slot in all_slots:
        if 'Between' in each_slot.text:
            available_slots.append(each_slot)

    return available_slots


def send_notification():
    # Fuction for sending notification when a slot is reserved
    notification = "Delivery slot reserved!"
    notify.send(notification)
    winsound.Beep(440, 1000)


week1_slots = check_available()
if len(week1_slots) > 0:
    week1_slots[0].click()
    send_notification()
else:
    # Check week 2 slots
    weeks_tab[1].click()
    week2_slots = check_available()
    if len(week2_slots) > 0:
        week2_slots[0].click()
        send_notification()
    else:
        # Check week 3 slots
        weeks_tab[2].click()
        week3_slots = check_available()
        if len(week3_slots) > 0:
            week3_slots[0].click()
            send_notification()

browser.quit()

if __name__ == '__main__':
    email = args.email
    password = args.password
