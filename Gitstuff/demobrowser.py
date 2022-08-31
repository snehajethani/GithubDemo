from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# service_object = Service("C:\\Users\\sachi\\Downloads\\chromedriver_win32\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_object)


service_object = Service("C:\\Users\\sachi\\Downloads\\edgedriver_win64\\msedgedriver.exe")
driver = webdriver.Edge(service=service_object)
driver.get("https://www.google.co.in/")
print(driver.title)
print(driver.current_url)
driver.close()