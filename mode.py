from flask import Flask, request, make_response, render_template

app = Flask(__name__)

# Home Route: Render the page with the current theme
@app.route('/')
def home():
    # Get the 'theme' cookie (default to 'light')
    theme = request.cookies.get('theme', 'light')
    return render_template('mode.html', theme=theme)

# Route to toggle the theme and reload the page
@app.route('/toggle-theme')
def toggle_theme():
    # Get the current theme
    current_theme = request.cookies.get('theme', 'light')
    # Toggle the theme
    new_theme = 'dark' if current_theme == 'light' else 'light'

    # Set the new theme in the cookie
    response = make_response("", 302)  # Redirect back to the home page
    response.set_cookie('theme', new_theme, max_age=30*24*60*60)  # Cookie valid for 30 days
    response.headers['Location'] = '/'  # Redirect to the home page

    return response

if __name__ == '__main__':
    app.run(debug=True)
