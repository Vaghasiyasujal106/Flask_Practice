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
            return redirect('/flash-msg')
        else:
            flash('Invalid username or password', 'error')
            return redirect('/mine')
    return render_template('form.html')  # Render the HTML file

# Route for a flash-msg page (after successful login)
@app.route('/flash-msg', methods=['GET', 'POST'])
def flash_msg():  # Changed from "flash" to "flash_msg"
    return make_response(render_template('flash-msg.html'))


@app.route('/mine', methods=['GET','POST'] )
def mine():
    return make_response(render_template('mine.html'))

app.run(debug=True)