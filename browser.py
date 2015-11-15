from selenium import webdriver
import threading
import cachetools
import logging
logger = logging.getLogger(__name__)

_driver = webdriver.PhantomJS()
_locker = threading.Lock()

def _fetch(url:str):
    logger.warn("id of webdriver %d" % id(_locker))
    with _locker:
        _driver.get(url)
        code = _driver.page_source
        return code

_cache = cachetools.TTLCache(maxsize=128, ttl=3600, missing=_fetch) # 默认一小时内缓存有效

def fetch(url:str)->str:
    return _cache[url]
