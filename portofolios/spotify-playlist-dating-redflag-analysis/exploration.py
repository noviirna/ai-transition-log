import json
import time
import traceback

import validators
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from validators import ValidationError


def validate_url(url_to_validate: str):
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


def setup_chromedriver():
    # Create the webdriver object and pass the arguments
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # enable this argument to hide the chrome browser UI
    options.add_argument("--ignore-certificate-errors")
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

    # Startup the chrome webdriver
    # pass the chrome options as parameters.
    return webdriver.Chrome(options=options)


def scroll_down_element_until_end(driver: webdriver, by: By, elementName: str):
    print("scrolling down element")
    try:
        print("begin scroll down")
        (ActionChains(driver)
         .click(driver.find_element(by=by, value=elementName))
         .perform())
        time.sleep(1)
        # note: the scrolling is working visually but the browser won't load the desired API
        # unlike when performing scroll manually
        # next maybe we are going to try to scroll using JS driver
        (ActionChains(driver)
         .send_keys(Keys.END)
         .perform())
        time.sleep(1)
    except:
        # pass through exception can't send keys
        pass
    finally:
        print("finish scroll down")
        time.sleep(10)


def process_logs(driver: webdriver.Chrome):
    print("begin processing logs")
    scraped_datas = []

    try:
        # Gets all the logs from performance in Chrome
        log_entries = driver.get_log("performance")

        # temporary json file for analying the API calls
        # after knowing how to filter the data, this will no longer be used
        with open("request_sent.json", "w", encoding="utf-8") as file:
            print("begin writing to file")
            file.write("[ ")

            for log_entry in log_entries:
                message_data = json.loads(log_entry["message"])["message"]

                if message_data.get("method", "") != "Network.requestWillBeSent": continue

                params = message_data.get("params", {})

                if (params.get("request", {}).get("method", "") != "POST"): continue

                requestId = params.get("requestId", "")

                try:
                    temp = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': requestId})
                    if temp is None: continue

                    responseBody = json.loads(temp.get("body", {}))

                    if responseBody == {} or responseBody is None: continue

                    requestBody = json.loads(
                        driver.execute_cdp_cmd('Network.getRequestPostData', {'requestId': requestId}).get(
                            "postData", {}))

                    operationName = requestBody.get("operationName", "")
                    if operationName != "fetchPlaylist" and operationName != "fetchPlaylistContents":
                        continue

                    scraped_datas.append(
                        responseBody.get("data", {}).get("data", {})
                    )

                    jsonData = {}
                    jsonData['request'] = (requestBody)
                    jsonData['response'] = (responseBody)
                    file.write(json.dumps(jsonData) + ",")

                except Exception:
                    print("found error when writing file, skip it")
                    print(traceback.format_exception_only())
                    continue

            file.write("{} ]")
            print("finished writing to file")

    finally:
        print("finish processing logs")
        return scraped_datas


def scrape_spotify_playlist_page(playlist_url: str):
    try:
        # Create an empty list variable to put the scraping results
        song_collections = []

        # Validate spotify URL
        if validate_url(playlist_url) is False:
            print("Invalid URL, can't proceed to continue process")
            return song_collections

        # Set up the Web Driver
        seleniumDriver = setup_chromedriver()

        # Load the page
        print("begin loading page")
        seleniumDriver.get(playlist_url)
        time.sleep(10)  # to ensure the page is fully loaded, esp when the internet connection is slow
        print("finish loading page")

        # Scroll until recommended track section show to ensure all URL is loaded
        scroll_down_element_until_end(seleniumDriver,
                                      By.CLASS_NAME,
                                      'c55UACltdzzDDQVfoF18')

        # Filter data from API, this approach chosen because there are no identifier in UI
        song_collections = process_logs(seleniumDriver)

        return song_collections
    except Exception:
        print(traceback.format_exc())
    finally:
        print("end")
        seleniumDriver.quit()


def build_prompt(songs_collections: list):
    return ""


def ai_analysis(spotify_playlist_url: str):
    try:
        song_collections = scrape_spotify_playlist_page(spotify_playlist_url)

        if len(song_collections) == 0:
            return "No Result, please try again with a different URL"

        # build prompt from song_collections
        prompt = build_prompt(song_collections)

        # integrate with AI model to analyze basic personality, attachment style prediction, based from the song_collections

        return "This is the result"
    except:
        return "No Result, please try again with a different URL"


playlist_link = "https://open.spotify.com/playlist/7wARwuyCiPRMURGmh6xTLq"  # put your spotify playlist link inside the "your_playlist_link"

print(
    ai_analysis(playlist_link)
)
