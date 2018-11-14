##### Modulers
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time


##### Veribles
profile = {"download.default_directory": "NUL", "download.prompt_for_download": False, }
dir_path = os.path.dirname(os.path.realpath(__file__))
chromedriver = dir_path + "/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver


##### Webdriver options
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option("prefs", profile)


##### Webdriver
driver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)
#driver.get("https://sharepoint.stackexchange.com/questions/34423/sharepoint-lists-vs-sharepoint-libraries") # good link
#driver.get("http://10.46.28.169dsgfdhsgjrtjrtgfhrdgdfhgfdynmymhgdjytfhdgf.com/") # dns error broken link
#driver.get("http://someradomlinktosomewareidontknow/") # This site cant't be reached broken link
#r = "http://someradomlinktosomewareidontknow/"
r = "https://servaid.atlascopco.com/AssertWeb/en-US/AtlasCopco/Catalogue/12810"
driver.get(r)
value = driver.find_elements_by_xpath('//div[@class="presentation-name-container"]/h2').get_attribute('class')
print(value)
driver.close()