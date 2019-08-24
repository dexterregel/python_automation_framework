from selenium import webdriver
from selenium.webdriver.common.alert import Alert
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
        game_select_page.join_game(host_name)
        password = 'mypasswordlol'
        Alert(self.driver).send_keys(password)
        Alert(self.driver).accept()