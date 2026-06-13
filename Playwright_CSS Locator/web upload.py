from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome WebDriver with your path
chrome_service = Service(r'C:\Selenium driver\Chrome\chromedriver.exe')

# Launch Chrome browser
driver = webdriver.Chrome(service=chrome_service)

# Open the ALM login page
driver.get('https://alm11p.ta.philips.com/qcbin/start_a.jsp')

# Wait for login fields
wait = WebDriverWait(driver, 10)
login_name = wait.until(EC.presence_of_element_located((By.ID, 'loginName')))  # Replace with actual ID
password = driver.find_element(By.ID, 'password')

# Enter your credentials (replace with your actual code and password)
login_name.send_keys('320287287')
password.send_keys('Saymyname@123A')  # Be careful with hard-coded passwords

# Click on the Authenticate button
authenticate_button = driver.find_element(By.ID, 'Authenticate')  # Ensure correct ID
authenticate_button.click()

# Wait until the domain dropdown appears and select domain
domain_dropdown = wait.until(EC.presence_of_element_located((By.ID, 'domain')))  # Replace with actual ID
domain_dropdown.click()
domain_dropdown.find_element(By.XPATH, "//option[@value='IPF']").click()

# Select the project
project_dropdown = driver.find_element(By.ID, 'project')  # Replace with actual ID
project_dropdown.click()
project_dropdown.find_element(By.XPATH, "//option[@value='PF1_0']").click()

# Click the login or proceed button
login_button = driver.find_element(By.ID, 'login')  # Ensure correct ID
login_button.click()

# Wait for the next page to load or add more steps if needed
time.sleep(5)  # Adjust based on your app’s load time

# Close the browser when done
driver.quit()