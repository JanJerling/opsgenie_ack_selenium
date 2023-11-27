from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import datetime
 

while 1 == 1 :
    error = 0
    while error < 1:
        time.sleep(30)
        try:
            driver=webdriver.Chrome()
            driver.get("https://takealot.app.opsgenie.com/alert/list")
            time.sleep(10)
            driver.find_element(By.XPATH, '//*[@id="ops-login"]/div[2]/div[1]/form/div[1]/div[1]/input').send_keys('jan.jerling@takealot.com')
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="ops-login"]/div[2]/div[1]/form/div[1]/div[2]/button').click()
            time.sleep(5)
            driver.find_element(By.XPATH, '//*[@id="ops-login"]/div[2]/div[1]/form/div[1]/div[2]/input').send_keys('bumpyR@t90')
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="ops-login"]/div[2]/div[1]/form/div[1]/div[3]/button[1]').click()
            time.sleep(15)
        except:
            print(Exception)
            driver.quit()
            error = 1
        try:
            while 1 == 1:
                checker = 0
                while checker < 1:
                    driver.refresh()
                    time.sleep(15)
                    unacked = driver.find_element(By.XPATH,'//*[@id="alert-list"]/div/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div[4]/p').text
                    if "Un'Acked" in unacked:
                        driver.find_element(By.XPATH,'//*[@id="alert-list"]/div/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div[4]').click()
                        unack = datetime.datetime.now()
                        print(unack, " - UnAcked Reached")
                        time.sleep(10)
                        try:
                            driver.find_element(By.CLASS_NAME,'alert-list-item-vue-cover')
                            tck = datetime.datetime.now()
                            print(tck, " - !!!!!!!!!!!!!!!Found Ticket!!!!!!!!!!!!!!!!!!!!")
                            driver.find_element(By.XPATH, '//*[@id="alert-list"]/div/div/div/div[2]/div/div[2]/div/div/div/a/div[4]/div[2]/div/div[1]/button[1]').click()
                            ack = datetime.datetime.now()
                            print(ack, " - Ticket Acked")
                        except:
                            notck = datetime.datetime.now()
                            print(notck, " - No ticket found")
                            checker = 1
                    else:
                        print("UnAcked element Not found!")
                        driver.quit()
                        error = 1
                    time.sleep(180) # wait time before refresh
        except:
            print(Exception)
            driver.quit()
            error = 1

