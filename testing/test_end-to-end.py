from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from settings import URL


# --- Start browser (Chrome or Firefox depending on what's installed) ---
# You may use Firefox if ChromeDriver isn't installed
try:
    driver = webdriver.Chrome()
except Exception:
    driver = webdriver.Firefox()

# --- Load the page ---
driver.get(URL)
time.sleep(1)  # let the page render

# --- Select factorial radio ---
factorial_radio = driver.find_element(By.CSS_SELECTOR, 'input[value="factorial"]')
factorial_radio.click()
time.sleep(2)

# --- Input number ---
number_input = driver.find_element(By.NAME, "number")
number_input.clear()
number_input.send_keys("5")
time.sleep(2)

# --- Submit the form ---
button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
button.click()

time.sleep(1)  # wait for response

# --- Check result ---
result = driver.find_element(By.CLASS_NAME, "result").text
print("Result text:", result)

if "Factorial of 5 is 120" in result:
    print("✅ Test passed")
else:
    print("❌ Test failed")

# --- Cleanup ---
driver.quit()
