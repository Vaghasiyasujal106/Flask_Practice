from flask import Flask, request, redirect, render_template, url_for, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Directory to save uploaded files
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/", methods=['GET', 'POST'])
def name():
    if request.method == 'POST':
        # Get form data
        username = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        img = request.files.get('img')  # Images are in request.files

        # Validate the form fields
        if not username or not email or not phone or not img or img.filename == '':
            flash("All fields are required, including the image!", "error")
            return render_template('img.html')  # Reload the form with an error

        # Save the uploaded image
        filename = secure_filename(img.filename)
        img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # If validation and saving succeed
        flash("Form submitted successfully!", "success")
        return render_template('successfully.html', username=username, email=email, phone=phone, image=filename)

    return render_template('img.html')  # Render the form template


@app.route("/about")
def about():
    return render_template("about.html")  # Render the about page


if __name__ == "__main__":
    app.run(debug=True)
