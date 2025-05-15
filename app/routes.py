from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from app.utils.resume_parser import parse_resume
from app.utils.ai_feedback import get_ai_feedback

app = Blueprint('app', __name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '' or not allowed_file(file.filename):
        return redirect(request.url)
    
    # Automatically create the uploads folder if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    
    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    parsed_content = parse_resume(file_path)
    ai_feedback = get_ai_feedback(parsed_content)

    return render_template('result.html', feedback=ai_feedback, content=parsed_content)