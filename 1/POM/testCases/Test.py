from selenium.webdriver.common.by import By
from selenium import webdriver
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POM.pageObjects.loginPage import LoginPage

baseURL = "https://www.saucedemo.com/"
standard_user = "problem_user"
password = "secret_sauce"
driver = webdriver.Chrome()

driver.get(baseURL)
lg = LoginPage(driver)
lg.setUsername(standard_user)
lg.setPassword(password)
lg.clickLogin()
items = len(driver.find_elements(By.CLASS_NAME, "inventory_item"))
for item in range(1, items + 1):
    print(driver.find_element(By.XPATH, '(//div[@class="inventory_item"])[' + str(
        item) + ']/div[@class="inventory_item_img"]').is_displayed())
    print(driver.find_element(By.XPATH, '(//div[@class="inventory_item"])[' + str(
        item) + ']/div[@class="inventory_item_description"]').is_displayed())
    if driver.find_element(By.XPATH, '(//div[@class="inventory_item"])[' + str(
            item) + ']/div[@class="inventory_item_description"]').is_displayed():
        print(driver.find_element(By.XPATH, '(//div[@class="inventory_item"])[' + str(
            item) + ']//div[@class="inventory_item_label"]').is_displayed())
        print(driver.find_element(By.XPATH, '(//div[@class="inventory_item"])[' + str(
            item) + ']//div[@class="pricebar"]').is_displayed())
        print(driver.find_element(By.XPATH, '(//div[@class="inventory_item"])[' + str(
            item) + ']//div[@class="inventory_item_price"]').is_displayed())
