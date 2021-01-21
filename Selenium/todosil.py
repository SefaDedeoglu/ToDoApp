from selenium.webdriver.common.by import By
from selenium import webdriver as wb
import  time
import selenium
import random

driver = wb.Chrome('D://chromedriver')
#driver1 = wb.Chrome('D://chromedriver')
driver.get("http:127.0.0.1:8000")
#driver1.get("http:stackoverflow.com/questions")
time.sleep(3)

k=1
driver.maximize_window()
while True:
    
    link = "/html/body/div[3]/div[2]/div[1]/div[3]/div["+str(k)+"]/div[2]/div[1]"
    #text = driver1.find_element_by_xpath(link).text
    k+=1
    button2 = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/button").click()
    time.sleep(1)
    butonyol = "/html/body/div[1]/div/div/div[2]/button["+str(k)+"]"
    button1= driver.find_elements_by_xpath(butonyol)[0].click()
    time.sleep(2)
    num = driver.find_element_by_xpath("/html/body/div[2]/button/span").text
    time.sleep(1)
    for i in range(0,int(num)):
        button3 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/button[2]").click()
        time.sleep(1)
        button4 = driver.find_element_by_xpath("/html/body/div/div/form/div[6]/div[1]/button").click()
        time.sleep(1)


    time.sleep(1)
    anamenu = driver.find_element_by_id("mainmenubutton")
    anamenu.click()
    time.sleep(3)
    
    if(k==15):
        k=1
    

driver.close()
