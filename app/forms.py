from flask_wtf import *
from wtforms import *
from wtforms.validators import data_required


class Login(FlaskForm):
    username = StringField(label="Username", validators=[data_required()])
    password = PasswordField(label="Password", validators=[data_required()])
    submit = SubmitField()


class Register(FlaskForm):
    username = StringField(label="Username", validators=[data_required()])
    password = PasswordField('Password',
           [validators.DataRequired(),validators.EqualTo('confirm', message='Password must match')])
    confirm = PasswordField("Confirm password")
    email = StringField(label="Email",validators=[data_required(), validators.Email(message="incorrect email format")])
    first_name = StringField(label="First name", validators=[data_required()])
    last_name = StringField(label="Last name", validators=[data_required()])
    company_name = StringField(label="Last name", validators=[data_required()])
    area_of_business = IntegerField(lable="Business Area",validators=[data_required()])
    office_address = StringField(label="Office address", validators=[data_required()])
    phone_number = IntegerField(lable="Phone number",validators=[data_required()])
    company_role = StringField(label="Company role", validators=[data_required()])
    num_employees = IntegerField(lable="employees number",validators=[data_required()])
    num_departments = IntegerField(lable="Departments number",validators=[data_required()])
    submit = SubmitField()

class Form(FlaskForm)