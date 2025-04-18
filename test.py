import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox()

# driver.get("https://www.breizhchrono.com/")

# # For cookies
# time.sleep(3)
# driver.find_element(By.ID,"tarteaucitronAllDenied2").click()

# # Go to result page
# driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div[2]/div/ul/li[2]/div[1]/div/div/a").click()

# For cookies
# driver.find_element(By.ID,"tarteaucitronPersonalize2").click()






du_35 = webdriver.Firefox()
du_35.get("https://www.breizhchrono.com/liste-des-courses/course_annee/2025/course_departement/35/course_nom/duathlon")

# Cookies
time.sleep(3)
du_35.find_element(By.ID,"tarteaucitronAllDenied2").click()


# Go to list of races
tab = du_35.find_elements(By.XPATH,'//*[@id="list-courses"]/table/tbody/tr')
# du_35.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/main/div/div[3]/table/tbody/tr[4]/td[1]/a').click()
# du_35.find_element(By.XPATH,f"/html/body/div[4]/div/div[2]/main/div/div[3]/table/tbody/tr[{j}]/td[1]/a").click()

j=1
for i in range (len(tab)):

    du_35.find_element(By.XPATH,f"/html/body/div[4]/div/div[2]/main/div/div[3]/table/tbody/tr[{j}]/td[1]/a").click()
    # du_35.find_element(By.XPATH,f"//*[@id='list-courses']/table/tbody/tr[{j}]/td[1]/a").click()
    time.sleep(3)
    # Search results for Lannion team members
    try:
        search_box = du_35.find_element(By.ID, "coureur_search") # Check that search bar is here
        search_box.clear()
        search_box.send_keys("Lannion")
        search_box.send_keys(Keys.ENTER)
    except Exception as ex:
        assert False

    time.sleep(10)
    j = j + 1
    du_35.back()
    du_35.back()


