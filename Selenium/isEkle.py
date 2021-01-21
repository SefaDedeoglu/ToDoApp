from selenium.webdriver.common.by import By
from selenium import webdriver as wb
import  time
import selenium
import random

driver = wb.Chrome('D://chromedriver')
driver1 = wb.Chrome('D://chromedriver')
driver.get("http:127.0.0.1:8000")
driver1.get("http:stackoverflow.com/questions")
time.sleep(5)

k=1
while True:
    link = "/html/body/div[3]/div[2]/div[1]/div[3]/div["+str(k)+"]/div[2]/div[1]"
    text = driver1.find_element_by_xpath(link).text
    k+=1
    button1= driver.find_elements_by_xpath("/html/body/div[4]/div/div[1]/button")[0]
    button1.click()
    time.sleep(3)
    kartno = driver.find_element_by_name("kartNo")
    projeNo = driver.find_element_by_name("projeNo")
    teknikuzman = driver.find_element_by_name("teknikUzman")
    tahminisüre = driver.find_element_by_name("tahminiSure")
    gerceklesensure = driver.find_element_by_name("gerceklesenSure")
    isaciklama = driver.find_element_by_name("isAciklamasi")
    isnotlar = driver.find_element_by_name("notlar")
    tarih = driver.find_element_by_name("tarih")
    gonder = driver.find_elements_by_xpath("/html/body/form/div/div[6]/button")[0]
    dahafazlaoge = driver.find_element_by_xpath("/html/body/form/div/div[5]/button")

    tarih.send_keys("19-01-2019")
    time.sleep(1)
    kartno.send_keys(text)
    time.sleep(1)
    projeNo.send_keys(text)
    time.sleep(1)
    teknikuzman.send_keys(text)
    time.sleep(1)
    tahminisüre.send_keys(text)
    time.sleep(1)
    gerceklesensure.send_keys(text)
    time.sleep(1)
    isaciklama.send_keys(text)
    time.sleep(1)
    isnotlar.send_keys(text)
    time.sleep(1)
    sayi = random.randint(1,10)
    for i in range(0,sayi):

        dahafazlaoge.click()
        time.sleep(1)
        ta = driver.find_element_by_name("t"+str(i+1)).send_keys("19-01-2019")
        ya = driver.find_element_by_name("y"+str(i+1)).send_keys("bilmiyorum")
        aa = driver.find_element_by_name("a"+str(i+1)).send_keys("bilmiyorum")
        time.sleep(1)
    if(k==15):
        k=1
    gonder.click()
    time.sleep(3)

driver.close()
