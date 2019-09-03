
import random
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
    
    
    def click_join_game_button(self, host_name):
        try:
            self.driver.find_element_by_xpath('//div[starts-with(@aria-label, "' + host_name + '")]//input[@class="gamelist_lobby_join"]').click()
        except Exception as err:
            print('Could not click the join game button: ', err)


    def enter_game_password(self, password):
        try:
            Alert(self.driver).send_keys(password)
        except Exception as err:
            print('Could not enter the password: ', err)
    
    
    def click_ok_button(self):
        try:
            Alert(self.driver).accept()
        except Exception as err:
            print('Could not click the ok button: ', err)
        
        # the page changes after clicking the ok button, so return a new page object
        return PlayGamePage(self.driver)


class PlayGamePage(BasePage):
    
    def select_rand_white_card(self):
        try:
            whiteCards = self.driver.find_elements_by_css_selector('div.game_hand_cards > div.card_holder')
            whiteCards[random.randint(0,len(whiteCards)-1)].click()
        except Exception as err:
            print('Could not select a random white card: ', err)
    
    
    def click_confirm_selection_button(self):
        try:
            self.driver.find_element_by_css_selector('input.confirm_card').click()
        except Exception as err:
            print('Could not click the confirm selection button: ', err)
    
    
    def select_rand_winner(self):
        try:
            # select a random group of white cards if players played more than one
            if verify_element_exists_by_xpath(self.driver, '//div[@class="game_white_cards_binder"]'):
                playedCards = self.driver.find_elements_by_xpath('//div[@class="game_white_cards_binder"]/div[@class="card_holder"]')
            # select a random white card
            else:
                playedCards = self.driver.find_elements_by_xpath('//div[contains(@class,"game_white_cards") and contains(@class,"game_right_side_cards")]/div[@class="card_holder"]')
            playedCards[random.randint(0,len(playedCards)-1)].click()
        except Exception as err:
            print('Could not select a random winner: ', err)







