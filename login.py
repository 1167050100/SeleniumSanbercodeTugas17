import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

        def setUp(self):
            self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
        def test_a_success_login(self):
            # steps
            driver = self.browser #buka web browser
            driver.get("https://www.saucedemo.com/") # buka situs
            time.sleep(3)
            driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
            time.sleep(1)
            driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
            time.sleep(1)
            driver.find_element(By.ID, "login-button").click()
            time.sleep(1)

            # validasi
            response_data = driver.find_element(By.CLASS_NAME,"title").text
            self.assertIn('PRODUCTS', response_data)

        def test_failed_login_with_null_credentials(self):
            #steps
            driver = self.browser #buka web browser 
            driver.get("https://www.saucedemo.com/") # buka situs
            time.sleep(3)
            driver.find_element(By.ID,"user-name").send_keys("") #null credentials
            time.sleep(1)
            driver.find_element(By.ID,"password").send_keys("") #null credentials
            time.sleep(1)
            driver.find_element(By.ID,"login-button").click()
            time.sleep(1)

            # validasi
            response_data = driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3').text
            self.assertIn('Epic sadface: Username is required', response_data)

        def test_failed_login_with_wrong_username(self):
            #steps
            driver = self.browser #buka web browser 
            driver.get("https://www.saucedemo.com/") # buka situs
            time.sleep(3)
            driver.find_element(By.ID,"user-name").send_keys("WrongUser") #wrong credentials
            time.sleep(1)
            driver.find_element(By.ID,"password").send_keys("secret_sauce") #correct credentials
            time.sleep(1)
            driver.find_element(By.ID,"login-button").click()
            time.sleep(1)

            # validasi
            response_data = driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3').text
            self.assertIn('Epic sadface: Username and password do not match any user in this service', response_data)

        def test_failed_login_with_wrong_password(self):
            #steps
            driver = self.browser #buka web browser 
            driver.get("https://www.saucedemo.com/") # buka situs
            time.sleep(3)
            driver.find_element(By.ID,"user-name").send_keys("standard_user") #correct credentials
            time.sleep(1)
            driver.find_element(By.ID,"password").send_keys("WrongPassword") #wrong credentials
            time.sleep(1)
            driver.find_element(By.ID,"login-button").click()
            time.sleep(1)

            # validasi
            response_data = driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3').text
            self.assertIn('Epic sadface: Username and password do not match any user in this service', response_data)

        def tearDown(self):
            self.browser.close()

if __name__ == "__main__":
    unittest.main()