from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service("C:\\Users\\sachi\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.implicitly_wait(2)

driver.get("https:/the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windows_opened = driver.window_handles
driver.switch_to.window(windows_opened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)

driver.switch_to.window(windows_opened[0])
print(driver.find_element(By.TAG_NAME,"h3").text)

driver.switch_to.window(windows_opened[0])
print(driver.find_element(By.TAG_NAME,"h3").text)


driver.get("https:/the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windows_opened = driver.window_handles
driver.switch_to.window(windows_opened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)

driver.switch_to.window(windows_opened[0])
print(driver.find_element(By.TAG_NAME,"h3").text)

driver.switch_to.window(windows_opened[0])
print(driver.find_element(By.TAG_NAME,"h3").text)