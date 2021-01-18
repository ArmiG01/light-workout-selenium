from selenium import webdriver
chrome_driver = "C:\Kotlin\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
url = "https://www.python.org/"
driver.get(url)
data = [i.get_attribute("datetime").split("T")[0] for i in driver.find_elements_by_css_selector(".event-widget time")]
events = [i.text for i in driver.find_elements_by_css_selector(".event-widget li a")]
final = {}
for i in range(len(data)):
    final[i] = {
        "time": data[i],
        "name": events[i]
    }
print(final)
driver.quit()
