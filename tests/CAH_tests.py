from selenium import webdriver
from functions import *
from pages.CAH_pages import *


class RandoBot():
    
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        
        # set nickname
        set_nickname_page = SetNicknamePage(self.driver)
        set_nickname_page.navigate_to()
        nickname = 'i_am_rando'
        set_nickname_page.enter_nickname(nickname)
        
        # join a game
        game_select_page = set_nickname_page.click_set_button()
        host_name='iWin'
        game_select_page.enter_filter_terms(host_name)
        wait_until_element_exists_by_xpath(self.driver, '//div[starts-with(@id, "gamelist") and starts-with(@aria-label, "' + host_name + '")]//input[@class="gamelist_lobby_join"]')
        game_select_page.click_join_game_button(host_name)
        password = 'drugs'
        game_select_page.enter_game_password(password)
        
        # play the game
        play_game_page = game_select_page.click_ok_button()
        
        while True:
            
            # wait for other players
            if (verify_element_exists_by_xpath(self.driver, '//div[@class="game_message" and contains(text(), "Waiting for players...")]') or
                verify_element_exists_by_xpath(self.driver, '//div[@class="game_message" and contains(text(), "You are the Card Czar.")]')):
                print("Waiting for players")
                self.driver.implicitly_wait(3)
            # play a random white card
            elif verify_element_exists_by_xpath(self.driver, '//div[@class="game_message" and contains(text(), "Select a card to play.")]'):
                while verify_element_exists_by_xpath(self.driver, '//div[@class="game_message" and contains(text(), "Select a card to play.")]'):
                    play_game_page.select_rand_white_card()
                    play_game_page.click_confirm_selection_button()
                self.driver.implicitly_wait(1)
            # select a random winner
            elif verify_element_exists_by_xpath(self.driver, '//div[@class="game_message" and contains(text(), "Select a winning card.")]'):
                # give some time to look at the cards
                self.driver.implicitly_wait(5)
                play_game_page.select_rand_winner()
                play_game_page.click_confirm_selection_button()
                # wait for the next round to start
                wait_until_element_exists_by_xpath(self.driver, '//div[@class="game_message" and contains(text(), "Select a card to play.")]')
            