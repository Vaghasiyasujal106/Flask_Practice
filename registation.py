from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session
from flask_sqlalchemy import SQLAlchemy
from passlib.handlers.sha2_crypt import sha256_crypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/mydb'
app.config['SQLALCHEMY_MODIFICATIONS'] = True  # Corrected (boolean value)
db = SQLAlchemy(app)


# Define User model (table structure)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), unique=False, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def info():
    return render_template('home.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    print("inside login")
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        try:
            user = User.query.filter_by(name=name).first() #ye check karega ki database me aisa koi user ka name hya data hai ya nhi( This checks if the username entered by the user exists in the database.)Why: We need to validate the user's credentials. If the user doesn’t exist, it indicates the person hasn’t registered yet, and we handle that later (in the except block).
            pas=user.password #
            if sha256_crypt.verify(password, pas):#Purpose: This compares the password entered by the user with the stored (hashed) password in the database.Why:Plain text passwords are insecure, so we store encrypted passwords in the database.Using sha256_crypt.verify(), we compare the entered password securely with the stored hash.

                session['name']=name  #Purpose: If the password matches, the user is logged in, and their username is stored in the session to track their login state.Why:Storing session['name'] allows the app to remember the user across pages.
                return make_response(render_template('completed.html'))   #if i try to show the next page when i enter the html file in action me muje url deni padegi
            else:
                flash("invalid username/password")#Purpose: If the password is incorrect, or if the user object is None, an error message is displayed.
                return redirect(url_for('login'))
        except:
            flash("please register first")
            return redirect(url_for('logout'))
    return render_template('signin.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        encpassword=sha256_crypt.encrypt(password)   #for password is encrypt password ko safe rakhta hai

        new_user = User(name=name, password=encpassword)  #new user ka data database me stor krta hai ,Ye ek temporary "user" object hai, jo baad me database me save hota hai db.session.commit() ke saath
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('registration done')
            return redirect(url_for('login'))
        except:                      # Handling Non-Existent User:Purpose: If the username doesn’t exist or there’s an error (e.g., user object is None), the code asks the user to register.
            flash('All ready registered.....please logging')  #mene register me uppr database me uniqye=true likha hai yani ye muje bataye ga ki register me ak bar hi data dat sakte ho  varna try block error ko catch karega and batayega already data hai register me
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('name',None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=False)