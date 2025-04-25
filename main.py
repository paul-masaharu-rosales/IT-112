from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'



@app.route('/')
def home():
    return "<h1>About Me Page</h1>"

@app.route("/about")
def aboutMe():
    return """<p>I am currently a student at North Seattle College and currently pursuing a Full Stack Development 
    certificate. I am currently not sure what I want to do after that but I am keeping my eyes and options open. I grew
    up in Seattle and really love living here. I like to go to parks and beaches, most commonly I will go to Discovery Park 
    or will see some of the japanese gardens that are in south Seattle.</p>"""

@app.route("/fortune")
def fortuneTeller():
    user = request.args.get('user')
    color = request.args.get('color')
    number = request.args.get('number')
    return render_template('assignment3.html', username = user, colorPicked = color, numberPicked = number)

db = SQLAlchemy(app)
class Cars(db.Model):
    id = db.Column('car_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    brand = db.Column(db.String(100))
    mpg = db.Column(db.Float(10))
    cost = db.Column(db.Float(100))

    def __init__(self, name, brand, mpg, cost):
        self.name = name
        self.brand = brand
        self.mpg = mpg
        self.cost = cost



@app.route('/mydatabase', methods = ['GET', 'POST'])
def showMyDatabase():
    if request.method == 'POST':
        return render_template('assignment4.html', cars = Cars.query.all())
    else:
        db.drop_all()
    db.create_all()

    mustang = Cars("Mustang", "Ford", 15.0, 23000)
    viper = Cars("Viper", "Dodge", 11.0, 175000)
    zr1 = Cars("ZR1", "Corvette", 13.0, 125000)
    turbo911 = Cars("911 Turbo", "Porche", 22.0, 225000)

    db.session.add(mustang)
    db.session.add(viper)
    db.session.add(zr1)
    db.session.add(turbo911)
    db.session.commit()
    return render_template('assignment4.html', cars = Cars.query.all())

  #need to add link to details next to each item  
    

if __name__ == '__main__':
    app.run(port=os.getenv("PORT", default=5000))
# to jump back into the env just run : source venv/bin/activate
# to get out of env type in terminal deactivate