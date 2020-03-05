import unittest 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestAcademySite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromeDriver/chromedriver.exe')

    def test_academy_site(self):
        driver = self.driver
        driver.get('https://sapengineering.academy/')
        self.assertIn('SAP Academy for Engineering – Beyond Code', driver.title)
        self.assertIn('https://sapengineering.academy/', driver.current_url)
        assert "404 - No results" not in driver.page_source

    def test_write_in_google(self):
        driver = self.driver
        driver.get('https://www.google.com/')
        element = driver.find_element_by_xpath('//input[@title="Search"]')
        element.send_keys('sap academy for engineering')
        element.send_keys(Keys.ENTER)
        link = driver.find_element_by_xpath('//a[@href="'+'https://sapengineering.academy/'+'"]')
        link.click()
        self.assertIn('SAP Academy for Engineering – Beyond Code', driver.title)
        self.assertIn('https://sapengineering.academy/', driver.current_url)
        assert "404 - No results" not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()