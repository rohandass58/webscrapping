import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# Get the current script directory
script_directory = os.path.dirname(os.path.realpath(__file__))

# Path to your Chrome profile (if needed)
chrome_profile_path = "/home/rohan/.config/google-chrome/Profile 1"

# Specify the path to the ChromeDriver executable
chromedriver_path = "/usr/bin/chromedriver"

# Selenium options for Chrome
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
)

# Create a new instance of the Chrome driver with the specified options, service, and executable path
driver = webdriver.Chrome(
    service=ChromeService(executable_path=chromedriver_path),
    options=chrome_options,
)

print("Driver initialized successfully")

try:
    # Go to the website
    driver.get("https://bot.sannysoft.com")

    # Simulate mouse movement
    actions = ActionChains(driver)
    actions.move_by_offset(10, 20).perform()
    time.sleep(1)
    print("Simulate mouse movement")

    # Scroll down the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    print("Scroll down the page")

    # Scroll up the page
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)
    print("Scroll up the page")

    # Add any additional actions or waits that mimic human behavior
    # ...

    # Take screenshot and save it in the same folder
    screenshot_path = os.path.join(script_directory, f"screenshot.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")

finally:
    # Close the driver
    driver.quit()
