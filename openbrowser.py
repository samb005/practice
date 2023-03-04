from selenium import webdriver
from selenium.webdriver.common.services imports Services
from selenium.webdriver.common.by imports By

serv_ob=Service("path of the chrome/firefox/edge driver")
driver=webdriver.Chrome(service=serv_ob)
url="www.google.com/"
driver.get(url)
driver.close()
