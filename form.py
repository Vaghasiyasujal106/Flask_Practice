from flask import Flask, render_template, request, redirect, url_for, flash, make_response

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For flashing messages

# Route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Example authentication logic
        if username == 'jeni_patel_1000' and not password == '':
            flash('Login successful!', 'success')
            return redirect('/logged')
        else:
            flash('Invalid username or password', 'error')
            return redirect('/logges')
    return render_template('form.html')  # Render the HTML file

@app.route('/logges', methods=['GET','POST'] )
def logges():
    return make_response(render_template('logges.html'))

# Route for a dashboard page (after successful login)
@app.route('/logged', methods=['GET','POST'] )
def logged():
    return make_response(render_template('logged.html'))

app.run(debug=True)