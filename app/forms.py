from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired


class AddressForm(FlaskForm):
    street = StringField('Street Address: ')
    city = StringField('City: ')
    state = StringField('State: ')
    zip = StringField('Zip: ')
    submit_Address = SubmitField('Submit')
