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
driver.get('https://thehub.group.atlascopco.com/teams/TOO_NACKA/RD/SitePages/Total%20workstation%20Integration%20lab.aspx')
driver2 = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)
driver2.maximize_window()

##### Find broken links 
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    r = elem.get_attribute("href")

    if "http://" in r or "https://" in r:
        try:
            driver2.get(r)
            try:
                try:
                    driver2.find_element_by_xpath("""//*[@id="main-message"]/h1""")
                    print(r + "broken link (This site cant't be reached)")
                except:
                    driver2.find_element_by_xpath("/html/body/h1")
                    print(r + "broken link (DNS ERROR)")
            except:
                pass#print("######" + r)#pass  # print("link works")  # pass#print("link works")
        except:
            pass  # print(r + "  broken link")
    else:
        pass  # print("not a link " + r)



##### Closes everything
driver2.close()
time.sleep(3)
driver.close()