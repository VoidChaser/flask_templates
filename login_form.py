from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    astro_id = StringField('Id астронавта', validators=[DataRequired()])
    astro_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    captain_id = StringField('Id капитана', validators=[DataRequired()])
    captain_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')