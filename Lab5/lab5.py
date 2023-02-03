from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json

service=Service('C:\PW\WstDoPythona\lab5\chromedriver_win32\chromedriver.exe')
driver=webdriver.Chrome(service=service)
driver.get('https://www.youtube.com/@scifun/videos')
button=driver.find_element(By.CSS_SELECTOR,'#yDmH0d > c-wiz > div > div > div > div.NIoIEf > div.G4njw > div.qqtRac > div.VtwTSb > form:nth-child(2) > div > div > button')
button.click()
time.sleep(2)
films=[]
for _ in range(35):
    elements=driver.find_elements(By.CSS_SELECTOR,'h3, ytd-video-meta-block span')
    #elements2=driver.find_elements(By.CSS_SELECTOR,'ytd-video-meta-block span')
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
for element in elements:
    films.append(element.text)
    #print(element.text)
time.sleep(1)
with open('abc.json','w',encoding='utf-8') as f:
    json.dump(films,f,ensure_ascii=False)
driver.close()