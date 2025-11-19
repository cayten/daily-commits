from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def test_title_change():
    opts=Options(); opts.add_argument('--headless=new')
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    try:
        driver.get('http://localhost:8000/index.html')
        name=driver.find_element(By.ID,'name'); btn=driver.find_element(By.ID,'btn')
        name.send_keys('CAYTEN'); btn.click(); time.sleep(0.2)
        assert driver.find_element(By.ID,'title').text=='Hello, CAYTEN'
    finally:
        driver.quit()
