import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as SeleniumWebDriverwait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_login_to_itlearn360(driver):
    driver.get("https://www.itlearn360.com/")
    import selenium.webdriver.support.ui as ui
    wait = ui.WebDriverWait(driver, 10)

    # Wait for and click the login menu item
    login_menu = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="menu-item-42364"]/a/span')))
    login_menu.click()

    # Wait for and fill the login form
    wait.until(EC.presence_of_element_located((By.NAME, 'log'))).send_keys("Demo12")
    driver.find_element(By.NAME, 'pwd').send_keys("Test123456$")
    driver.find_element(By.NAME, 'wp-submit').click()

