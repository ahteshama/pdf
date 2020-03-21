import os

from flask import Flask, current_app, request, send_from_directory
import pikepdf
import uuid

app = Flask(__name__)

UNLOCKED_FILE_DEST = 'static/unlocked'


# file
@app.route('/unlock-pdf', methods=['POST'])
def unlock_pdf():
    pdf_unlocked = pikepdf.open(request.files['file'])
    filename = str(uuid.uuid4())
    destination_file_path = os.path.join(current_app.root_path, UNLOCKED_FILE_DEST) + '/' + filename + '.pdf'
    pdf_unlocked.save(destination_file_path)
    return {'file': '/download-pdf/' + filename + '.pdf'}


@app.route('/download-pdf/<filename>', methods=['GET'])
def download_pdf(filename):
    destination_file_path = os.path.join(current_app.root_path, UNLOCKED_FILE_DEST)
    return send_from_directory(directory=destination_file_path, filename=filename)
