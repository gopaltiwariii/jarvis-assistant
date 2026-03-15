import datetime
import webbrowser
import wikipedia
import pyjokes

def tell_time():
    """Returns the current time."""
    time = datetime.datetime.now().strftime('%I:%M %p')
    return f"The current time is {time}"

def tell_date():
    """Returns the current date."""
    date = datetime.datetime.now().strftime('%B %d, %Y')
    return f"Today is {date}"

def open_website(url_name):
    """Opens a website based on a simple name."""
    sites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://www.github.com",
        "stackoverflow": "https://stackoverflow.com"
    }
    
    if url_name in sites:
        webbrowser.open(sites[url_name])
        return f"Opening {url_name}"
    else:
        # Fallback to search if not a direct match
        webbrowser.open(f"https://www.google.com/search?q={url_name}")
        return f"Searching for {url_name} on Google"

def summarize_wikipedia(query):
    """Searches Wikipedia and returns a short summary."""
    try:
        results = wikipedia.summary(query, sentences=2)
        return f"According to Wikipedia: {results}"
    except wikipedia.exceptions.DisambiguationError as e:
        return f"There are multiple results for {query}. Please be more specific."
    except wikipedia.exceptions.PageError:
        return f"I couldn't find any Wikipedia page for {query}."
    except Exception as e:
        return "An error occurred while searching Wikipedia."

def tell_joke():
    """Returns a random programming joke."""
    joke = pyjokes.get_joke()
    return joke
