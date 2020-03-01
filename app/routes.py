# <<<<<<< HEAD
from app import app, db
from flask import flash, redirect, url_for, request, render_template
from app.forms import *
from app.models import Admin
from flask_mail import Mail,Message
from .file import File


mail = Mail(app)

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


@app.route('/registration',methods= ['GET','POST'])
def registration():
    register_form = Register()
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
                return redirect(url_for('register'))
            else:
                admin = Admin(username=username,password=password,email=email,first_name=first_name,
                              last_name=last_name,company_name=company_name,area_of_business=area_of_business,
                              office_address=office_address,phone_number=phone_number,company_role=company_role,
                              num_employees=num_employees,num_departments=num_departments)
                db.session.add(admin)
                db.session.commit()
                flash('You have successfully registered, please log in')
                return render_template('login.html')
    return render_template('registration.html',form=register_form)

@app.route('/form',methods=['GET','POST'])
def form():
    pass

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/admin',methods=['GET','POST'])
def admin_panel():
    if request.method == 'GET':
        return render_template('adminpanel.html')

    if request.method == 'POST':
        email = request.form['email']
        file_data = request.form['file']
        file = File(file_data)
        file.readFile()
        
        msg = Message('hey there', recipients=[email])
        msg.html = """<h5> Hello world </h>
                        <p>Hello world first time</p>    
                    """
        mail.send(msg)
    flash('Email was sent successfully')
    return redirect(url_for('admin_panel'))

#=======
#
# >>>>>>> 443cc9ef3e0d0ab3c2fb9285af392e0839cb8a51
