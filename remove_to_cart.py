import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestRemoveAddCart(unittest.TestCase):

        def setUp(self):
            self.browser = webdriver.Chrome(ChromeDriverManager().install())

        def test_remove_add_to_cart(self):
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

            #remove to cart
            driver.find_element(By.ID,"remove-sauce-labs-backpack").click() #Click Button add to cart
            time.sleep(1)

            # validasi
            response_data = driver.find_element(By.CLASS_NAME,"shopping_cart_link").text
            self.assertIn('', response_data)

        def test_multiple_remove_to_cart(self):
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

            #add multiple to cart
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

        #remove multiple to cart
            driver.find_element(By.ID,"remove-sauce-labs-backpack").click() #Click Button add to cart
            time.sleep(1)
            driver.find_element(By.ID,"remove-sauce-labs-bike-light").click() #Click Button add to cart
            time.sleep(1)
            driver.find_element(By.ID,"remove-sauce-labs-bolt-t-shirt").click() #Click Button add to cart
            time.sleep(1)
            driver.find_element(By.ID,"remove-sauce-labs-fleece-jacket").click() #Click Button add to cart
            time.sleep(1)
            driver.find_element(By.ID,"remove-sauce-labs-onesie").click() #Click Button add to cart
            time.sleep(1)
            driver.find_element(By.ID,"remove-test.allthethings()-t-shirt-(red)").click() #Click Button add to cart
            time.sleep(1)

            # validasi
            response_data = driver.find_element(By.CLASS_NAME,"shopping_cart_link").text
            self.assertIn('', response_data)

        def tearDown(self):
            self.browser.close()

if __name__ == "__main__":
    unittest.main()