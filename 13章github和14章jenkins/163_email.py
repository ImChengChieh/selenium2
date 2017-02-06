from selenium import webdriver
import time

driver= webdriver.Chrome()
driver.get("http://mail.163.com/")
driver.maximize_window()
driver.implicitly_wait(10)
iframe=driver.find_element_by_xpath('//*[@id="x-URS-iframe"]')
driver.switch_to.frame(iframe)
driver.find_element_by_xpath('//*[@name="email"]').send_keys("a13056432125")
driver.find_element_by_xpath('//*[@name="password"]').send_keys("zhenghuacai727")
driver.find_element_by_id('dologin').click()

time.sleep(3)
driver.quit()

