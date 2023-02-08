from selenium import webdriver
from selenium.webdriver.common.by import By


class BoatLifestyle:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.boat-lifestyle.com/")

    def login(self):
        self.driver.find_element(By.XPATH,"//span[@class='toggle-link']").click()
        self.driver.find_element(By.XPATH,"//a[@href='/account/login']").click()
        self.driver.find_element(By.ID,"customer[email]").send_keys("kentanicmario09@gmail.com")
        self.driver.find_element(By.ID,"customer[password]").send_keys("12345Abcd*")
        self.driver.find_element(By.XPATH,"//span[@class='loader-button__text']").click()

    def order(self):
        return 0

class PlaceOrder(BoatLifestyle):
    def order(self):
        self.driver.find_element(By.XPATH,"//a[@class='button button--primary']").click()
        self.driver.find_element(By.XPATH,"//button[@class='popover-button hidden-pocket']").click()
        self.driver.find_element(By.XPATH,"//*[contains(text(),'Best selling')]").click()
        self.driver.find_element(By.XPATH,"//a[@href='/products/airdopes-131']").click()
        self.driver.find_element(By.XPATH,"(//span[@class='loader-button__text'])[2]").click()
        self.driver.find_element(By.XPATH,"//span[@class='checkmark']").click()
        self.driver.find_element(By.XPATH,"//span[normalize-space()='PLACE ORDER']").click()

    def add_address(self):
        self.driver.find_element(By.ID,"checkout_shipping_address_address1").send_keys("L&T Knowledge City NH-8 Ajwa Road Crossing Waghodia")
        self.driver.find_element(By.ID,"checkout_shipping_address_address2").send_keys("xyz apartment")
        self.driver.find_element(By.ID,"checkout_shipping_address_city").send_keys("vadodara")
        self.driver.find_element(By.ID,"checkout_shipping_address_zip").send_keys("3900000")
        self.driver.find_element(By.ID,"checkout_reduction_code").send_keys("123456")
        self.driver.find_element(By.ID,'checkout_submit').click()

    def element_check(self):
        try:
            self.driver.find_element(By.XPATH,"//span[@id='toggle-link']").click()
        except:
            print("Invalid xpath")


obj = PlaceOrder()
while True:
    print("Enter 1 for login")
    print("Enter 2 for Add item to cart only if you are logged in")
    print("Enter 3 to add address only if you are logged in and added items to your cart")
    print("Enter 4 for element check")
    print("Enter 5 to exit")
    choice = int(input())
    if choice == 1:
        obj.login()
    elif choice == 2:
        obj.order()
    elif choice == 3:
        obj.add_address()
    elif choice == 4:
        obj.element_check()
    elif choice == 5:
        quit()
