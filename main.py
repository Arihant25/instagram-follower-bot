from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

# Get the login credentials from the user
email = input("Enter your Instagram email/phone number/username:\n")
password = input("Enter your Instagram password:\n")
username = input(
    "Enter the username of the account whose followers you want to follow:\n")

CHROME_DRIVER_PATH = input(
    r"Enter the location of the Chrome Driver on your PC, for example - C:\Downloads\chromedriver.exe" + "\n")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(CHROME_DRIVER_PATH)

# Navigate to Instagram and login
driver.get("https://www.instagram.com/accounts/login/")
# Wait for the login page to load
sleep(3)
# Enter the email address
driver.find_element_by_xpath(
    '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(email)
# Enter the password
driver.find_element_by_xpath(
    '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
# Click the login button
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
# Wait for it to login
sleep(3)

# Go to the profile of the user whose profile you want to scrape
driver.get(f"https://www.instagram.com/{username}")

# Open the followers list
driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()

# Wait for the followers list to load
sleep(3)

while True:
    # Get the followers list
    followers = driver.find_elements_by_css_selector("li button")

    # Click on the follow button of each user in the list
    for follower in followers:
        try:
            # Follow each follower
            follower.click()
            # Wait for 3 seconds to avoid looking like a bot
            sleep(3)
        except ElementClickInterceptedException:
            # Click on the cancel button if the user is already being followed
            driver.find_element_by_xpath(
                '/html/body/div[6]/div/div/div/div[3]/button[2]').click()

    # Scroll down the page
    modal = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
    for i in range(10):
        driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        sleep(2)
