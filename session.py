from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For flashing messages and session k liye muje secret_key likhni padegi....

@app.route('/', methods=['GET', 'POST'])
def info():
    return render_template('info.html')  # Login form

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Simple authentication logic9
        if username == 'jeni_patel_1000' and password:
            session['username'] = username  # Save the username in the session
            #flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))  # Redirect to the dashboard
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
    return render_template('info.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:  # Check if the user is logged in
        flash('Login successful!', 'success')
        return render_template('dashboard.html', username=session['username']) #dashboard me loging k bad jo page hoga vo dekhaye ga usme flash message bhi hoga ,logout ka button bhi hoga,profile ka button bhi hoga
    else:
        flash('Please log in first.', 'error')
        return redirect(url_for('login'))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'username' in session:  # Remove username from the session
        return render_template('profile.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)  # Remove username from the session
    flash('You have been logged out.', 'info')
    return redirect(url_for('info'))  # Redirect to login page

if __name__ == '__main__':
    app.run(debug=True)
