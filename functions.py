

def verify_element_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except:
        return False
    return True


def verify_element_exists_by_css_selector(driver, css_selector):
    try:
        driver.find_element_by_css_selector(css_selector)
    except:
        return False
    return True


def wait_until_element_exists_by_xpath(driver, xpath, max_wait = None, raise_exception = True):

    if max_wait == None:
        max_wait = 5
        
    print('Waiting until element exists...')
    time = 0
    while not verify_element_exists_by_xpath(driver, xpath) and time <= max_wait:
        driver.implicitly_wait(1)
        time += 1

    if raise_exception and not verify_element_exists_by_xpath(driver, xpath):
        raise Exception('The element did not appear')


def wait_until_element_exists_by_css_selector(driver, css_selector, max_wait = None, raise_exception = True):

    if max_wait == None:
        max_wait = 5
        
    print('Waiting until element exists...')
    time = 0
    while not verify_element_exists_by_css_selector(driver, css_selector) and time <= max_wait:
        driver.implicitly_wait(1)
        time += 1

    if raise_exception and not verify_element_exists_by_css_selector(driver, css_selector):
        raise Exception('The element did not appear')