from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path=
                             r'C:\Users\Johnny\AppData\Local\Programs\Python\driver\phantomjs-2.1.1-windows\bin\phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(5)
print(driver.find_element_by_id("content").text)
driver.close()