from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Correct configuration for database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/mydb'
app.config['SQLALCHEMY_MODIFICATIONS'] = True  # Corrected (boolean value)
db = SQLAlchemy(app)


# Define User model (table structure)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    gmail = db.Column(db.String(120), unique=True, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    username='sujal'
    gmail='sujalvaghasiya053@gmail.com'

    new_user = User(username='username', gmail='gmail')  # email not gmail

    db.session.add(new_user)                  #iss line se instance query finde hogi
    db.session.commit()
    return 'success'

if __name__ == '__main__':
    app.run(debug=True)
