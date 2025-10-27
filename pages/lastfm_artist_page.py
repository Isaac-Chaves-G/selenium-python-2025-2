from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LastFmArtistPage(BasePage):
    LATEST_RELEASE__DATE = (By.CLASS_NAME, "artist-header-featured-items-item-dat1e")
    
    def get_latest_release_date(self):
        return self.find_element