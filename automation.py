import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://forms.abujaelectricity.com/DATP/")

time.sleep(3)

first_click = web.find_element_by_xpath('//*[@id="SelectId_0"]/div[2]/div[2]/div/span')
first_click.click()