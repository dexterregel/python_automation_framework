




class BasePage():
    
    def __init__(self, driver):
        self.driver = driver
    
    def navigate_to(self):
        self.driver.get(self.url)


class SetNicknamePage(BasePage):
    
    url = 'https://pyx-1.pretendyoure.xyz/zy/game.jsp'
    
    def enter_nickname(self, nickname):
        try:
            self.driver.find_element_by_css_selector('input#nickname').send_keys(nickname)
        except Exception as err:
            print('Could not enter nickname: ', err)
    
    
    def click_set_button(self):
        try:
            self.driver.find_element_by_css_selector('input#nicknameconfirm').click()
        except Exception as err:
            print('Could not click the Set button: ', err)
        
        return GameSelectPage(self.driver)


class GameSelectPage(BasePage):
    
    def enter_filter_terms(self, filter_terms):
        try:
            self.driver.find_element_by_css_selector('input#filter_games').send_keys(filter_terms)
        except Exception as err:
            print('Could not enter filter terms: ', err)
    
    
    def join_game(self, game_name):
        try:
            self.driver.find_element_by_xpath('//div[starts-with(@id, "gamelist") and starts-with(@aria-label, "' + game_name + '")]//input[@class="gamelist_lobby_join"]').click()
        except Exception as err:
            print('Could not join game because: ', err)
    
    
    def enter_password(self, password):
        try:
            self.driver.switch_to().alert().send_keys(password)
        except Exception as err:
            print('Could not enter the password: ', err)
        
        self.driver.switch_to().alert().accept()
        







