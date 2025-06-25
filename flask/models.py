from flask_sqlalchemy import SQLAlchemy

#initialize oue database and API
db = SQLAlchemy()
 
#created Model 1
class UserModel(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(80))
   phone_number = db.Column(db.Integer)
   prefence = db.Column(db.String(80))

   #What prints when we look at the class
   def __repr__(self):
      return f"User {self.name}, Phone_number {self.phone_number}, Prefence {self.prefence}"
   

#created Model 2
class TableModel(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   user_id = db.Column(db.Integer, primary_key=True)
   capacity = db.Column(db.Integer)
   status = db.Column(db.String, nullable=False, default='pending')

   #What prints when we look at the class
   def __repr__(self):
      return f"Table {self.user_id}, Capacity {self.capacity}, Prefence {self.status}"
   

#created model 3
class ReservationModel(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   user_id = db.Column(db.Integer, primary_key=True)
   table_id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(80))
   number_of_guest = db.Column(db.Integer)
   date = db.Column(db.String,nullable=False)
   time = db.Column(db.String,nullable=False)
   status = db.Column(db.String, nullable=False, default='pending')

   #What prints when we look at the class
   def __repr__(self):
      return f"Reservation {self.name}, User_id{self.user_id}, Table_id{self.table_id}, Number_of_guest {self.number_of_guest}, Date {self.date}, Time {self.time}, Status {self.status} "