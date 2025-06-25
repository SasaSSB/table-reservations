from flask_restful import Resource, reqparse, fields, marshal_with 
from models import db, ReservationModel
from models import db, UserModel
from models import db, TableModel


#Varibles for userFields
userFields = {
   'id': fields.Integer,
   'name': fields.String,
   'phone_number': fields.Integer,
   'prefence': fields.String,
}

user_panams = reqparse.RequestParser()
user_panams.add_argument('name', type=str)
user_panams.add_argument('phone_number', type=int )
user_panams.add_argument('prefence', type=str , required = True)

#Mainly uses the CRUD Post , Put and Delete
class Users(Resource):
   #Get all data 
   @marshal_with(userFields)
   def get(self):
      user = UserModel.query.all()
      return user
   
    #Adds a resource when sending a POST
   @marshal_with(userFields)
   def post(self):
      #will parse the dta from the body request
      params = user_panams.parse_args()
      user = UserModel (name=params.get('name'),  phone_number=params.get('phone_number'), prefence=params.get('prefence'))
      db.session.add(user)
      db.session.commit()
      return user, 201
   
   
   #Update will happen on the existing Users
   @marshal_with(userFields)
   def put(self):
      params = user_panams.parse_args()
      user_id = params.get('id')
      user = UserModel.query.get(user_id)    
      
      user.name = params.get('name')
      user.phone_number = params.get('phone_number')
      user.prefence = params.get('prefence')

      db.session.commit()
      return user
   
   #Delete the existing resource when getting the information from GET to add to the body
   @marshal_with(userFields)
   def delete(self):
      params = user_panams.parse_args()
      user_id = params.get('id')
      user = UserModel.query.get(user_id)

      db.session.delete(user)
      db.session.commit()
      return UserModel.query.all()


#Varibles for tableFields
tableFields = {
   'id': fields.Integer,
   'user_id': fields.Integer,
   'capacity': fields.Integer,
}

table_panams = reqparse.RequestParser()
table_panams.add_argument('user_id', type=str)
table_panams.add_argument('capacity', type=int )

#Mainly uses the CRUD Post , Put and Delete
class Tables(Resource):
   #Get all data 
   @marshal_with(tableFields)
   def get(self):
      table = TableModel.query.all()
      return table
   
    #Adds a resource when sending a POST
   @marshal_with(tableFields)
   def post(self):
      #will parse the dta from the body request
      params = table_panams.parse_args()
      table = TableModel (user_id=params.get('user_id'),capacity=params.get('capacity'))
      db.session.add(table)
      db.session.commit()
      return table, 201
   
   
   #Update will happen on the existing Users
   @marshal_with(tableFields)
   def put(self):
      params = table_panams.parse_args()
      table_id = params.get('id')
      table = TableModel.query.get(table_id)    
      
      table.user_id = params.get('user_id')
      table.capacity = params.get('capacity')

      db.session.commit()
      return table
   
   #Delete the existing resource when getting the information from GET to add to the body
   @marshal_with(tableFields)
   def delete(self):
      params = table_panams.parse_args()
      table_id = params.get('id')
      table = TableModel.query.get(table_id)

      db.session.delete(table)
      db.session.commit()
      return TableModel.query.all()


#Varibles for reservationFields
reservationFields = {
   'id': fields.Integer,
   'user_id': fields.Integer,
   'table_id': fields.Integer,
   'name': fields.String,
   'number_of_guest': fields.Integer,
   'date': fields.String,
   'time': fields.String,
   'status': fields.String,
}

reservation_panams = reqparse.RequestParser()
reservation_panams.add_argument('name', type=str)
reservation_panams.add_argument('user_id', type=int )
reservation_panams.add_argument('table_id', type=int )
reservation_panams.add_argument('number_of_guest', type=int )
reservation_panams.add_argument('date', type=str , required = True)
reservation_panams.add_argument('time', type=str, required=True)
reservation_panams.add_argument('status', type= str , required=True)

#Mainly uses the CRUD Post , Put and Delete
class Reservations(Resource):
   #Get all data 
   @marshal_with(reservationFields)
   def get(self):
      reservation = ReservationModel.query.all()
      return reservation
   
    #Adds a resource when sending a POST
   @marshal_with(reservationFields)
   def post(self):
      #will parse the dta from the body request
      params = reservation_panams.parse_args()
      reservation = ReservationModel (name=params.get('name'),  user_id=params.get('user_id'), table_id=params.get('table_id'),number_of_guest=params.get('number_of_guest'), date=params.get('date'),time=params.get('time'), status=params.get('status'))

      db.session.add(reservation)
      db.session.commit()
      return reservation, 201
   
   
   #Update will happen on the existing reservations
   @marshal_with(reservationFields)
   def put(self):
      params = reservation_panams.parse_args()
      reservation_id = params.get('id')
      reservation = ReservationModel.query.get(reservation_id)    
      
      reservation.name = params.get('name')
      reservation.userid = params.get('userid')
      reservation.tableid = params.get('tableid')
      reservation.number_of_guest = params.get('number_of_guest')
      reservation.date = params.get('date')
      reservation.time = params.get('time')
      reservation.status = params.get('status')

      db.session.commit()
      return reservation
   
   #Delete the existing resource when getting the information from GET to add to the body
   @marshal_with(reservationFields)
   def delete(self):
      params = reservation_panams.parse_args()
      reservation_id = params.get('id')
      reservation = ReservationModel.query.get(reservation_id)

      db.session.delete(reservation)
      db.session.commit()
      return ReservationModel.query.all()