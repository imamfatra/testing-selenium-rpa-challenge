from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class RpaChallange:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://rpachallenge.com/')
    
    def start(self):
        buttom_start = self.driver.find_element(By.CLASS_NAME, "uiColorButton")
        buttom_start.click()
        print("start")
    
    def address(self, address_var):
        address = self.driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelAddress']")
        address.clear()
        address.send_keys(address_var)
        print("input address")

    def role_in_company(self, role_var):
        role = self.driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelRole']")
        role.clear()
        role.send_keys(role_var)
        print("input role in company")

    def email(self, email_var):
        mail = self.driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelEmail']")
        mail.clear()
        mail.send_keys(email_var)
        print("input email")
    
    def first_name(self, first_name_var):
        fe = self.driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']")
        fe.clear()
        fe.send_keys(first_name_var)
        print("input first name")
    
    def last_name(self, last_name_var):
        ln = self.driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelLastName']")
        ln.clear()
        ln.send_keys(last_name_var)
        print("input last name")

    def company_name(self, company_var):
        company_name = self.driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelCompanyName']")
        company_name.clear()
        company_name.send_keys(company_var)   
        print("input company name")
    
    def phone_number(self, phone_var):
        phone_number = self.driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelPhone']")
        phone_number.clear()
        phone_number.send_keys(phone_var)
        print("input phone number")
    
    def submit(self):
        buttom_submit = self.driver.find_element(By.XPATH, "//input[@value='Submit']")
        buttom_submit.click()
        print("submit")
    
    def quit(self):
        self.driver.quit()
