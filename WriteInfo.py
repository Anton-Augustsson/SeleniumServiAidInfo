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
