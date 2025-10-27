from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ImdbMoviePage(BasePage):
    MOVIE_TITLE = (By.XPATH, "//h1")
    MOVIE_RATING = (By.XPATH, "//span[contains(@class, 'sc-bde20123-1')]")

    def get_movie_title(self):
        element = self.find_element(self.MOVIE_TITLE)
        return element.text.strip()

    def get_movie_rating(self):
        element = self.find_element(self.MOVIE_RATING)
        return element.text.strip()
