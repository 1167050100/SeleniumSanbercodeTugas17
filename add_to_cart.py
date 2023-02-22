import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestAddCart(unittest.TestCase):

        def setUp(self):
            self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
        def test_add_to_cart(self):
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

            #add to cart
            driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click() #Click Button add to cart
            time.sleep(1)

            # validasi
            response_data = driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text
            self.assertIn('1', response_data)

        def test_multiple_add_to_cart(self):
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

            #add to cart
            driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click() #Click Button add to cart
            time.sleep(1)
            driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click() #Click Button add to cart
            time.sleep(1)
            driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt").click() #Click Button add to cart
            time.sleep(1)
            driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket").click() #Click Button add to cart
            time.sleep(1)
            driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie").click() #Click Button add to cart
            time.sleep(1)
            driver.find_element(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)").click() #Click Button add to cart
            time.sleep(1)
            

            # validasi
            response_data = driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text
            self.assertIn('6', response_data)
                  
        def tearDown(self):
            self.browser.close()

if __name__ == "__main__":
    unittest.main()