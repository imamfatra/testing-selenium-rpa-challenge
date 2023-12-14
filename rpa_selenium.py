from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class RpaChallange:
    def __init__(self) -> None:
        """
        Initializes the RpaChallange class and sets up the Selenium webdriver.
        """
        self.driver = webdriver.Chrome()
        self.driver.get('https://rpachallenge.com/')
    
    def start(self):
        """
        Clicks on the start button to initiate the process.
        """
        buttom_start = self.driver.find_element(By.CLASS_NAME, "uiColorButton")
        buttom_start.click()
        print("start")
    
    def address(self, address_var):
        """
        Enters the address value in the input field.
        
        Args:
            address_var (str): The address value to be entered.
        """
        address = self.driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelAddress']")
        address.clear()
        address.send_keys(address_var)
        print("input address")

    def role_in_company(self, role_var):
        """
        Enters the role in company value in the input field.
        
        Args:
            role_var (str): The role in company value to be entered.
        """
        role = self.driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelRole']")
        role.clear()
        role.send_keys(role_var)
        print("input role in company")

    def email(self, email_var):
        """
        Enters the email value in the input field.
        
        Args:
            email_var (str): The email value to be entered.
        """
        mail = self.driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelEmail']")
        mail.clear()
        mail.send_keys(email_var)
        print("input email")
    
    def first_name(self, first_name_var):
        """
        Enters the first name value in the input field.
        
        Args:
            first_name_var (str): The first name value to be entered.
        """
        fe = self.driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']")
        fe.clear()
        fe.send_keys(first_name_var)
        print("input first name")
    
    def last_name(self, last_name_var):
        """
        Enters the last name value in the input field.
        
        Args:
            last_name_var (str): The last name value to be entered.
        """
        ln = self.driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelLastName']")
        ln.clear()
        ln.send_keys(last_name_var)
        print("input last name")

    def company_name(self, company_var):
        """
        Enters the company name value in the input field.
        
        Args:
            company_var (str): The company name value to be entered.
        """
        company_name = self.driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelCompanyName']")
        company_name.clear()
        company_name.send_keys(company_var)   
        print("input company name")
    
    def phone_number(self, phone_var):
        """
        Enters the phone number value in the input field.
        
        Args:
            phone_var (str): The phone number value to be entered.
        """
        phone_number = self.driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelPhone']")
        phone_number.clear()
        phone_number.send_keys(phone_var)
        print("input phone number")
    
    def submit(self):
        """
        Clicks on the submit button to submit the form.
        """
        buttom_submit = self.driver.find_element(By.XPATH, "//input[@value='Submit']")
        buttom_submit.click()
        print("submit")
    
    def quit(self):
        """
        Quits the Selenium webdriver.
        """
        self.driver.quit()
