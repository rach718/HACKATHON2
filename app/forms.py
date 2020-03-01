from flask_wtf import *
from wtforms import *
from wtforms.validators import (data_required,EqualTo)


class Login(FlaskForm):
    username = StringField(label="Username", validators=[data_required()])
    password = PasswordField(label="Password", validators=[data_required()])
    submit = SubmitField()


class Register(FlaskForm):
    username = StringField(label="Username", validators=[data_required()])
    password = PasswordField('Password', validators=[data_required()])
    confirm = PasswordField('Repeat Password',validators=[EqualTo(password, message='Passwords must match.')])
    email = StringField(label="Email",validators=[data_required(), validators.Email(message="incorrect email format")])
    first_name = StringField(label="First name", validators=[data_required()])
    last_name = StringField(label="Last name", validators=[data_required()])
    company_name = StringField(label="Company name", validators=[data_required()])
    area_of_business = IntegerField(label="Business Area",validators=[data_required()])
    office_address = StringField(label="Office address", validators=[data_required()])
    phone_number = IntegerField(label="Phone number",validators=[data_required()])
    company_role = StringField(label="Company role", validators=[data_required()])
    num_of_employees = IntegerField(label="employees number",validators=[data_required()])
    num_of_departments = IntegerField(label="Departments number",validators=[data_required()])

    recaptcha = RecaptchaField()
    submit = SubmitField()

class Form(FlaskForm):
    pass
