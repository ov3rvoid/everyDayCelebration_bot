from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://kakoysegodnyaprazdnik.ru")
# november_2_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/baza/noyabr/2']")))
# november_2_button.click()
# print('OOOOOOOOOOOOOOOOKKKKKKKKKKKKKKKKKKKK')
# time.sleep(3)
time.sleep(5)
november_2_button = driver.find_element(By.XPATH, "//a[@href='/baza/noyabr/2']")
november_2_button.click()
time.sleep(5)
