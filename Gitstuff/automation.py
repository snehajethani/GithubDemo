from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service("C:\\Users\\sachi\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)


# service_object = Service("C:\\Users\\sachi\\Downloads\\edgedriver_win64\\msedgedriver.exe")
# driver = webdriver.Edge(service=service_object)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute('value') == 'option2':
        checkbox.click()
        assert checkbox.is_selected()
        break


for checkbox in checkboxes:
    if checkbox.get_attribute('value') == 'option2':
        checkbox.click()
        assert checkbox.is_selected()
        break