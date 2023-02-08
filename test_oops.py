import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


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