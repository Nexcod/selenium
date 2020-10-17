import time

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webelement import WebElement

MAX_WAIT = 10


def wait_for(fn) -> WebElement:
    start_time = time.time()
    while True:
        try:
            return fn()
        except (AssertionError, WebDriverException) as e:
            if time.time() - start_time > MAX_WAIT:
                raise e
            time.sleep(0.5)
