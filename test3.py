from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
dir_path = os.path.dirname(os.path.realpath(__file__))
chromedriver = dir_path + "/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
data = pd.read_excel("C:/Users/TOOanau/PycharmProjects/SeleniumServiAidInfo/equipment-leader-info.xlsx")

def GetInfo(ArticleNumber):
    xpath = ['//*[@id="main-navigationbar"]/ul/li[1]', '//*[@id="main-navigationbar"]/ul/li[2]',
             '//*[@id="main-navigationbar"]/ul/li[3]', '//*[@id="main-navigationbar"]/ul/li[4]']
    value = []
    x = 0

    driver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)
    driver.get("https://servaid.atlascopco.com/AssertWeb/en-US/AtlasCopco/Catalogue/1")
    driver.maximize_window()

    try:
        search = driver.find_element_by_xpath('/html/body/div/nav[1]/ul/li[1]/div/div/div/input')
        search.send_keys(ArticleNumber)#"4220437503")  # "8433 0564 38")#"4211603085 ")#""4220437503")#"4220 4375 03 ")#"4222 0443 00")#"8433 0564 39")#"8433 0564 38")
        time.sleep(5) #What to search
        driver.find_element_by_xpath("/html/body/div/section[4]/section/section/div[2]/ul[1]/li/a/div").click()
    except:
        pass

    time.sleep(2)
    while x < 4:  ########### Range is better
        print(x)
        try:
            value.append(driver.find_element_by_xpath(xpath[x]).get_attribute("title"))

        except:
            pass
        #print(value)
        x = x + 1

    try: InfoLink = driver.current_url
    except: InfoLink = ''
    try: ImageLink = driver.find_element_by_xpath('/html/body/div/section[4]/div/section/div/section[2]/div/section/div/section[2]/section/img').get_attribute('src')
    except: ImageLink = ''
    try: group = value[1]
    except: group = ''
    try: TYPE = value[len(value)-1]
    except: TYPE = ''

    #print(group)
    print(Name + "\n" + InfoLink + "\n" + ImageLink + "\n" + group + "\n" + TYPE)

    time.sleep(2)
    driver.close()
    return


#"8433 0564 38" "4211603085 " "4220437503" "4220 4375 03" "4222 0443 00" "8433 0564 39" "8433 0564 38"

EquipmentName = ""
ArticleNumber = data['Article Number']
SerialNumber = ""
for x in ArticleNumber: GetInfo(x)