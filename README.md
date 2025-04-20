# Selenium Chrome Test: Validate Installation and Basic Setup

This repository contains a basic Selenium test script written in Python. This test aims to validate that Selenium is installed correctly, ChromeDriver is configured properly, and the automation setup works as expected by simply opening a website.

## 📌 Objective

To open a target website using Selenium and Google Chrome, ensuring:
- Selenium is installed and importable.
- ChromeDriver is accessible and functional.
- The browser opens and stays open using Chrome options (specifically, the `detach` option).

---

## ✅ Requirements

Before running this test, ensure the following are installed on your system:

- Python 3.7+
- Google Chrome browser
- ChromeDriver (version must match the installed Chrome browser)
- Selenium Python package

### Install Selenium
```bash
pip install selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set Chrome options to keep the browser open
options = Options()
options.add_experimental_option("detach", True)

# Initialize the Chrome WebDriver with options
driver = webdriver.Chrome(options=options)

# Open the website
driver.get("https://demo.itle360.com")

⚙️ How It Works
Options() object is used to set Chrome configurations.

The detach option is set to True, which keeps the browser open after the script finishes execution.

webdriver.Chrome() initializes the Chrome browser instance.

get() method loads the provided website URL.

🚫 Common Issue: Browser Closes Immediately
By default, Selenium closes the browser as soon as the script ends. This is solved by using:

python
Copy
Edit
options.add_experimental_option("detach", True)
This keeps the browser open after execution so you can visually verify the automation result.

📎 Notes
You can reuse this script as a boilerplate for any future Selenium test.

Only the URL in driver.get() needs to be changed for different test cases.

ChromeDriver must be added to your system’s PATH or specify its path in webdriver.Chrome(executable_path="...")
