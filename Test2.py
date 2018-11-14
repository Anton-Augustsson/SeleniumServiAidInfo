from selenium import webdriver
import time
import os

profile = {"download.default_directory": "NUL", "download.prompt_for_download": False, }
dir_path = os.path.dirname(os.path.realpath(__file__))
chromedriver = dir_path + "/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver


##### Webdriver options
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option("prefs", profile)
options.add_argument("user-data-dir= <full local path Google Chrome user data default folder>")

driver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)
driver.get("https://thehub.group.atlascopco.com/teams/TOO_NACKA/RD/SitePages/Solution%20Verification%20Collaboration%20page.aspx")

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.send_keys("TOOanau")
password.send_keys("June@2018")


time.sleep(3)
driver.close()
