<<<<<<< HEAD
from app import app, db
from flask import flash, redirect, url_for, request, render_template
from app.forms import *
from app.models import Admin



@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login',methods= ['GET','POST'])
def login():
    loginForm = Login()
    if request.method == "GET":
        return render_template('login.html',form=loginForm)

    if request.method == 'POST':
        if loginForm.validate_on_submit():
            username = loginForm.username.data
            password = loginForm.password.data

            if username.lower() in [admin.username.lower() for admin in Admin.query.all()]:
                if password.lower() in [admin.password.lower() for admin in Admin.query.all()]:
                    return render_template('home.html')
                else:
                    flash("PASSWORD INCORRECT")
                    return redirect(url_for('login'))
            else:
                flash("USERNAME INCORRECT")
                return redirect(url_for('login'))


@app.route('/register',methods= ['GET','POST'])
def register():
    registerForm = Register()
    if request.method == "GET":
        return render_template('registration.html',form=registerForm)

    if request.method == 'POST':
        if registerForm.validate_on_submit():
            username = registerForm.username.data
            password = registerForm.password.data
            email = registerForm.email.data
            first_name = registerForm.first_name.data
            last_name = registerForm.last_name.data
            company_name = registerForm.company_name.data
            area_of_business = registerForm.area_of_business.data
            office_address = registerForm.office_address.data
            phone_number = registerForm.phone_number.data
            company_role = registerForm.company_role.data
            num_employees = registerForm.num_employees.data
            num_departments = registerForm.num_departments.data

            if email.lower() in [admin.email.lower() for admin in Admin.query.all()]:
                flash('This email is already exist')
                return redirect(url_for('register'))
            else:
                admin = Admin(username=username,password=password,email=email,first_name=first_name,
                              last_name=last_name,company_name=company_name,area_of_business=area_of_business,
                              office_address=office_address,phone_number=phone_number,company_role=company_role,
                              num_employees=num_employees,num_departments=num_departments)
                db.session.add(admin)
                db.session.commit()
                return render_template('login.html')


@app.route('/form',methods=['GET','POST'])
def form():

=======

>>>>>>> 443cc9ef3e0d0ab3c2fb9285af392e0839cb8a51
