from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    Nombre = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    Apellido = StringField('Apellido', validators=[DataRequired(), Length(min=2, max=25)])
    Edad = IntegerField('Edad', validators=[DataRequired()])
    Altura = StringField('Altura', validators=[DataRequired(), Length(min=2, max=20)])
    Calorias = IntegerField('Calorias', validators=[DataRequired()])
    Peso_act = StringField('Peso Actual', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    Miembro = StringField('Miembro', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Registrame')



class LoginForm(FlaskForm):
    User = StringField('User', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Iniciar Sesión')