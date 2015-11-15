from selenium import webdriver
import threading
import logging
logger = logging.getLogger(__name__)

_driver = webdriver.PhantomJS()
_locker = threading.Lock()

def fetch(url:str):
    logger.warn("id of webdriver %d" % id(_locker))
    with _locker:
        _driver.get(url)
        code = _driver.page_source
        return code

