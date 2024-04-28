from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Initialize Chrome driver using Selenium Manager
driver = webdriver.Chrome()

# Navigate to the login page
driver.get('https://mozi-login.alibaba-inc.com/ssoLogin.htm?APP_NAME=logistics-adminportal&BACK_URL=https%3A%2F%2Fwww.dazlogistics.com.bd%2F')

# Find the username and password fields and enter your credentials
username_field = driver.find_element('name', 'domainAccount')
password_field = driver.find_element('name', 'password')

# Enter your username and password
username_field.send_keys('')
password_field.send_keys('')

# Submit the login form by clicking the login button
login_button = driver.find_element('class name', 'sso-btn-submit')

login_button.click()

# Wait for the page to load after login (add more time if needed)
time.sleep(20)

# Now navigate to the page containing the form
driver.get('https://www.dazlogistics.com.bd/lop/fd/re-inbound-point?partnerCode=6b431c3f-b2bd-44b0-a96f-0a546ea4a220')

# Read data from Excel
data = pd.read_excel('E:/test.xlsx')

# Loop through data and input into form
for entry in data['Data']:
    # Find the text field by its componentkey attribute
    input_field = driver.find_element('name', 'trackingNumber')

   # Iterate over each row in the DataFrame and input text into the input field
for index, row in data.iterrows():
    text = row['Data']  # Assuming 'Data' is the column name in Excel
    input_field.send_keys(text)

    # Press the Enter key
    input_field.send_keys(Keys.ENTER)

    # Wait for some time before inputting the next data
    time.sleep(1)

# Close the browser
driver.quit()
