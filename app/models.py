from . import db


class PropertyModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    bedrooms = db.Column(db.Integer)
    description = db.Column(db.String(1000))
    bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(255))
    price = db.Column(db.Numeric(15, 2))
    photo = db.Column(db.String(255))
    property_type = db.Column(db.String(100))

    def __init__(self, title, no_bedrooms, no_bathrooms, description,
                 price, location, property_type, photo):
        super().__init__()

        self.title = title
        self.no_bedrooms = no_bedrooms
        self.no_bathrooms = no_bathrooms
        self.description = description
        self.price = price
        self.location = location
        self.property_type = property_type
        self.photo = photo
