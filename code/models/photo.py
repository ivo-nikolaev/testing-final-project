from db import db

class PhotoModel(db.Model):
    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    photo_name = db.Column(db.String(80))
    data = db.Column(db.LargeBinary)
    visible = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)

    def __init__(self, photo_name, data, visible, user_id):
        self.photo_name = photo_name
        self.data = data
        self.visible = visible
        self.user_id = user_id

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(username = name).first()

    @classmethod
    def find_all_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id = user_id).all()
        

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()