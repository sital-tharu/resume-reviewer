import requests

def get_ai_feedback(resume_text):
    # Use Ollama locally to get AI feedback on the resume text
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",  # Change to your preferred local model if needed
                "prompt": f"Give constructive feedback on this resume:\n{resume_text}",
                "stream": False
            },
            timeout=180  # Increased timeout to 180 seconds
        )
        response.raise_for_status()
        data = response.json()
        feedback_text = data.get("response", "No feedback received.")
        # Clean up the feedback text for better display
        feedback_text = feedback_text.strip()
        return {"score": None, "comments": feedback_text}
    except Exception as e:
        return {"score": 0, "comments": f"Error getting feedback: {str(e)}"}

def parse_feedback_response(response):
    # This function parses the AI feedback response and formats it for display.
    score = response.get("score", 0)
    comments = response.get("comments", "")
    formatted_feedback = {
        "score": score,
        "comments": comments  # Already a string, no need to join
    }
    return formatted_feedback