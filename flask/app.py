from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from models import db
from resources import Users
from resources import Tables
from resources import Reservations

app = Flask(__name__)

#connect to DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#activates the db and api
db.init_app(app)

#Add for API
api = Api(app)

#API routes for veiwing all the reservations 
api.add_resource(Users,Tables, Reservations, '/api/users','/api/tables','/api/reservations')
with app.app_context():
  db.create_all()

if __name__ == '__main__':
   app.run(debug=True)