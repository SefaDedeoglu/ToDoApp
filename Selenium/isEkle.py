from selenium.webdriver.common.by import By
from selenium import webdriver as wb
import  time
import selenium

driver = wb.Chrome('D://chromedriver')
driver.get("http:127.0.0.1:8000")
time.sleep(3)
while True:
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
    gonder = driver.find_elements_by_xpath("/html/body/form/div/div[6]/button")[0]


    kartno.send_keys("test0")
    time.sleep(1)
    projeNo.send_keys("test1")
    time.sleep(1)
    teknikuzman.send_keys("test2")
    time.sleep(1)
    tahminisüre.send_keys("test3")
    time.sleep(1)
    gerceklesensure.send_keys("test4")
    time.sleep(1)
    isaciklama.send_keys("test5")
    time.sleep(1)
    isnotlar.send_keys("test6")
    time.sleep(1)
    gonder.click()
    time.sleep(3)

driver.close()
