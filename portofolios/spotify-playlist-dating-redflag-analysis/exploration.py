import time
import traceback

import validators
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from validators import ValidationError


def validate_url(url_to_validate):
    print("validating url start")
    try:
        result = validators.url(url_to_validate)
        if isinstance(result, ValidationError):
            return False
        return result
    except:
        return False
    finally:
        print("validating url finish")

def scrape_spotify_playlist_page(playlist_url):
    try:
        # create an empty list variable to put the scraping results
        song_collections = []

        # Validate spotify URL
        if validate_url(playlist_url) is False:
            print("Invalid URL, can't proceed to continue process")
            return "No Result"

        # Configure WebDriver to use headless Firefox
        options = Options()
        options.add_argument('-headless')
        options.add_experimental_option("detach", True)


        seleniumDriver = webdriver.Chrome(options=options)

        # Get the URL given
        print("begin loading page")
        seleniumDriver.get(playlist_url)
        print("finish loading page")

        # scroll until recommended track section show to ensure all URL is loaded
        print("begin scroll down")
        seleniumDriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        print("finish scrol down")

        ## my PC had some issues with the chrome driver, and unable to run it, now I am exploring other methods to continue this mini project

        # search result from API with
        #       uri: https://api-partner.spotify.com/pathfinder/v2/query
        #       request body: operationName: fetchPlaylist
        #       this is a single hit API

        # search result from API with
        #       uri: https://api-partner.spotify.com/pathfinder/v2/query
        #       request body: operationName: fetchPlaylistContents
        #       this is a multiple hit API

        # list all the songs and artists of a playlist

        seleniumDriver.quit()
        return song_collections
    except Exception:
        print(traceback.format_exc())
        return song_collections


def ai_analysis(spotify_playlist_url):
    try:
        song_collections = scrape_spotify_playlist_page(spotify_playlist_url)

        # build prompt from song_collections

        # integrate with AI model to analyze basic personality, attachment style prediction, based from the song_collections
        if len(song_collections) == 0:
            return "No Result, please try again with a different URL"

        return "This is the result"
    except:
        return "No Result, please try again with a different URL"


playlist_link = "https://open.spotify.com/playlist/7wARwuyCiPRMURGmh6xTLq"  # put your spotify playlist link inside the "your_playlist_link"

print(
    ai_analysis(playlist_link)
)