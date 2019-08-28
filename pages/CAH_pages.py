
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from functions import *

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
    
    
    def join_game(self, game_name, password):
        try:
            self.driver.find_element_by_xpath('//div[starts-with(@id, "gamelist") and starts-with(@aria-label, "' + game_name + '")]//input[@class="gamelist_lobby_join"]').click()
        except Exception as err:
            print('Could not join game because: ', err)
    
        Alert(self.driver).send_keys(password)
        Alert(self.driver).accept()
        
        return PlayGamePage(self.driver)
    
    
    def enter_password(self, password):
        try:
            self.driver.switch_to().alert().send_keys(password)
        except Exception as err:
            print('Could not enter the password: ', err)
        
        self.driver.switch_to().alert().accept()

class PlayGamePage(BasePage):
    
    def selectRandWhiteCard(self):
        whiteCards = self.driver.find_elements_by_css_selector('div.game_hand_cards > div.card_holder')
        whiteCards[random.randint(0,len(whiteCards)-1)].click()
    
    def click_confirm_selection_button(self):
        self.driver.find_element_by_css_selector('input.confirm_card').click()
    
    def selectRandWinner(self):
        # if pick X round
        if verify_element_exists_by_xpath(self.driver, '//div[@class="game_white_cards_binder"]'):
            playedCards = self.driver.find_elements_by_xpath('//div[@class="game_white_cards_binder"]/div[@class="card_holder"]')
        else:
            playedCards = self.driver.find_elements_by_xpath('//div[contains(@class,"game_white_cards") and contains(@class,"game_right_side_cards")]/div[@class="card_holder"]')
        
        playedCards[random.randint(0,len(playedCards)-1)].click()
        







