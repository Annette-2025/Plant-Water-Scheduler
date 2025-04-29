from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

class PlantWaterSchedulerTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Start the Chrome browser
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        # Create screenshots folder if it doesn't exist
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')

    def setUp(self):
        # Inject dummy plants data into localStorage
        self.driver.get("http://localhost:1001/pages/plantList.html")
        plants_data = {
            "plants": [
                {},
                {"name": "Rose", "month": 1, "day": 15, "year": 2025},
                {"name": "Lily", "month": 1, "day": 20, "year": 2025}
            ]
        }
        script = f"window.localStorage.setItem('plants', '{str(plants_data).replace("'", '"')}');"
        self.driver.execute_script(script)

    def tearDown(self):
        # Take a screenshot if the test failed
        if hasattr(self, '_outcome') and self._outcome.errors:
            for test, exc_info in self._outcome.errors:
                if exc_info:
                    test_method_name = self._testMethodName
                    timestamp = int(time.time())
                    self.driver.save_screenshot(f'screenshots/{test_method_name}_{timestamp}.png')

    def test_1_open_plant_list_page(self):
        driver = self.driver
        driver.get("http://localhost:1001/pages/plantList.html")
        header = driver.find_element(By.TAG_NAME, "h1").text
        self.assertIn("Plant", header)
        print("Opened plantList.html successfully!")

    def test_2_click_list_item(self):
        driver = self.driver
        driver.get("http://localhost:1001/pages/plantList.html")
        list_items = driver.find_elements(By.TAG_NAME, "li")
        self.assertTrue(len(list_items) > 0, "No list items found on plantList page!")
        list_items[0].click()
        print("Clicked a list item successfully!")

    def test_3_navigate_to_calendar(self):
        driver = self.driver
        driver.get("http://localhost:1001/pages/calendar.html")
        header = driver.find_element(By.TAG_NAME, "h2").text
        self.assertIn("January", header)
        print("Opened calendar.html successfully!")

    def test_4_verify_calendar_elements(self):
        driver = self.driver
        driver.get("http://localhost:1001/pages/calendar.html")
        month_element = driver.find_element(By.TAG_NAME, "h2")
        self.assertTrue(month_element.is_displayed())
        print("Calendar month header found!")

    def test_5_open_next_page(self):
        driver = self.driver
        driver.get("http://localhost:1001/pages/nextpage.html")
        header = driver.find_element(By.TAG_NAME, "h2").text
        self.assertIn("February", header)
        print("Opened nextpage.html successfully!")

    def test_6_open_april_page(self):
        driver = self.driver
        driver.get("http://localhost:1001/pages/april.html")
        table = driver.find_element(By.TAG_NAME, "table")
        self.assertTrue(table.is_displayed())
        print("Opened april.html and found table successfully!")

    @classmethod
    def tearDown(self):
    # Correct way to capture screenshots if test failed
        if hasattr(self, '_outcome') and self._outcome.result.errors:
            for method, error in self._outcome.result.errors:
                if error:
                    test_name = self._testMethodName
                    timestamp = int(time.time())
                    self.driver.save_screenshot(f'screenshots/{test_name}_{timestamp}.png')

if __name__ == "__main__":
    unittest.main()
