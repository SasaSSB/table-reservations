from flask.app import app,db

#Database  created
with app.app_context():
  db.create_all()