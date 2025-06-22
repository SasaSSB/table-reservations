from flask_sqlalchemy import SQLAlchemy

#initialize oue database and API
db = SQLAlchemy()

#created model
class ReservationModel(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(80), nullable=False)
   number_of_guest = db.Column(db.Integer)
   date = db.Column(db.String,nullable=False)
   time = db.Column(db.String,nullable=False)
   status = db.Column(db.String, nullable=False, default='pending')

   #What prints when we look at the class
   def __repr__(self):
      return f"Reservation {self.name}, Number_of_guest {self.number_of_guest}, Date {self.date}, Time {self.time}, Status {self.status} "