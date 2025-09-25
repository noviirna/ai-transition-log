import json
import traceback

from selenium import webdriver
from selenium.common import WebDriverException

from ..constant.constant import (ChromeDevToolProtocol as CDP,
                                 Generic,
                                 HttpMethod,
                                 NetworkLogs as CONSTANT,
                                 Spotify)
from ..helper.validator import str_is_empty_or_none, dct_is_empty_or_none
from ..model.model import PlaylistItem


def get_response_body(driver: webdriver.Chrome, request_id: str):
    try:
        return driver.execute_cdp_cmd(CDP.NETWORK_GET_RESPONSE_BODY,
                                      {CONSTANT.KEY_REQUEST_ID: request_id}).get(
            CONSTANT.KEY_BODY, {})
    except WebDriverException:
        return None


def get_request_body(driver: webdriver.Chrome, request_id: str):
    try:
        return driver.execute_cdp_cmd(CDP.NETWORK_GET_REQUEST_POST_DATA,
                                      {CONSTANT.KEY_REQUEST_ID: request_id}).get(
            CONSTANT.KEY_POST_DATA, {})
    except WebDriverException:
        return None


def get_dict_from_dict_default_empty(dictionary: dict, key: str) -> dict:
    return dictionary.get(key, {})


def operation_name_is_allowed(operation_name: str) -> bool:
    return (operation_name != Spotify.REQ_PARAM_FETCH_PLAYLIST_FIRST_PAGE
            and operation_name != Spotify.REQ_PARAM_FETCH_PLAYLIST_NEXT_PAGE)


## todo: there are still something missing in this method that makes the filters not works
def filter_playlist_items(filtered_network_logs: dict) -> list[PlaylistItem]:
    song_details = []
    for log in filtered_network_logs:
        items = (log.get(CONSTANT.KEY_DATA, {})
                 .get('playlistV2', {})
                 .get('content', {})
                 .get('items', []))
        if len(items) > 0:
            for item in items:
                detail = item.get('itemV2', {}).get('data', {})
                title = detail.get('name', Generic.EMPTY_STRING)
                artist = detail.get('artists', {}).get('items', [])
                song_details.append(PlaylistItem(title, process_artist_names(artist)))
        else:
            print("items is empty")

    print(song_details)
    with (open("songs_details.json", "w", encoding="utf-8") as f):
        f.write(json.dumps(song_details))

    return song_details


def process_artist_names(artists: list[dict]) -> str:
    if len(artists) == 0:
        return 'Unknown'

    artists = ""
    for artist in artists:
        name = artist.get('profile', {}).get('name', Generic.EMPTY_STRING)
        if (str_is_empty_or_none(name)): continue
        artists += name
        artists += Generic.COMMA_STRING

    artists = artists.rstrip(Generic.COMMA_STRING)
    return artists


def filter_network_logs(driver: webdriver.Chrome) -> list[dict]:
    # Fets all the logs from performance in Chrome
    log_entries = driver.get_log(CONSTANT.KEY_CHROME_LOG_PERFORMANCE)

    datas = "["
    for log_entry in log_entries:
        message_data = json.loads(log_entry[CONSTANT.KEY_MESSAGE])[CONSTANT.KEY_MESSAGE]

        if message_data.get(CONSTANT.KEY_METHOD,
                            Generic.EMPTY_STRING) != CDP.NETWORK_REQUEST_WILL_BE_SENT: continue

        params = message_data.get(CONSTANT.KEY_PARAMS, {})

        request_id = params.get(CONSTANT.KEY_REQUEST_ID, Generic.EMPTY_STRING)
        if str_is_empty_or_none(request_id): continue

        http_method = params.get(CONSTANT.KEY_REQUEST, {}).get(CONSTANT.KEY_METHOD, Generic.EMPTY_STRING)
        if http_method != HttpMethod.POST: continue

        try:
            net_request_body = get_request_body(driver, request_id)
            if dct_is_empty_or_none(net_request_body): continue

            request_body = json.loads(net_request_body)

            if operation_name_is_allowed(
                    request_body.get(Spotify.KEY_OPERATION_NAME, Generic.EMPTY_STRING)): continue

            net_response_body = get_response_body(driver, request_id)
            if dct_is_empty_or_none(net_response_body): continue

            response_body = json.loads(net_response_body)

            generated_json = {CONSTANT.KEY_REQUEST: request_body, CONSTANT.KEY_RESPONSE: response_body}
            datas += (json.dumps(generated_json) + Generic.COMMA_STRING)

        except Exception:
            traceback.print_exc()
            continue

    datas = datas.rstrip(",")
    datas += "]"

    # write the json for analyzing the logic only
    with (open("api_details.json", "w", encoding="utf-8") as file):
        file.write(datas)

    return json.loads(datas)


def process_netlogs(driver: webdriver.Chrome) -> list:
    # Filter only relevant traffic from network logs
    processed_netlogs = filter_network_logs(driver)

    # Filter so you only get the song and
    final_result = filter_playlist_items(processed_netlogs)
    return final_result
