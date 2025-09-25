import json
import traceback

from selenium import webdriver
from selenium.common import WebDriverException


def get_response_body(driver: webdriver.Chrome, requestId: str):
    try:
        print("get response body")
        return driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': requestId}).get("body", {})
    except WebDriverException as e:
        return None


def get_request_body(driver: webdriver.Chrome, requestId: str):
    try:
        print("get request body")
        return driver.execute_cdp_cmd('Network.getRequestPostData', {'requestId': requestId}).get("postData", {})
    except WebDriverException as e:
        return None


def process_netlogs(driver: webdriver.Chrome):
    print("begin processing logs")
    scraped_datas = []

    try:
        # Gets all the logs from performance in Chrome
        log_entries = driver.get_log("performance")

        # temporary json file for analying the API calls
        # after knowing how to filter the data, this will no longer be used
        with (open("request_sent.json", "w", encoding="utf-8") as file):
            print("begin writing to file")
            file.write("[ ")

            for log_entry in log_entries:
                message_data = json.loads(log_entry["message"])["message"]

                if message_data.get("method", "") != "Network.requestWillBeSent": continue

                params = message_data.get("params", {})

                if (params.get("request", {}).get("method", "") != "POST"): continue

                requestId = params.get("requestId", "")
                if requestId == '' or requestId is None: continue

                try:
                    netRequestBody = get_request_body(driver, requestId)
                    if None is netRequestBody or {} == netRequestBody: continue

                    requestBody = json.loads(netRequestBody)

                    operationName = requestBody.get("operationName", "")
                    if operationName != "fetchPlaylist" and operationName != "fetchPlaylistContents":
                        continue

                    netResponseBody = get_response_body(driver, requestId)
                    if None is netResponseBody or {} == netResponseBody: continue

                    responseBody = json.loads(netResponseBody)

                    scraped_datas.append(
                        responseBody.get("data", {}).get("data", {})
                    )

                    jsonData = {}
                    jsonData['request'] = (requestBody)
                    jsonData['response'] = (responseBody)
                    file.write(json.dumps(jsonData) + ",")

                except Exception:
                    print("found error when writing file, skip it")
                    print(traceback.print_exc())
                    continue

            file.write("{} ]")
            print("finished writing to file")

    finally:
        print("finish processing logs")
        return scraped_datas
