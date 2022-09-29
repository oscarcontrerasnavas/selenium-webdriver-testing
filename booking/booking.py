from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import booking.constants as const


class Booking(webdriver.Chrome):
    def __init__(
        self,
        service=ChromeService(ChromeDriverManager().install()),
        teardown=False,
        headless=False,
    ):
        self.teardown = teardown
        options = Options()
        options.headless = headless
        super(Booking, self).__init__(service=service, options=options)
        self.implicitly_wait(30)
        self.maximize_window()

    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()

    def land_home_page(self):
        self.get(const.BASE_URL)

    def select_currency(self, currency="USD"):
        currency_button = self.find_element(
            By.XPATH, '//button[@data-tooltip-text="Choose your currency"]'
        )
        currency_button.click()
        currency_option = self.find_element(
            By.XPATH,
            f'(//div[@class="bui-traveller-header__currency"][contains(text(), "{currency}")])[1]',
        )
        currency_option.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, "ss")
        search_field.clear()
        search_field.send_keys(place_to_go)
        destination = self.find_element(
            By.CSS_SELECTOR,
            'ul[aria-label="List of suggested destinations "] li:first-child',
        )
        destination.click()

    def select_dates(self, checkin_date, checkout_date):
        # TODO: Select dates X months in the future
        check_in = self.find_element(By.CSS_SELECTOR, f'td[data-date="{checkin_date}"]')
        check_in.click()
        check_out = self.find_element(
            By.CSS_SELECTOR, f'td[data-date="{checkout_date}"]'
        )
        check_out.click()

    def select_adults(self, adults=1):

        # Open the container
        self.find_element(By.ID, "xp__guests__toggle").click()

        # Select the current value
        current_adults = int(
            self.find_element(By.CSS_SELECTOR, "span[data-adults-count]").text.split(
                " "
            )[0]
        )

        if adults > current_adults:
            for _ in range(current_adults, adults):
                self.find_element(
                    By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]'
                ).click()

        if adults < current_adults:
            for _ in range(current_adults, adults, -1):
                self.find_element(
                    By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]'
                ).click()

    # TODO: Methods for child number and room number

    def submit_search(self):
        self.find_element(By.CSS_SELECTOR, 'button[data-sb-id="main"]').click()

    def get_page_title(self):
        return self.title

    def get_result_length(self):
        results = self.find_elements(
            By.CSS_SELECTOR, 'div[data-testid="property-card"]'
        )
        return len(results)
