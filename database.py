from flask import Flask,render_template,request
from flask_mysqldb import MySQL

# Initialize the Flask app with the name 'MyApp'
app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='mydb'
mysql = MySQL(app)

@app.route("/")
def index():
    firstname="sujal"
    lastname="vaghasiya"
    cur=mysql.connection.cursor()
    cur.execute('INSERT INTO user(fname,lname) VALUES (%s,%s)',(firstname,lastname))
    mysql.connection.commit()
    cur.close()
    return "success"

app.run(debug=True)