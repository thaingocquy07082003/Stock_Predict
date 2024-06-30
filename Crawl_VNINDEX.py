import numpy as np
from selenium import webdriver 
from time import sleep
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
# from webdriver_manager.chrome import ChromeDriverManager  # Chrome
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager    # Edge
from selenium.common.exceptions import NoSuchElementException , ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd 
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_next_and_wait(driver):
    target_div = driver.find_element(By.XPATH, '//*[@id="divStart"]/div/div[3]/div[3]')
    target_div.click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "render-table-owner")))

driver = webdriver.Edge(service=EdgeService(executable_path='D:/Crawl_data_VietStock/msedgedriver.exe'))

# Open url 
url = "https://s.cafef.vn/lich-su-giao-dich-vnindex-1.chn"
driver.get(url)

# Lấy URL trang hiện tại
current_url = driver.current_url

# Gửi yêu cầu GET đến URL trang hiện tại
response = requests.get(current_url)

# Kiểm tra mã trạng thái HTTP
status_code = response.status_code

# In mã trạng thái HTTP
print("Mã trạng thái HTTP:", status_code)
page_index = 1
date = []
open = []
close = []
change = []
highest = []
lowest = []
weight = []
for index in range(1,55):
    sleep(3)
    for i in range(1,21):
        element_date = driver.find_element(By.XPATH,f'//*[@id="render-table-owner"]/tr[{i}]/td[1]')
        date.append(element_date.text)
        element_close = driver.find_element(By.XPATH,f'//*[@id="render-table-owner"]/tr[{i}]/td[2]')
        close.append(element_close.text)
        element_change = driver.find_element(By.XPATH,f'//*[@id="render-table-owner"]/tr[{i}]/td[4]')
        change.append(element_change.text)
        element_open = driver.find_element(By.XPATH,f'//*[@id="render-table-owner"]/tr[{i}]/td[9]')
        open.append(element_open.text)
        element_highest = driver.find_element(By.XPATH,f'//*[@id="render-table-owner"]/tr[{i}]/td[10]')
        highest.append(element_highest.text)
        element_lowest = driver.find_element(By.XPATH,f'//*[@id="render-table-owner"]/tr[{i}]/td[11]')
        lowest.append(element_lowest.text)
        element_weight = driver.find_element(By.XPATH,f'//*[@id="render-table-owner"]/tr[{i}]/td[7]')
        weight.append(element_weight.text)
        #   //*[@id="render-table-owner"]/tr[1]/td[3]
        # //*[@id="render-table-owner"]/tr[2]/td[3]
    click_next_and_wait(driver)    
        
    
percentile_list = pd.DataFrame(
    {'Ngay': date,
     'Dong cua': close,
     'Mo cua': open,
     'Cao nhat': highest,
     'Thap nhat' : lowest  ,
     'KL' : weight ,
     '% Thay doi' : change
    })
print(percentile_list)
print(len(date))
percentile_list.to_csv("VNINDEX_STOCK.csv", sep=',', encoding='utf-8',index=False)
# //*[@id="render-table-owner"]/tr[1]/td[2]
# //*[@id="render-table-owner"]/tr[2]/td[2]
#  54 page