import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.chrome_executable_path = "./chromedriver"
driver = webdriver.Chrome(options=options)
driver.get("http://localhost:5500/index.html")
with open('text.txt', 'r') as file:
    content = file.readline().strip()
values = content.split()
input_elements = driver.find_elements("xpath", "//input")
for i, value in enumerate(values):
    if i < len(input_elements):
        input_element = input_elements[i]
        input_element.send_keys(value)
time.sleep(5)
driver.quit()
