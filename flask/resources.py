from flask_restful import Resource, reqparse, fields, marshal_with 
from models import db, ReservationModel

#Varibles for reservationFields
reservationFields = {
   'id': fields.Integer,
   'name': fields.String,
   'number_of_guest': fields.Integer,
   'date': fields.String,
   'time': fields.String,
   'status': fields.String,
}

reservation_panams = reqparse.RequestParser()
reservation_panams.add_argument('name', type=str, required=True)
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
      reservation = ReservationModel (name=params.get('name'), number_of_guest=params.get('number_of_guest'), date=params.get('date'),time=params.get('time'), status=params.get('status'))

      db.session.add(reservation)
      db.session.commit()
      return reservation
   
   
   #Update will happen on the existing reservations
   @marshal_with(reservationFields)
   def put(self):
      params = reservation_panams.parse_args()
      reservation_id = params.get('id')
      reservation = ReservationModel.query.get(reservation_id)    
      
      reservation.name = params.get('name')
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
      movie = ReservationModel.query.get(reservation_id)

      db.session.delete(movie)
      db.session.commit()
      return ReservationModel.query.all()