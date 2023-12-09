import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Get the current script directory
script_directory = os.path.dirname(os.path.realpath(__file__))

# Path to your Firefox profile
firefox_profile_path = "/home/rohan/snap/firefox/common/.mozilla/firefox/jhm3yqh4.roman"

# Specify the path to the GeckoDriver executable
geckodriver_path = "/snap/bin/geckodriver"

# Create a FirefoxProfile instance
firefox_profile = webdriver.FirefoxProfile(firefox_profile_path)

# Set a custom user agent
options = Options()
options.headless = True  # Run Firefox in headless mode
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)
options.add_argument("--window-size=1366,768")
options.profile = firefox_profile

# Disable image loading
firefox_profile.set_preference("permissions.default.image", 2)

# Create a new instance of the Firefox driver with the specified profile, options, and executable path
driver = webdriver.Firefox(
    service=Service(executable_path=geckodriver_path),
    options=options,
)
print("Driver initialized successfully")

# Maximum allowed instances of bot detection
max_bot_detection_instances = 3

# Counter for bot detection instances
bot_detection_count = 0

try:
    while bot_detection_count < max_bot_detection_instances:
        # Go to the website
        driver.get("https://bot.sannysoft.com")

        # Inject JavaScript to set navigator.webdriver to false
        driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )

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

        # Check if bot detection occurred (you need to replace this condition with the actual detection mechanism)
        if "red-highlight" in driver.page_source:
            print("Bot detection instance detected!")
            bot_detection_count += 1

        # Add any additional actions or waits that mimic human behavior
        # ...

        # Take screenshot and save it in the same folder
        screenshot_path = os.path.join(
            script_directory, f"screenshot_{bot_detection_count}.png"
        )
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")

finally:
    # Close the driver
    driver.quit()
