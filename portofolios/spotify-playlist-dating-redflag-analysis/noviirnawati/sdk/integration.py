def build_prompt(songs_collections: list) -> str:
    if len(songs_collections) == 0: return ""
    return "TODO"
    # TODO: CHOOSE AI MODEL, AND PLATFORM
    # TODO: ENGINEER THE PROMPT


def ai_analysis(song_collections: list):
    try:
        prompt = build_prompt(song_collections)
        if prompt == "": return "No Results"

        # integrate with AI model to analyze basic personality, attachment style prediction, based from the song_collections
        # TODO SDK INTEGRATION - CODING, SET UP API KEYS, ETC

        return "This is the result"
    except Exception:
        return "No Result, please try again with a different URL"
