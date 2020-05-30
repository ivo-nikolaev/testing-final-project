from db import db

class PhotoModel(db.Model):
    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    photo_name = db.Column(db.String(80))
    data = db.Column(db.LargeBinary)
    user_id = db.Column(db.Integer)

    # def __init__(self, photo_name, data, user_id):
    #     self.user = user
    #     self.data = data
    #     self.user_id = user_id

    def __init__(self, photo_name, data):
        self.photo_name = photo_name
        self.data = data

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    # price = db.Column(db.Float(precision=2))

    # store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    # store = db.relationship('StoreModel')

    # def __init__(self, name, price, store_id):
    #     self.name = name
    #     self.price = price
    #     self.store_id = store_id

    # def json(self):
    #     return {'name': self.name, 'price': self.price}

    # @classmethod
    # def find_by_name(cls, name):
    #     return cls.query.filter_by(name=name).first()

    # def delete_from_db(self):
    #     db.session.delete(self)
    #     db.session.commit()