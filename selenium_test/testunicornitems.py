import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUnicornItems(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
    
    def test_login(self):
        self.driver.get("http://unicornitems.com/my-account/")

        WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.NAME, "username")))
        username = self.driver.find_element(By.ID, "username")
        password = self.driver.find_element(By.ID, "password")
        username.send_keys("kadiii")
        password.send_keys("123")
        
        # Login düğmesine tıklayın
        login_button = self.driver.find_element(By.NAME, "login")
        login_button.click()

        WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.XPATH, "html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul")))
        alert_message = self.driver.find_element(By.XPATH, "html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul")
                
        assert "ERROR: INCORRECT USERNAME OR PASSWORD" in alert_message.text
    

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
