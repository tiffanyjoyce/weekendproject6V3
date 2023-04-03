from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class productForm(FlaskForm):
    pokemonname = StringField('Pokemon', validators = [DataRequired()])
    submit = SubmitField()