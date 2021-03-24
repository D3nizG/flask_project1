from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import (StringField, TextAreaField, SelectField,
                     IntegerField, DecimalField, SubmitField)
from wtforms.validators import InputRequired


class PropertyForm(FlaskForm):
    property_title = StringField(
        'Property Title', validators=[InputRequired()])

    description = TextAreaField('Description', validators=[InputRequired()])
    no_bedrooms = IntegerField('No. of Rooms', validators=[InputRequired()])
    no_bathrooms = IntegerField(
        'No. of Bathrooms', validators=[InputRequired()])
    price = DecimalField('Price', validators=[InputRequired()])
    property_type = SelectField('Property Type',
                                choices=[
                                    ('house', 'House'),
                                    ('apartment', 'Apartment')
                                ])
    location = StringField(validators=[InputRequired()])
    property_photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'JPG and PNG Images only!')
    ])
    submit = SubmitField("Add Property")
