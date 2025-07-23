from flask import Flask, render_template, request, redirect, make_response, url_for

app = Flask(__name__)

# Route for login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')  # Get the username from the form
        if username:  # If username is provided
            # Create a response and set a cookie
            response = make_response(redirect('/success'))  # Redirect to success page
            response.set_cookie('username', username, max_age=7*24*60*60)  # Save username for 7 days
            return response
        else:
            return "Please enter a username!"  # Handle empty username

    return render_template('cookies.html')  # Render the login page for GET requests


# Route for success page
@app.route('/success')
def success():
    username = request.cookies.get('username')  # Retrieve the username from cookies
    if username:  # If username exists in cookies
        return f"""
        <h1>Username successfully saved!</h1>
        
        <a href="/profile"><button>Go to Profile</button></a>
        """
    else:  # If no username in cookies, redirect to login page
        return redirect('/')


# Route for profile page
@app.route('/profile')
def profile():
    username = request.cookies.get('username')  # Retrieve the username from cookies
    if username:  # If username exists in cookies
        return f"""
        <h1>Welcome to your profile!</h1>
        <p>This is your secure profile page.</p>
        <a href="/"><button>Logout</button></a>
        """
    else:  # If no username in cookies, redirect to login page
        return redirect('/')


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
