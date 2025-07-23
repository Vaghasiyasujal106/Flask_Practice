from flask import Flask

# Initialize the Flask app with the name 'MyApp'
app = Flask("MyApp")

@app.route("/login")
def home():
    return "Welcome to MyApp!"

@app.route("/about")
def about():
    return "sujal is here."


app.run(debug=True)
