import os
from google import genai
from .actions import tell_time, tell_date, open_website, summarize_wikipedia, tell_joke

# Initialize the Gemini client. It expects the GEMINI_API_KEY environment variable.
client = None
try:
    if "GEMINI_API_KEY" in os.environ:
        client = genai.Client()
except Exception as e:
    print(f"Error initializing Gemini: {e}")

def get_gemini_response(prompt):
    """Generates a response using the Gemini model."""
    if not client:
        return "I'm sorry, sir. My advanced connection to the Gemini network is not currently configured. I need a valid GEMINI_API_KEY."
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"I'm sorry, sir. I encountered a network error while connecting to my advanced brain."

def process_command(query):
    """Processes the text command and returns a response string."""
    query = query.lower()

    if "time" in query:
        return tell_time()
    
    elif "date" in query or "day" in query:
        return tell_date()
    
    elif "joke" in query:
        return tell_joke()

    elif "open" in query:
        # Simple extraction: "open youtube" -> "youtube"
        site_name = query.replace("open ", "").strip()
        site_name = site_name.split(" ")[0] # Just get the first word after open
        return open_website(site_name)

    elif "wikipedia" in query:
        # Extract query: "search wikipedia for python" -> "python"
        search_query = query.replace("wikipedia", "").replace("search", "").replace("for", "").strip()
        if search_query:
            return summarize_wikipedia(search_query)
        else:
            return "What would you like me to search on Wikipedia?"

    elif any(greeting in query for greeting in ["hello", "hi", "hey"]):
        return "Hello sir. How can I assist you today?"
        
    elif "how are you" in query:
        return "I am functioning at full capacity. Thanks for asking."

    elif "exit" in query or "quit" in query or "stop" in query or "goodbye" in query:
        return "Goodbye sir. Have a great day."

    # Unknown command, send to Gemini if available
    return get_gemini_response(query)
