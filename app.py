from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'sample_data'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    company_name = db.Column(db.String(100), nullable=True)
    address= db.Column(db.String(100), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(100), nullable=True)
    zip = db.Column(db.Integer, nullable=True)
    phone1= db.Column(db.String(100), nullable=True)
    phone2 = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    department = db.Column(db.String(100), nullable=True)
    
    def json(self):
        return {'first_name':self.first_name,
                'last_name': self.last_name,
                'company_name': self.company_name,
                'address': self.address,
                'city': self.city,
                'state': self.state,
                'zip': self.zip,
                'phone1': self.phone1,
                'phone2': self.phone2,
                'email': self.email,
                'department': self.department,
                'id': self.id}

db.create_all()

# create a user
@app.route('/users', methods=['POST'])
def create_user():
  try:
    data = request.get_json()
    new_user = User(first_name=data['first_name'],
                    last_name=data['last_name'],
                    company_name=data['company_name'],
                    address=data['address'],
                    city=data['city'],
                    state=data['state'],
                    zip=data['zip'],
                    phone1=data['phone1'],
                    phone2=data['phone2'],
                    email=data['email'],
                    department=data['department'] )
    db.session.add(new_user)
    db.session.commit()
    return make_response(jsonify({'message': 'user created'}), 201)
  except Exception as e:
    return make_response(jsonify({'message': 'error creating user'}), 500)

# get all users
@app.route('/users', methods=['GET'])
def get_users():
  try:
    users = User.query.all()
    return make_response(jsonify([user.json() for user in users]), 200)
  except Exception as  e:
    return make_response(jsonify({'message': 'error getting users'}), 500)

# get a user by id
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      return make_response(jsonify({'user': user.json()}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error getting user'}), 500)

# update a user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      data = request.get_json()
      user.first_name=data['first_name'],
      user.last_name=data['last_name'],
      user.company_name=data['company_name'],
      user.address=data['address'],
      user.city=data['city'],
      user.state=data['state'],
      user.zip=data['zip'],
      user.phone1=data['phone1'],
      user.phone2=data['phone2'],
      user.email=data['email'],
      user.department=data['department'] 
      db.session.commit()
      return make_response(jsonify({'message': 'user updated'}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error updating user'}), 500)
