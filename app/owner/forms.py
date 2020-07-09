from wtforms import Form, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, length, NumberRange


class OwnerForm(Form):
    name = StringField('Name', [DataRequired(), length(2, 20, 'name must be 1-20 symbols'), ])
    age = IntegerField('Age', [DataRequired(), NumberRange(7, 120, 'age must be 1-120')])
    city = StringField('City', [DataRequired(), length(2, 20, 'name must be 1-20 symbols'), ])
    save = SubmitField('Save')


class PetForm(Form):
    name = StringField('Name', [DataRequired(), length(1, 20, 'name must be 1-20 symbols'), ])
    age = IntegerField('Age', [DataRequired(), NumberRange(1, 100, 'age must be 1-120')])
    type = StringField('Type', [DataRequired(), length(1, 20, 'name must be 1-20 symbols'), ])
    save = SubmitField('Save')
