import os
from app import app, db
from flask import flash, redirect, url_for, request, render_template
from app.forms import *
from app.models import Admin
from flask_mail import Mail,Message
from .file import File
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


mail = Mail(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login',methods= ['GET','POST'])
def login():
    loginForm = Login()
    if request.method == "GET":
        return render_template('login.html',form=loginForm)

    if request.method == 'POST':
        if not loginForm.validate_on_submit():
            user = Admin.query.filter_by(username=loginForm.username.data).first()
            if user:
                if check_password_hash(user.password, loginForm.password.data):
                    #login_user(user, remember=loginForm.remember.data)
                    login_user(user)
                    return redirect(url_for('admin_panel'))
                flash("Invalid username or password")
                return redirect('login')
            # username = loginForm.username.data
            # password = loginForm.password.data

            # if username.lower() in [admin.username.lower() for admin in Admin.query.all()]:
            #     if password.lower() in [admin.password.lower() for admin in Admin.query.all()]:
            #         return render_template('home.html')
            #     else:
            #         flash("PASSWORD INCORRECT")
            #         return redirect(url_for('login'))
            # else:
            #     flash("USERNAME INCORRECT")
            #     return redirect(url_for('login'))
            flash('User doesn\'t exist')
            return redirect('login')
    return render_template('login.html',form=loginForm)

@app.route('/registration',methods= ['GET','POST'])
def registration():
    register_form = Register()
    login_form = Login()
    if request.method == "GET":
        return render_template('registration.html',form=register_form)

    if request.method == 'POST':
        if not register_form.validate():
            username = register_form.username.data
            password = register_form.password.data
            email = register_form.email.data
            first_name = register_form.first_name.data
            last_name = register_form.last_name.data
            company_name = register_form.company_name.data
            area_of_business = register_form.area_of_business.data
            office_address = register_form.office_address.data
            phone_number = register_form.phone_number.data
            company_role = register_form.company_role.data
            num_employees = register_form.num_of_employees.data
            num_departments = register_form.num_of_departments.data

            if email.lower() in [admin.email.lower() for admin in Admin.query.all()]:
                flash('This email is already exist')
                return render_template('registration.html',form=register_form)
            else:
                hashed_password = generate_password_hash(password, method='sha256')
                admin = Admin(username=username,password=hashed_password,email=email,first_name=first_name,
                              last_name=last_name,company_name=company_name,area_of_business=area_of_business,
                              office_address=office_address,phone_number=phone_number,company_role=company_role,
                              num_employees=num_employees,num_departments=num_departments)
                db.session.add(admin)
                db.session.commit()
                flash('You have successfully registered, please log in')
                return render_template('login.html',form=login_form)
    return render_template('registration.html',form=register_form)

@app.route('/form',methods=['GET','POST'])
def form():
    pass

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/admin',methods=['GET','POST'])
@login_required
def admin_panel():
    if request.method == 'GET':
        return render_template('adminpanel.html')

    if request.method == 'POST':
        email = request.form['email']
        file_data = request.files['file']
        file = File(file_data)
        email_list = file.read_file()
        if email:
            msg = Message('hey there', recipients=[email])
            msg.html = """<h5> Hello world </h>
                        <p>Hello world first time</p>    
                    """
            mail.send(msg)
            flash('Email was sent successfully')
            return redirect(url_for('admin_panel'))
        else:
            with mail.connect() as con:
                for email in email_list:
                    msg = Message('Hey there',recipients=[email])
                    msg.html = """
                                <h5>Hello my fellows humans </h5>
                                <b> This message from AI robotics </b>
                                    <h1>You have been hacked! </h1>
                               """
                    con.send(msg)
                    flash('Email\'s were sent successfully')
                return redirect(url_for('admin_panel'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))