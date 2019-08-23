from selenium import webdriver
from functions import *
from pages.Gametabs_pages import *

class SearchTest:
    
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        
        home_page = HomePage(self.driver)
        home_page.navigate_to()
        home_page.select_search_scope('forums')
        home_page.enter_search_terms('hello')
        search_page = home_page.click_search_button()
        search_page.verify_search_results('hello')
        
        self.driver.close()


# positive and negative testing for logging in and out of the website
class LogInTest:
    
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        
        home_page = HomePage(self.driver)
        
        # try logging in without entering a username and verify the expected error appears
        home_page.navigate_to()
        home_page.click_sign_in_link()
        # assert that the log-in popup appears
        username = ''
        password = 'test'
        home_page.enter_username(username)
        home_page.enter_password(password)
        home_page.click_login_button()
        assert verify_element_exists_by_xpath(self.driver, '//div[@id="auth-app"]//div[contains(text(), "User name field is required.")]'), 'The expected message did not appear'
        
        # try logging in without entering a password and verify the expected error appears
        home_page.navigate_to()
        home_page.click_sign_in_link()
        # assert that the log-in popup appears
        username = 'test'
        password = ''
        home_page.enter_username(username)
        home_page.enter_password(password)
        home_page.click_login_button()
        assert verify_element_exists_by_xpath(self.driver, '//div[@id="auth-app"]//div[contains(text(), "Password field is required.")]'), 'The expected message did not appear'
        
        # try logging in with incorrect credentials and verify the expected message appears
        home_page.navigate_to()
        home_page.click_sign_in_link()
        # assert that the log-in popup appears
        username = 'test'
        password = 'test'
        home_page.enter_username(username)
        home_page.enter_password(password)
        home_page.click_login_button()
        wait_until_element_exists_by_xpath(self.driver, '//div[@id="auth-app"]//div[contains(text(), "Wrong username or password.")]', 5, True)
        assert verify_element_exists_by_xpath(self.driver, '//div[@id="auth-app"]//div[contains(text(), "Wrong username or password.")]'), 'The expected message did not appear'
        
        # test logging in
        home_page.navigate_to()
        home_page.click_sign_in_link()
        # assert that the log-in popup appears
        username = 'what if bears could'
        password = ''
        home_page.enter_username(username)
        home_page.enter_password(password)
        home_page.click_login_button()
        # assert that the user is logged in
        
        # test logging out
        # home_page.click_
        
        # home_page.click_login_button()
        

