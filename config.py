import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    UPLOAD_FOLDER = 'app/uploads'
    ALLOWED_EXTENSIONS = {'pdf', 'docx'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB limit for uploads

    # Add any other configuration settings as needed
    AI_FEEDBACK_API_URL = os.environ.get('AI_FEEDBACK_API_URL') or 'https://api.example.com/feedback'
    AI_FEEDBACK_API_KEY = os.environ.get('AI_FEEDBACK_API_KEY') or 'your_api_key'