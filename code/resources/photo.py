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
    parser.add_argument('data',
                        type=FileStorage,
                        location='files',
                        required=True,
                        help="You must provide a file"
                        )
    parser.add_argument('visible',
                        type=bool
                        )
    
    @jwt_required()
    def post(self):
        data = PhotoUpload.parser.parse_args()

        file = data['data']
        newFile = file.read()

        user_id = current_identity.id

        photo = PhotoModel(data['photo_name'],newFile, data['visible'], user_id)
        photo.save_to_db()

        return {"message": "Picture added succesfully"}, 201

# It's ment only for the owner of the photo
class PhotoGet(Resource):
    @jwt_required()
    def get(self, _id):
        photo = PhotoModel.find_by_id(_id)

        user_id = current_identity.id

        if (photo and photo.user_id == user_id) :
            return send_file(
                BytesIO(photo.data),
                mimetype="image/jpeg")

#Return a list of all the visible photos' IDs
class PhotosById(Resource):
    def get(self, user_id):
        photos = PhotoModel.find_all_by_user_id(user_id)
        # Get only phots that are set to vissible
        # BUG - need to set visible to INT and check for 0/1, since no BOOL in SQLite
        photos = [p for p in photos if p.visible]
        list_of_ids = []
        for photo in photos:
            list_of_ids.append(photo.id)

        return list_of_ids

# class PhotoGet(Resource):
#     @jwt_required()
#     def get(self, _id):
#         photo = PhotoModel.find_by_id(_id)

#         user_id = current_identity.id

#         if (photo and photo.user_id == user_id) :
#             return send_file(
#                 BytesIO(photo.data),
#                 mimetype="image/jpeg")

# PUT /photo/id - will change name and visibility of the photo
# class PhotoGet(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('photo_name',
#                         type=str,
#                         )
#     parser.add_argument('visibility',
#                         type=int
#     )
#     @jwt_required()
#     def put(self):
#         data = PhotoUpload.parser.parse_args()

#         file = data['data']
#         newFile = file.read()

#         user_id = current_identity.id

#         photo = PhotoModel(data['photo_name'],newFile, user_id)
#         photo.save_to_db()
