from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.Google.com/")

driver.switch_to.new_window()
driver.get("https://www.itlearn360.com/demo-course/")
number_tab=len(driver.window_handles)
print(number_tab)

tab_value=driver.window_handles
print(tab_value)

current_tab=driver.current_window_handle
print(current_tab)

driver.find_element(By.XPATH,'//*[@id="menu-item-42162"]/a/span').click()

first_tab=tab_value[0]

if current_tab!= first_tab:
    driver.switch_to.window(first_tab)

driver.find_element(By.LINK_TEXT, "Gmail").click()