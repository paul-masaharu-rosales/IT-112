from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'




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



@app.route('/mydatabase')
def showMyDatabase():

    return render_template('assignment4.html', cars = Cars.query.all())

@app.route('/carsDB/<car_id>')
def getDetails(car_id):
    car = Cars.query.filter_by(id = car_id).first()
    
    return render_template('displayAssignment4.html', name = car.name, brand = car.brand, mpg = car.mpg, cost = car.cost)


class Houses(db.Model):
    id = db.Column('house_id', db.Integer, primary_key = True)
    owner = db.Column(db.String(100))
    address = db.Column(db.String(100))
    sellPrice = db.Column(db.Integer)
    boughtPrice = db.Column(db.Integer)
    yearFirstBought = db.Column(db.Integer)
    def __init__(self, owner, address, boughtPrice, sellPrice, yearFirstBought):
        self.owner = owner
        self.address = address
        self.boughtPrice = boughtPrice
        self.sellPrice = sellPrice
        self.yearFirstBought = yearFirstBought

    @property
    def serialize(self):
        return {
            'id': self.id,
            'owner' : self.owner,
            'address': self.address,
            'boughtPrice' : self.boughtPrice,
            'sellPrice' : self.sellPrice,
            'yearFirstBought': self.yearFirstBought

        }

@app.route('/housesDB/return')
def getData():    
    try:
        return jsonify([houses.serialize for houses in Houses.query.all()]), 200
    except Exception:
        return app.response_class(response={"status":"failure"}, status=500, mimetype="application/json")

@app.post('/housesDB/addHouse')
def addHouse():
    data = request.get_json()

    try: 
        house = Houses(owner=data['owner'], address=data['address'], boughtPrice=data['boughtPrice'], sellPrice=data['sellPrice'], yearFirstBought=data['yearFirstBought'])
        db.session.add(house)
        db.session.commit()
        return jsonify({"status" : "success"})
    except Exception:
        return app.response_class(response={"status" : "failure"}, status=500, mimetype="application/json")

    


if __name__ == '__main__':
    app.run(port=os.getenv("PORT", default=5000))
# to jump back into the env just run : source venv/bin/activate
# to get out of env type in terminal deactivate