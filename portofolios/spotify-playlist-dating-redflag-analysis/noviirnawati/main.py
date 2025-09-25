from .sdk.integration import ai_analysis
from .web_scraper.web_api_scraper import scrape_spotify_playlist_page

playlist_link = "https://open.spotify.com/playlist/7wARwuyCiPRMURGmh6xTLq"  # put your spotify playlist link inside the "your_playlist_link"

songs_collection = scrape_spotify_playlist_page(playlist_link)

ai_analysis(songs_collection)
