from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import TelField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'development key'  # Secret key for CSRF protection

# Define the form
class LoginForm(FlaskForm):
    name = TelField("Your Name", validators=[DataRequired(message='Please enter your name')])
    submit = SubmitField('Submit')

# Route for the form
@app.route('/', methods=['GET', 'POST'])
def contact():
    form = LoginForm()
    if form.validate_on_submit():  # If the form is valid
        return redirect(url_for('hello'))  # Redirect to the "hello" route
    return render_template('wtform.html', form=form)

# Route for the "Hello" page
@app.route('/hello', methods=['GET', 'POST'])  # Fixed the argument to 'methods'
def hello():
    if request.method == 'POST':
        return render_template('hello.html')
    return "Hello!"  # Default response for GET requests

if __name__ == '__main__':
    app.run(debug=True)


