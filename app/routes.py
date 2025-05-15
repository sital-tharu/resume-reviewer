# routes.py defines the main routes and logic for the Flask app
from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from app.utils.resume_parser import parse_resume  # Import resume parsing function
from app.utils.ai_feedback import get_ai_feedback  # Import AI feedback function

app = Blueprint('app', __name__)  # Create a Flask blueprint for modular routing

UPLOAD_FOLDER = 'uploads'  # Folder to store uploaded files
ALLOWED_EXTENSIONS = {'pdf', 'docx'}  # Allowed file extensions

def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    """
    Render the upload form for the user to submit a resume.
    """
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle the file upload, parse the resume, get AI feedback, and render the result page.
    """
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '' or not allowed_file(file.filename):
        return redirect(request.url)
    
    # Automatically create the uploads folder if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    
    filename = secure_filename(file.filename)  # Sanitize the filename
    file_path = os.path.join(UPLOAD_FOLDER, filename)  # Full path for saving
    file.save(file_path)  # Save the uploaded file

    parsed_content = parse_resume(file_path)  # Extract text from the resume
    ai_feedback = get_ai_feedback(parsed_content)  # Get feedback from the AI

    return render_template('result.html', feedback=ai_feedback, content=parsed_content)  # Show results