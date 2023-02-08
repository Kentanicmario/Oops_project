import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestBoatLifestyle:
    @pytest.fixture
    def driver(self, request):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(30)
        request.addfinalizer(driver.quit)
        return driver

    def test_login(self, driver):
        driver.get("https://www.boat-lifestyle.com/")
        driver.find_element(By.XPATH, "//span[@class='toggle-link']").click()
        driver.find_element(By.XPATH, "//a[@href='/account/login']").click()
        driver.find_element(By.ID, "customer[email]").send_keys("kentanicmario09@gmail.com")
        driver.find_element(By.ID, "customer[password]").send_keys("12345Abcd*")
        driver.find_element(By.XPATH, "//span[@class='loader-button__text']").click()
        expected_header = 'You have not placed any orders yet.'
        element = driver.find_element(By.XPATH, "//p[contains(@class,'text--subdued')]")
        assert expected_header in element.text
    def test_order(self, driver):
        driver.get("https://www.boat-lifestyle.com/")
        driver.find_element(By.XPATH, "//span[@class='toggle-link']").click()
        driver.find_element(By.XPATH, "//a[@href='/account/login']").click()
        driver.find_element(By.ID, "customer[email]").send_keys("kentanicmario09@gmail.com")
        driver.find_element(By.ID, "customer[password]").send_keys("12345Abcd*")
        driver.find_element(By.XPATH, "//span[@class='loader-button__text']").click()
        driver.find_element(By.XPATH,"//a[@class='button button--primary']").click()
        driver.find_element(By.XPATH,"//button[@class='popover-button hidden-pocket']").click()
        driver.find_element(By.XPATH,"//*[contains(text(),'Best selling')]").click()
        driver.find_element(By.XPATH,"//a[@href='/products/airdopes-131']").click()
        driver.find_element(By.XPATH,"(//span[@class='loader-button__text'])[2]").click()
        driver.find_element(By.XPATH,"//span[@class='checkmark']").click()
        driver.find_element(By.XPATH,"//span[normalize-space()='PLACE ORDER']").click()
        expected_header = 'DELIVERY ADDRESS'
        element = driver.find_element(By.XPATH, "//h2[contains(@class,'section__title layout-flex__item layout-flex__item--stretch')]")
        assert expected_header in element.text
    def test_add_address(self, driver):
        driver.get("https://www.boat-lifestyle.com/")
        driver.find_element(By.XPATH, "//span[@class='toggle-link']").click()
        driver.find_element(By.XPATH, "//a[@href='/account/login']").click()
        driver.find_element(By.ID, "customer[email]").send_keys("kentanicmario09@gmail.com")
        driver.find_element(By.ID, "customer[password]").send_keys("12345Abcd*")
        driver.find_element(By.XPATH, "//span[@class='loader-button__text']").click()
        driver.find_element(By.XPATH, "//a[@class='button button--primary']").click()
        driver.find_element(By.XPATH, "//button[@class='popover-button hidden-pocket']").click()
        driver.find_element(By.XPATH, "//*[contains(text(),'Best selling')]").click()
        driver.find_element(By.XPATH, "//a[@href='/products/airdopes-131']").click()
        driver.find_element(By.XPATH, "(//span[@class='loader-button__text'])[2]").click()
        driver.find_element(By.XPATH, "//span[@class='checkmark']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='PLACE ORDER']").click()
        driver.find_element(By.ID,"checkout_shipping_address_address1").send_keys("L&T Knowledge City NH-8 Ajwa Road Crossing Waghodia")
        driver.find_element(By.ID,"checkout_shipping_address_address2").send_keys("xyz apartment")
        driver.find_element(By.ID,"checkout_shipping_address_city").send_keys("vadodara")
        driver.find_element(By.ID,"checkout_shipping_address_zip").send_keys("3900000")
        driver.find_element(By.ID,"checkout_reduction_code").send_keys("123456")
        driver.find_element(By.ID,'checkout_submit').click()
        expected_header = 'Your GST Information'
        element = driver.find_element(By.XPATH, "//h2[contains(@class,'gst-heading')]")
        assert expected_header in element.text
    def test_element_check(self):
        try:
            self.driver.find_element(By.XPATH,"//span[@id='toggle-link']").click()
        except:
            print("Invalid xpath")
            expected_header = 'Invalid xpath'
            assert expected_header == 'Invalid xpath'