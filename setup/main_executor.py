import sys
from setup.browser_setup import BrowserSetup
from pages.homePage import Page
import random
from setup import utils
from setup.ad_clicker import AdClicker
import time


class MainExecutor:
    def __init__(
            self, device_type="both",
            proxy_active=True,
            device_name="random",
            browser_name="random",
            region="na",                    # rd, us, na, au, as, eu
            add_utm=True,
            enable_ad_click=False,
            ad_click_frequency=2
    ):
        self.device_type = device_type
        self.proxy_active = proxy_active
        self.device_name = device_name
        self.browser_name = browser_name
        self.region = region
        self.add_utm = add_utm
        self.enable_ad_click = enable_ad_click
        self.ad_click_frequency = ad_click_frequency

    def setup_driver(self):
        browser_setup = BrowserSetup()
        return browser_setup.setup_browser(
            self.device_type,
            self.proxy_active,
            device_name=self.device_name,
            browser_name=self.browser_name,
            region=self.region,
        )

    def process_run(self, driver, click_ad, ad_log_file):

        target_url = utils.target_url(self.add_utm)
        utils.open_url_with_retry(driver, target_url)

        page = Page(driver)

        # ad_clicker = AdClicker(driver)

        if click_ad:
            ad_target = random.choice(
                ["homepage", "genderPage", "loanAmountPage", "loanTypePage"])

            # if ad_target == "homepage":
            #     print("Visiting Homepage")
            #     ad_clicker.select_random_ad(ad_log_file, ad_target)

            # elif ad_target == "genderPage":
            #     print("Visiting GenderPage")
            #     homePage.click_random_age()
            #     ad_clicker.select_random_ad(ad_log_file, ad_target)

            # elif ad_target == "loanAmountPage":
            #     print("Visiting LoanAmountPage")
            #     homePage.click_random_age()
            #     genderPage.click_random_gender()
            #     ad_clicker.select_random_ad(ad_log_file, ad_target)

            # else:
            #     print("Visiting LoanTypePage")
            #     homePage.click_random_age()
            #     genderPage.click_random_gender()
            #     loanAmountPage.click_random_loan_amount()
            #     ad_clicker.select_random_ad(ad_log_file, ad_target)
        else:

            page_actions = {
                "homePage": ["click_random_age"],
                "genderPage": ["click_random_age", "click_random_gender"],
                "loanAmountPage": ["click_random_age", "click_random_gender", "click_random_loan_amount"],
                "loanTypePage": ["click_random_age", "click_random_gender", "click_random_loan_amount", "click_random_loan_type"]
            }

            weights = {
                "loanTypePage": 0.4,
                "loanAmountPage": 0.3,
                "genderPage": 0.2,
                "homePage": 0.1
            }

            target_page = random.choices(
                list(weights.keys()), weights=list(weights.values()), k=1)[0]
            print(f"Final page - {target_page}")

            for action in page_actions[target_page]:
                page.click_random_element(action)
