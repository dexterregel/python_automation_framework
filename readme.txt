
actual documentation is in progress. right now this readme is serving as a history and
lessons learned for developing the framework


before moving to pytest, this framework worked like:
	each test case was its own class
	each test case's steps were part of its class' __init__ method
	main.py created test case objects, and because the steps were part of __init__,
	the steps would run once main was called and the object was created
	a test looked like (note the selfs. those couldn't be used anymore because
	the test wasn't an object anymore):
		class Gametabs_SearchTest:
    
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

	also before pytest, main.py imported each python/test case file from the 
	ui_tests folder. going forward that isn't necessary because pytest will find
	the tests automatically based on naming conventions
	like:
		from ui_tests.Gametabs_tests import *

after pytest, each test was turned into a function instead. because pytest runs the test
automatically, there's no need for the class -> __init__ catch



