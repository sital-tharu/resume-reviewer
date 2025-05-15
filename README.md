# Flask Resume App

This project is a web application built using Flask that allows users to upload their resumes, parse the content, obtain AI feedback, and display it on a simple frontend.

## Features

- User-friendly interface for uploading resumes.
- Resume parsing functionality for PDF and DOCX formats.
- Integration with an AI feedback service to provide insights on resumes.
- Display of parsed content and AI feedback in a readable format.

## Project Structure

```
flask-resume-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── templates
│   │   ├── base.html
│   │   ├── upload.html
│   │   └── result.html
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       └── scripts.js
│   ├── utils
│   │   ├── ai_feedback.py
│   │   └── resume_parser.py
│   └── uploads
├── tests
│   ├── __init__.py
│   └── test_routes.py
├── requirements.txt
├── config.py
├── run.py
└── README.md
```

## Usage

1. Run the application: python run.py
   
2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Use the upload form to submit your resume and receive AI feedback.
