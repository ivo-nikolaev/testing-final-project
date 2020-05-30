from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.photo import PhotoUpload

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
#This will be changed later
app.secret_key = 'secret'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

# POST url/auth
# {
# 	"username": "test",
# 	"password": "test"
# }
# - Will return a JWT token. 
jwt = JWT(app, authenticate, identity)  # /auth


#POST url/register
# {
# 	"username": "test",
# 	"password": "test",
# 	"email":"test@gmail.com"
# }
# - Will create a new user in the DB
api.add_resource(UserRegister, '/register')

#POST url/photo
# having a form with
# photo_name : "some_name"
# data : example.jpg - really any file at the moment
# will upload the file to the DB
api.add_resource(PhotoUpload, '/photo')


# ##API CALLS

# # GET /auth
# @app.route('/user/', methods=['GET'])
# def get_user():
#     pass
# # POST /user/<user_id>
# @app.route('/user/', metods=['POST'])
# def create_user():
#     pass
# # PUT /user/update
# @app.route('/user/', methods=['PUT'])
# def update_user():
#     pass
# # POST /user/logout
# @app.route('/user/', methods=['DELETE'])
# def delete_user():
#     pass

# #GET /photo/<id> 
# @app.route('/photo/<photo_id>')
# def get_photo(photo_id):
#     pass
# #POST /photo/ 
# @app.route('/photo/', metods=['POST'])
# def add_photo():
#     pass
# #PUT /photo/<id> @
#DELETE /photo/<id>

##PAGES ROUTES

#HTML / - user's home page, whre they can choose to CRUD photos
#HTML /login - a log in form, JWT generation
#HTML /sign up 
#HTML /album/<user_name>


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)