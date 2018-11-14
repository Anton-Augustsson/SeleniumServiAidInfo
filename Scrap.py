
####################################################################################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
import os
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
dir_path = os.path.dirname(os.path.realpath(__file__))
chromedriver = dir_path + "/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)
time.sleep(5)
driver.close()
######################################################################################################################
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors')
#options.add_argument('--ignore-ssl-errors')
dir_path = os.path.dirname(os.path.realpath(__file__))
chromedriver = dir_path + "/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)
WriteCredentials = driver.get('https://thehub.group.atlascopco.com/teams/TOO_NACKA/RD/SitePages/Solution%20verification%20internal.aspx')

'''''
time.sleep(1)
WriteCredentials.send_keys("TOOanau")
WriteCredentials.send_keys(Keys.TAB)
WriteCredentials.send_keys("June@2018")
time.sleep(1)
WriteCredentials.send_keys(Keys.ENTER)
time.sleep(1)
'''''

links = driver.find_elements_by_css_selector("a")
for link in links:
    r = requests.head(link.get_attribute('href'))
    print(link.get_attribute('href'), r.status_code)

#######################################################################################################################
from sharepoint import SharePointSite, basic_auth_opener
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

server_url = "https://thehub.group.atlascopco.com/"
site_url = server_url + "teams/TOO_NACKA/RD/SitePages/Solution%20verification%20internal.aspx"

opener = basic_auth_opener(server_url, "TOOau", "June@20")#"TOOanau", "June@2018")

site = SharePointSite(site_url, opener)
site.as_xml()
'''''
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
dir_path = os.path.dirname(os.path.realpath(__file__))
chromedriver = dir_path + "/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)
driver.get(site)
time.sleep(2)
driver.close()
'''''
#######################################################################################################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
dir_path = os.path.dirname(os.path.realpath(__file__))
chromedriver = dir_path + "/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)
driver.get("https://servaid.atlascopco.com/AssertWeb/en-US/AtlasCopco/Catalogue/1")
driver.maximize_window()

search = driver.find_element_by_xpath('/html/body/div/nav[1]/ul/li[1]/div/div/div/input')
search.send_keys("8433 0564 38")
time.sleep(1)
search.send_keys(Keys.ENTER)
time.sleep(1)
search.send_keys(Keys.ENTER)
#search.send_keys(u'\ue007') #send_keys(Keys.RETURN)#driver.find_element_by_class_name("quick-search-textbox").send_keys("8433 0564 38").send_keys(Keys.RETURN)
time.sleep(6)
driver.close()

#######################################################################################################################

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
URL='https://thehub.group.atlascopco.com/teams/TOO_NACKA/RD/Lists/Equipment/NewForm.aspx?Source=https%3A%2F%2Fthehub%2Egroup%2Eatlascopco%2Ecom%2Fteams%2FTOO_NACKA%2FRD%2FSitePages%2FSSV%2520Equipment%2520lending%2Easpx&RootFolder='
XPATH1="""//*[@id="Title_fa564e0f-0c70-4ab9-b863-0177e6ddd247_$TextField"]"""
XPATH2="""//*[@id="ctl00_ctl45_g_f6aeff94_31ce_41db_a4a9_87121dfd45e0_ctl00_toolBarTbl_RightRptControls_ctl00_ctl00_diidIOSaveItem"]"""
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
dir_path = os.path.dirname(os.path.realpath(__file__))
chromedriver = dir_path + "/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)
WriteCredentials = driver.get(URL)
w = driver.find_element_by_xpath(XPATH1)
w.send_keys("This Was Writen automatically")
driver.find_element_by_xpath(XPATH2).click()

time.sleep(4)
driver.get(URL)
time.sleep(4)
driver.close()
print("How on earth did this work")


#######################################################################################################################


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
driver2 = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)
driver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)
driver.get('https://thehub.group.atlascopco.com/teams/TOO_NACKA/RD/SitePages/Solution%20verification%20internal.aspx')


##### Find broken links
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    r1 = elem.get_attribute("href")
    r = requests.head(r1)#elem.get_attribute("href"))


    if r1.find("https://"):#sr.find("https://"):
        print("not a link " + r1)  #pass
    else:
        try:
            print(r.status_code)#driver2.get(r)
        except:
            print(r1 + " status failed")#"  broken link")



##### Closes everything
driver2.close()
time.sleep(3)
driver.close()

########################################################################################################################

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
driver2 = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)
driver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)
driver.get(
    'https://thehub.group.atlascopco.com/teams/TOO_NACKA/RD/SitePages/Total%20workstation%20Integration%20lab.aspx')

##### Find broken links
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    r = elem.get_attribute("href")

    if "http://" in r or "https://" in r:
        try:
            driver2.get(r)
            time.sleep(0.5)
            try:
                try:
                    driver.find_element_by_xpath("""//*[@id="main-message"]/h1""")
                    print("broken link (This site cant't be reached)")
                except:
                    driver.find_element_by_xpath("/html/body/h1")
                    print("broken link (DNS ERROR)")
            except:
                print("######" + r)  # pass  # print("link works")  # pass#print("link works")
        except:
            pass  # print(r + "  broken link")
    else:
        pass  # print("not a link " + r)

##### Closes everything
driver2.close()
time.sleep(3)
driver.close()

################################################################################################################