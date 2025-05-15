# resume_parser.py provides functions to extract text from PDF and DOCX resumes
from PyPDF2 import PdfReader  # For reading PDF files
from docx import Document     # For reading DOCX files

def parse_pdf(file_path):
    """
    Extracts text from a PDF file.
    Args:
        file_path (str): Path to the PDF file.
    Returns:
        str: Extracted text from the PDF file.
    """
    text = ""
    with open(file_path, "rb") as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def parse_docx(file_path):
    """
    Extracts text from a DOCX file.
    Args:
        file_path (str): Path to the DOCX file.
    Returns:
        str: Extracted text from the DOCX file.
    """
    text = ""
    doc = Document(file_path)
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text.strip()

def parse_resume(file_path):
    """
    Extracts text from a resume file (PDF or DOCX).
    Args:
        file_path (str): Path to the uploaded resume file.
    Returns:
        str: Extracted text from the resume, or an error message if unsupported.
    """
    if file_path.lower().endswith('.pdf'):
        # Open and read PDF file
        reader = PdfReader(file_path)
        text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
        return text
    elif file_path.lower().endswith('.docx'):
        # Open and read DOCX file
        doc = Document(file_path)
        text = "\n".join(para.text for para in doc.paragraphs)
        return text
    else:
        # Unsupported file type
        return "Unsupported file format."