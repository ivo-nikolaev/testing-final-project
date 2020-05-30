from flask import send_file
from flask_restful import Resource, reqparse, request 
from werkzeug.datastructures import FileStorage
from flask_jwt import jwt_required, current_identity
from io import BytesIO

from models.photo import PhotoModel
from models.user import UserModel


class PhotoUpload(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('photo_name',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    # parser.add_argument('data',
    #                     type=file,
    #                     required=True,
    #                     help="You must provide a file"
    #                     )
    parser.add_argument('data',
                        type=FileStorage,
                        location='files')
    
    @jwt_required()
    def post(self):
        data = PhotoUpload.parser.parse_args()

        # if PhotoModel.find_by_username(data['photo_name']):
        #     return {"message": "A photo with that name already exists"}, 400

        file = data['data']
        newFile = file.read()

        user_id = current_identity.id

        photo = PhotoModel(data['photo_name'],newFile, user_id)
        photo.save_to_db()

        return {"message": "Picture added succsfully"}, 201

class PhotoGet(Resource):
    @jwt_required()
    def get(self, _id):
        photo = PhotoModel.find_by_id(_id)

        user_id = current_identity.id

        if (photo and photo.user_id == user_id) :
            return send_file(
                BytesIO(photo.data),
                mimetype="image/jpeg")
