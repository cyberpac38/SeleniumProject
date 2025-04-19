from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://tutorialspoint.com/selenium/practice/selenium_automation_practice.php")

driver.find_element(By.NAME,'name').send_keys("tutorialspoint")
driver.find_element(By.NAME,'email').send_keys("cyberpac38@gmail.com")
