
class BasePage():

    def __init__(self, driver):
        self.driver = driver


    def navigate_to(self)
        self.driver.get(self.url)
    
    
    def click_search_button(self):
        self.driver.find_element_by_css_selector('.nav-input').click()
    
    
    def click_my_wish_list_link(self):
        self.driver.find_element_by_xpath('//div[@id="nav-al-wishlist"]//span[contains(text(), "My Wish List")]').click()
        return ListsPage(self.driver)
        

    def open_accounts_and_lists_flyout_menu(self):
        self.driver.execute_script('document.querySelector("#nav-flyout-accountList").style.display = "block"')


    def enter_seach_terms(self, search_terms):
        self.driver.find_element_by_css_selector('#twotabsearchtextbox').send_keys(search_terms)
        
    
class ListsPage(BasePage):
    
    def enter_search_terms(self, search_terms):
        self.driver.find_element_by_css_selector('#itemSearchTextInput').send_keys(search_terms)
        
        
    

    
