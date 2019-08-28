from selenium import webdriver
from functions import *
from pages.CAH_pages import *


class RandoBot():
    
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        
        set_nickname_page = SetNicknamePage(self.driver)
        set_nickname_page.navigate_to()
        
        nickname = 'i_am_rando'
        set_nickname_page.enter_nickname(nickname)
        game_select_page = set_nickname_page.click_set_button()
        
        host_name='mygame'
        game_select_page.enter_filter_terms(host_name)
        wait_until_element_exists_by_xpath(self.driver, '//div[starts-with(@id, "gamelist") and starts-with(@aria-label, "' + host_name + '")]//input[@class="gamelist_lobby_join"]')
        password = 'mypasswordlol'
        play_game_page = game_select_page.join_game(host_name, password)
        
        while True:
            
            # wait for other players
            if (verify_element_exists_by_xpath(self.driver, '//div[@class="game_message" and contains(text(), "Waiting for players...")]') or
                verify_element_exists_by_xpath(self.driver, '//div[@class="game_message" and contains(text(), "You are the Card Czar.")]')):
                print("Waiting for players")
                self.driver.implicitly_wait(3)
            
            # play a white card
            elif verify_element_exists_by_xpath(self.driver, '//div[@class="game_message" and contains(text(), "Select a card to play.")]'):
                
                while verify_element_exists_by_xpath(self.driver, '//div[@class="game_message" and contains(text(), "Select a card to play.")]'):
                    play_game_page.selectRandWhiteCard()
                    play_game_page.click_confirm_selection_button()
                
            # select a winning card
            elif verify_element_exists_by_xpath(self.driver, '//div[@class="game_message" and contains(text(), "Select a winning card.")]'):
                # give some time to look at the cards
                self.driver.implicitly_wait(5)
                play_game_page.selectRandWinner()
                play_game_page.click_confirm_selection_button()
                # wait for the next round to start or else you'll get stuck in the card czar loop
                self.driver.implicitly_wait(10)
            