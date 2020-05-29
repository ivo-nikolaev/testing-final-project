from flask_restful import Resource, reqparse, request
from werkzeug.datastructures import FileStorage
from models.photo import PhotoModel


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

    def post(self):
        data = PhotoUpload.parser.parse_args()

        # if PhotoModel.find_by_username(data['photo_name']):
        #     return {"message": "A photo with that name already exists"}, 400

        file = data['data']
        newFile = file.read()

        photo = PhotoModel(data['photo_name'],newFile)
        photo.save_to_db()

        return {"message": "Picture added succsfully"}, 201