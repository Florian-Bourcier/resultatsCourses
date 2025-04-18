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






driver = webdriver.Firefox()
driver.get("https://www.breizhchrono.com/liste-des-courses/course_annee/2025/course_departement/35/course_nom/duathlon")

# Cookies
time.sleep(3)
driver.find_element(By.ID,"tarteaucitronAllDenied2").click()

##################################################################

# # Locate the table element
# table = driver.find_element(By.CLASS_NAME, "list")

# # Extract rows from the table
# rows = table.find_elements(By.TAG_NAME, "tr")

# # Iterate over rows and extract data
# for row in rows:
#     row.find_elements(By.TAG_NAME, "td").

# time.sleep(5)
# driver.quit()


##################################################################


# Go to list of races
tab = driver.find_elements(By.XPATH,'//*[@id="list-courses"]/table/tbody/tr')
# driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/main/div/div[3]/table/tbody/tr[4]/td[1]/a').click()
# driver.find_element(By.XPATH,f"/html/body/div[4]/div/div[2]/main/div/div[3]/table/tbody/tr[{j}]/td[1]/a").click()

j=1
for i in range (len(tab)):

    driver.find_element(By.XPATH,f"/html/body/div[4]/div/div[2]/main/div/div[3]/table/tbody/tr[{j}]/td[1]/a").click()
    # driver.find_element(By.XPATH,f"//*[@id='list-courses']/table/tbody/tr[{j}]/td[1]/a").click()
    time.sleep(3)
    # Search results for Lannion team members
    try:
        search_box = driver.find_element(By.ID, "coureur_search") # Check that search bar is here
        search_box.clear()
        search_box.send_keys("Lannion")
        search_box.send_keys(Keys.ENTER)
    except Exception as ex:
        assert False

    time.sleep(10)
    j = j + 1
    driver.back()
    driver.back()



time.sleep(5)
driver.quit()






####################################
# GPT
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# # Initialize the WebDriver (e.g., Chrome)
# driver = webdriver.Chrome()

# try:
#     # Open the webpage
#     driver.get("https://www.breizhchrono.com/liste-des-courses/course_annee/2025/course_departement/35/course_nom/duathlon")

#     # Wait for the page to load completely
#     time.sleep(5)  # You might need to adjust the sleep time

#     # Locate the table element
#     table = driver.find_element(By.CLASS_NAME, "list-course")

#     # Extract rows from the table
#     rows = table.find_elements(By.TAG_NAME, "tr")

#     # Iterate over rows and extract data
#     for row in rows:
#         cells = row.find_elements(By.TAG_NAME, "td")
#         row_data = [cell.text for cell in cells]
#         print(row_data)

# finally:
#     # Close the WebDriver
#     driver.quit()