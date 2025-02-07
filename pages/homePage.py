import random
import time
from setup.smooth_scroll import SmoothScroll


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.navigator = SmoothScroll(driver)

    def click_random_element(self, action):
        actions = {
            "click_random_age": self.navigator.scroll_bottom_up_button_click,
            "click_random_gender": self.navigator.scroll_bottom_up_button_click,
            "click_random_loan_amount": self.navigator.scroll_bottom_up_button_click,
            "click_random_loan_type": self.navigator.scroll_bottom_up_button_click,
        }

        if action in actions:
            actions[action]()
