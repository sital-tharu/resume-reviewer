import requests  # For making HTTP requests to the Ollama API
import markdown2  # ✅ Add this to convert markdown to HTML

def get_ai_feedback(resume_text):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": f"Give constructive feedback on this resume:\n{resume_text}",
                "stream": False
            },
            timeout=180
        )
        response.raise_for_status()
        data = response.json()
        feedback_text = data.get("response", "No feedback received.").strip()

        # ✅ Convert markdown to HTML
        feedback_html = markdown2.markdown(feedback_text)

        return {"score": None, "comments": feedback_html}  # Return HTML-formatted comments
    except Exception as e:
        return {"score": 0, "comments": f"Error getting feedback: {str(e)}"}

def parse_feedback_response(response):
    score = response.get("score", 0)
    comments = response.get("comments", "")
    formatted_feedback = {
        "score": score,
        "comments": comments
    }
    return formatted_feedback
