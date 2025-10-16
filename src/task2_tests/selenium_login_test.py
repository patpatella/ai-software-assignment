# src/task2_tests/selenium_login_test.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

def run_tests():
    # point to your local file
    file_path = "file://" + os.path.abspath("login_page.html")
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # run headless for CI
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(file_path)
    time.sleep(0.5)

    # valid credentials
    driver.find_element(By.ID, "username").send_keys("user1")
    driver.find_element(By.ID, "password").send_keys("pass1")
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(0.3)
    msg = driver.find_element(By.ID, "message").text
    print("Valid login message:", msg)
    assert "success" in msg.lower()

    # invalid credentials
    driver.refresh()
    time.sleep(0.3)
    driver.find_element(By.ID, "username").send_keys("wrong")
    driver.find_element(By.ID, "password").send_keys("wrong")
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(0.3)
    msg2 = driver.find_element(By.ID, "message").text
    print("Invalid login message:", msg2)
    assert "failed" in msg2.lower()

    # take screenshot
    screenshot_path = os.path.join("screenshots", "login_test_result.png")
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot(screenshot_path)
    print("Saved screenshot:", screenshot_path)

    driver.quit()

if __name__ == "__main__":
    run_tests()
