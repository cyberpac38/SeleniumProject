
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.itlearn360.com/")
#driver.implicitly_wait(10)

wait = WebDriverWait(driver,10)

driver.find_element(By.NAME,'')
element=wait.until(Ec.presence_of_element_located(By.XPATH,'//*[@id="menu-item-42364"]/a/span'))

driver.find_element(By.NAME, 'log').send_keys("Demo12")
driver.find_element(By.NAME, 'pwd').send_keys("Test123456$")
driver.find_element(By.NAME, 'wp-submit').click()