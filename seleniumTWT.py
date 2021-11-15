# VIDEO 1: Introduction to Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files\geckodriver.exe"
driver = webdriver.Firefox(executable_path=PATH)

#VIDEO 2: Locating elements from an HTML
# driver.get("https://www.techwithtim.net")
# print(driver.title)
#
# search = driver.find_element_by_name("s")
# search.send_keys("test")
# search.send_keys(Keys.RETURN)

# print(driver.page_source)             #TO GET THE CONTENTS OF THE PAGE
# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "main"))
#     )
#
#     articles = main.find_elements_by_tag_name("article")
#     for article in articles:
#         header = article.find_elements_by_class_name("entry_summary")
#         print(header.text)
#
# finally:
#     driver.quit()

#VIDEO 3: Page Navigating and clicking elements
driver.get("https://techwithtim.net")
link = driver.find_element_by_link_text("Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()

    driver.back()
    driver.back()
    driver.back()

except:
    driver.quit()