from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https:////training.qaonlinetraining.com/testPage.php")

driver.find_element(By.NAME, "bike").click()
driver.find_element(By.NAME, "car").click()
driver.find_element(By.NAME, "boat").click()
driver.find_element(By.NAME, "horse").click()

driver.find_element(By.NAME, "submit").click()
