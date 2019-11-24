from selenium import webdriver
from functions import *
from pages.Gametabs_pages import *

def test_search():

    driver = webdriver.Firefox()
    driver.maximize_window()
    
    home_page = HomePage(driver)
    home_page.navigate_to()
    home_page.select_search_scope('forums')
    home_page.enter_search_terms('hello')
    search_page = home_page.click_search_button()
    search_page.verify_search_results('hello')
    
    driver.close()


# positive and negative testing for logging in and out of Gametabs
def test_log_in():
    driver = webdriver.Firefox()
    driver.maximize_window()
    
    home_page = HomePage(driver)
    
    # try logging in without entering a username and verify the expected error appears
    home_page.navigate_to()
    home_page.click_sign_in_link()
    wait_until_element_exists_by_css_selector(driver, 'div[id="auth-app"]')
    username = ''
    password = 'test'
    home_page.enter_username(username)
    home_page.enter_password(password)
    home_page.click_login_button()
    wait_until_element_exists_by_xpath(driver, '//div[@id="auth-app"]//div[contains(text(), "User name field is required.")]')
    
    # try logging in without entering a password and verify the expected error appears
    home_page.navigate_to()
    home_page.click_sign_in_link()
    wait_until_element_exists_by_css_selector(driver, 'div[id="auth-app"]')
    username = 'test'
    password = ''
    home_page.enter_username(username)
    home_page.enter_password(password)
    home_page.click_login_button()
    wait_until_element_exists_by_xpath(driver, '//div[@id="auth-app"]//div[contains(text(), "Password field is required.")]')
    
    # try logging in with incorrect credentials and verify the expected message appears
    home_page.navigate_to()
    home_page.click_sign_in_link()
    wait_until_element_exists_by_css_selector(driver, 'div[id="auth-app"]')
    username = 'test'
    password = 'test'
    home_page.enter_username(username)
    home_page.enter_password(password)
    home_page.click_login_button()
    wait_until_element_exists_by_xpath(driver, '//div[@id="auth-app"]//div[contains(text(), "Wrong username or password.")]')
    
    # try logging in with valid credentials
    home_page.navigate_to()
    home_page.click_sign_in_link()
    wait_until_element_exists_by_css_selector(driver, 'div[id="auth-app"]')
    username = ''
    password = ''
    home_page.enter_username(username)
    home_page.enter_password(password)
    home_page.click_login_button()
    wait_until_element_exists_by_xpath(driver, '//div[@id="login-or-register"]/a[contains(text(),"' + username + '")]')
    
    # try logging out
    home_page.click_logout_link()
    wait_until_element_exists_by_xpath(driver, '//div[@id="login-or-register" and contains(text(), "Welcome to gametabs.net!")]')
    
    driver.close()
        
        
        

