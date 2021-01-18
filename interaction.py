from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver = "C:\Kotlin\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
url = "http://secure-retreat-92358.herokuapp.com/"
driver.get(url)
fname = driver.find_element_by_name("fName")
lname = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
fname.send_keys("Arman")
lname.send_keys("Karapetyan")
email.send_keys("arman009.cooll@gmail.com")
button = driver.find_element_by_class_name("btn-block")
button.send_keys(Keys.ENTER)
