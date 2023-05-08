# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By # New version selenium using this one
from selenium.webdriver.chrome.service import Service # Then for login need to use this
from selenium.webdriver.support.ui import Select # import selector for selecting store
from selenium.webdriver.support.ui import WebDriverWait # define WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # define EC
import time

# open Web Browser
s = Service(r'C:\Users\forev\Downloads\chromedriver_win32 (1)\chromedriver') # 利用selenium做爬蟲
driver = webdriver.Chrome(service=s)

# Open web

driver.get('https://www.google.com/search?q=7-11%E9%96%80%E5%B8%82%E6%9F%A5%E8%A9%A2&oq=7-11%E9%96%80%E5%B8%82&aqs=chrome.1.69i57j0i433i512j0i512l5j5.5511j0j7&sourceid=chrome&ie=UTF-8&bshm=lbse/1')
#map_web = driver.find_element(By.XPATH, value = '//*[@id="rso"]/div[1]/div/div/table/tbody/tr[1]/td/div/h3/a')
map_web = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="rso"]/div[1]/div/div/table/tbody/tr[1]/td/div/h3/a')))
map_web.click()
# map_mask = driver.find_element(By.ID, "mapMask")
# content = map_mask.get_attribute("innerHTML")
# print(content)

#time.sleep(5)
# Target: 超級郡門市
frame_content = driver._switch_to.frame(0)
print(frame_content)
select = Select(driver.find_element(By.XPATH, value = f'//*[@id="sel_area"]'))
select.select_by_visible_text(u"桃園市") # This is what you want you can change.
time.sleep(3)

# choosing zone, This is not neccessary.
# select_zone = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(Select(driver.find_element(By.XPATH, value = f'//*[@id="road"]'))))
# select_zone = Select(driver.find_element(By.XPATH, value = f'//*[@id="zone"]'))
# select_zone.select_by_visible_text(u"中壢區")
# time.sleep(3)

js = 'document.getElementById("road").style.display="Block";'
driver.execute_script(js)
#WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="road_chosen"]')))
# choosing street
select_road = Select(driver.find_element(By.XPATH, value = f'//*[@id="road"]'))
select_road.select_by_visible_text(u"松信路")
time.sleep(3)

# choosing shop
select_store = driver.find_element(By.XPATH, value = f'//*[@id="ol_stores"]/li[1]')
select_store.click()
time.sleep(2)

#門市確認
# return to original frame, because changing to other frame that make selenium can not find the html content
driver.switch_to.default_content() 

map_mask = driver.find_element(By.ID, "mapMask")
content = map_mask.get_attribute("innerHTML")
print(content)
driver.find_element(By.XPATH, value = f'//*[@id="sevenDataBtn"]').click()
time.sleep(2)
driver.find_element(By.XPATH, value = f'//*[@id="AcceptBtn"]').click()
time.sleep(2)
driver.find_element(By.XPATH, value = f'//*[@id="submit_butn"]').click()

time.sleep(5)
# 關閉瀏覽器
driver.close()


