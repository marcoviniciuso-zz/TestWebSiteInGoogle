import unittest 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestAcademySite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromeDriver/chromedriver.exe')

    def test_academy_site(self):
        driver = self.driver
        driver.get('https://www.google.com/search?q=sap+academy+engineering&rlz=1C1GCEU_pt-BRBR819BR819&oq=sap+aca&aqs=chrome.0.69i59l2j69i60j69i61j69i60j69i65l3.1025j0j7&sourceid=chrome&ie=UTF-8')
        link = driver.find_element_by_xpath('//a[@href="'+'https://sapengineering.academy/'+'"]')
        link.click()
        self.assertIn('SAP Academy for Engineering – Beyond Code', driver.title)
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
        assert "404 - No results" not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()