#Spezifikation des Eingabe-html-formulars
from wtforms import Form, StringField, SelectField, validators
import math

class InputForm(Form):
    Formula = StringField(
        label='Ausdruck in x',
        default='sin(x)',
        validators=[validators.InputRequired()])
    Domain = StringField(
        label='Intervall: [xmin, xmax]', 
        default='[0, 2*pi]',
        validators=[validators.InputRequired()])
    
