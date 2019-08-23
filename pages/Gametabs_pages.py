
from selenium.webdriver.common.action_chains import ActionChains

class BasePage():
    
    def __init__(self, driver):
        self.driver = driver
    
    def navigate_to(self):
        self.driver.get(self.url)


class HomePage(BasePage):
    
    url = 'https://www.gametabs.net/'
    
    def select_search_scope(self, scope):
        
        scope = scope.lower()
        if scope == 'site':
            try:
                self.driver.find_element_by_css_selector('input[id^+"edit-sitesearch"]').click()
            except Exception as err:
                print('Could not select the site radio button: ', err)
        elif scope == 'forums':
            try:
                # self.driver.find_element_by_css_selector('input[id^="edit-sitesearch-gametabs.net/forum"]').click()
                ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector('input[id^="edit-sitesearch-gametabs.net/forum"]')).click(self.driver.find_element_by_css_selector('input[id^="edit-sitesearch-gametabs.net/forum"]')).perform()
            except Exception as err:
                print('Could not select the forums radio button: ', err)
        else:
            print('Search scope is defined as ' + scope + ' but it can only site or forums')
    
    
    def enter_search_terms(self, search_terms):
        self.driver.find_element_by_id('edit-query').send_keys(search_terms)
    
    
    def click_search_button(self):
        self.driver.find_element_by_id('edit-sa').click()
        return SearchPage(self.driver)
    
    
    def click_sign_in_link(self):
        try:
            self.driver.find_element_by_css_selector('a[id="login-link"]').click()
        except Exception as err:
            print('Could not click the Sign-in link: ', err)
    
    
    def enter_username(self, username):
        try:
            self.driver.find_element_by_css_selector('input[placeholder="Username"]').send_keys(username)
        except Exception as err:
            print('Could not enter username: ', err)
    
    
    def enter_password(self, password):
        try:
            self.driver.find_element_by_css_selector('input[placeholder="Password"]').send_keys(password)
        except Exception as err:
            print('Could not enter password: ', err)

    
    def click_login_button(self):
        try:
            self.driver.find_element_by_css_selector('button span').click()
        except Exception as err:
            print('Could not click the Login button: ', err)
            
            
    def click_logout_link(self):
        try:
            self.driver.find_element_by_css_selector('a[id="logout-link"]').click()
        except Exception as err:
            print('Could not click the Logout link: ', err)


class SearchPage(BasePage):
    
    def verify_search_results(self, results_expected):
        print('the page is broken so did not find ' + results_expected)
        
        








