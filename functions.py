import logging
import time


def verify_element_exists_by_xpath(driver, xpath):
    logging.info("Entering verify_element_exists_by_xpath with xpath = "
        + xpath)
    doesElementExist = True
    try:
        driver.find_element_by_xpath(xpath)
    except:
        doesElementExist = False
    logging.info("Exiting verify_element_exists_by_xpath with doesElementExist = "
        + str(doesElementExist))
    return doesElementExist


def verify_element_exists_by_css_selector(driver, css_selector):
    logging.info("Entering verify_element_exists_by_css_selector with "
        + "css selector = " + css_selector)
    doesElementExist = True
    try:
        driver.find_element_by_css_selector(css_selector)
    except:
        doesElementExist = False
    logging.info("Exiting verify_element_exists_by_css_selector with "
        + "doesElementExist = " + str(doesElementExist))
    return doesElementExist


def wait_until_element_exists_by_xpath(driver, xpath, max_wait = None, raise_exception = True):

    logging.info('Entering wait_until_element_exists_by_xpath with xpath = '
        + xpath + ', max_wait = ' + str(max_wait) + ', raise_exception = '
        + str(raise_exception))
    doesElementExist = False

    if max_wait == None:
        logging.info("max_wait not specified, defaulting to 5 seconds")
        max_wait = 5
        
    logging.info('Waiting until element exists...')
    elapsedTime = 0
    while elapsedTime <= max_wait:
        if verify_element_exists_by_xpath(driver, xpath):
            logging.info("Element found after waiting " + str(elapsedTime) + " second(s)")
            doesElementExist = True
            break
        else:
            logging.info("Element not found. Elapsed wait time = " + str(elapsedTime)
                + " second(s)")
            time.sleep(1)
            elapsedTime += 1
    
    if raise_exception and not doesElementExist:
        logging.error('The element identified by the XPath ' + xpath
            + ' did not appear within the max wait time of ' + max_wait + ' seconds.')
        raise Exception('The element identified by the XPath ' + xpath
            + ' did not appear within the max wait time of ' + max_wait + ' seconds.')


def wait_until_element_exists_by_css_selector(driver, css_selector, max_wait = None, raise_exception = True):
    logging.info('Entering wait_until_element_exists_by_css_selector with css_selector = '
        + css_selector + ', max_wait = ' + str(max_wait) + ', raise_exception = '
        + str(raise_exception))
    
    if max_wait == None:
        max_wait = 5
        
    logging.info('Waiting until element exists...')
    elapsedTime = 0
    while not verify_element_exists_by_css_selector(driver, css_selector) and elapsedTime <= max_wait:
        time.sleep(1)
        elapsedTime += 1

    if raise_exception and not verify_element_exists_by_css_selector(driver, css_selector):
        logging.error('The element identified by the CSS selector ' + css_selector
            + ' did not appear within the max wait time of ' + max_wait + ' seconds.')
        raise Exception('The element identified by the CSS selector ' + css_selector
            + ' did not appear within the max wait time of ' + max_wait + ' seconds.')
