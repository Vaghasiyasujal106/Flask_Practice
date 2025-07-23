from flask import Flask, request, render_template, flash, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Directory to save uploaded files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the upload folder exists
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def upload():
    return render_template('upload.html')  # Load the file upload form

@app.route("/upload", methods=['POST'])
def handle_upload():
    if 'file' not in request.files:  # Ensure a file was uploaded
        flash('No file part', 'error')
        return redirect(url_for('upload'))

    file = request.files['file']

    if file.filename == '':  # Check if a file was selected
        flash('No selected file', 'error')
        return redirect(url_for('upload'))

    # Save the file securely to the UPLOAD_FOLDER
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
    file.save(file_path)

    # Render the success page
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)

