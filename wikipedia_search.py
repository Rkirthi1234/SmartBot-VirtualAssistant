import wikipedia

wikipedia.set_lang("en")

def search_wikipedia(query):
    try:
        print("Searching Wikipedia for:", query)
        summary = wikipedia.summary(query, sentences=1)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return "Multiple results found: " + ", ".join(e.options[:5])
    except wikipedia.exceptions.PageError:
        return "No matching Wikipedia page found."
    except Exception as e:
        return f"An error occurred: {e}"
