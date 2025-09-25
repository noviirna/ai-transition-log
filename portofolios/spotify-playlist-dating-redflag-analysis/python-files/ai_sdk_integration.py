from web_api_scraper import *


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



