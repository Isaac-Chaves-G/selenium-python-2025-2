from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ImdbHomePage(BasePage):
    SEARCH_BOX = (By.ID, "suggestion-search")
    SEARCH_BUTTON = (By.ID, "suggestion-search-button")

    def search_movie(self, movie_name):
        self.enter_text(self.SEARCH_BOX, movie_name)
        self.click(self.SEARCH_BUTTON)
