import requests  # For making HTTP requests to the Ollama API

# Function to get AI feedback from a local Ollama model
# Takes resume_text (string) as input and returns a dictionary with score and comments

def get_ai_feedback(resume_text):
    # Use Ollama locally to get AI feedback on the resume text
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",  # Ollama API endpoint
            json={
                "model": "llama3",  # Model name; change if you use a different model
                "prompt": f"Give constructive feedback on this resume:\n{resume_text}",  # Prompt for the AI
                "stream": False  # Get the full response at once
            },
            timeout=180  # Wait up to 180 seconds for a response
        )
        response.raise_for_status()  # Raise an error if the request failed
        data = response.json()  # Parse the JSON response
        feedback_text = data.get("response", "No feedback received.")  # Extract feedback
        feedback_text = feedback_text.strip()  # Clean up whitespace
        return {"score": None, "comments": feedback_text}  # Return feedback in a dict
    except Exception as e:
        # If there's an error, return an error message in the comments
        return {"score": 0, "comments": f"Error getting feedback: {str(e)}"}

# Function to format the feedback for display in the template
# Takes the response dict and returns a formatted dict

def parse_feedback_response(response):
    # This function parses the AI feedback response and formats it for display.
    score = response.get("score", 0)
    comments = response.get("comments", "")
    formatted_feedback = {
        "score": score,
        "comments": comments  # Already a string, no need to join
    }
    return formatted_feedback