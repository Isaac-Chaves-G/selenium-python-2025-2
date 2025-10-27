# ...existing code...
from behave import given,when,then
from selenium import webdriver
from pages.lastfm_homepage import LastFmHomePage
from pages.lastfm_results_page import LastFmResultPage
from pages.lastfm_artist_page import LastFmArtistPage

@given("el usuario está en la home page de last.fm")
def step_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.last.fm/")
    context.lastfm_home = LastFmHomePage(context.driver)
