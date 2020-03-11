import os
import pygal
from app import app, db
from flask import flash, redirect, url_for, request, render_template
from app.forms import *
from app.models import *
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
     #return render_template('dashboard.html')


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
                flash("Invalid username or password",'error')
                return redirect('login')

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
                flash('This email is already exist','error')
                return render_template('registration.html',form=register_form)
            else:
                hashed_password = generate_password_hash(password, method='sha256')
                admin = Admin(username=username,password=hashed_password,email=email,first_name=first_name,
                              last_name=last_name,company_name=company_name,area_of_business=area_of_business,
                              office_address=office_address,phone_number=phone_number,company_role=company_role,
                              num_employees=num_employees,num_departments=num_departments)
                db.session.add(admin)
                db.session.commit()
                flash('You have successfully registered, please log in','success')
                return render_template('login.html',form=login_form)
    return render_template('registration.html',form=register_form)

@app.route('/form/<id>',methods=['GET','POST'])
def form(id):
    if request.method == 'GET':
        questions = Question.query.all()
        return render_template('form.html',questions_list=questions)

    if request.method == 'POST':
        questions = Question.query.all()
        result = Results_Data()
        data = request.form
        for question_id,question_answer in data.items():
            result.admin_id = id
            result.question_id = question_id
            result.result = question_answer
            db.session.add(result)
            db.session.commit()
            result = Results_Data()
    return render_template('form.html',questions_list=questions)

@app.route('/products')
def products():
    return render_template('products.html')


@app.route('/adminpanel',methods=['GET','POST'])
@login_required
def admin_panel():
    if request.method == 'GET':
        one_counting = 0
        two_counting = 0
        three_counting = 0
        four_counting = 0
        five_counting = 0
        charts_list = []
        chart_data = Results_Data.query.filter(Results_Data.admin_id == current_user.id).all()
        question_list = Question.query.all()
        for question in question_list:
            for data in chart_data:
                if question.id == data.question_id:
                    if data.result == 1:
                        one_counting += 1
                    elif data.result == 2:
                        two_counting += 1
                    elif data.result == 3:
                        three_counting += 1
                    elif data.result == 4:
                        four_counting += 1
                    elif data.result == 5:
                        five_counting += 1
            charts_list = create_chart(one_counting,two_counting,three_counting,four_counting,five_counting,question)
            size =len(charts_list)
            one_counting = 0
            two_counting = 0
            three_counting = 0
            four_counting = 0
            five_counting = 0
        print(len(charts_list))
        return render_template('adminpanel.html',chart=charts_list)

    if request.method == 'POST':
        #get email from text input
        email = request.form['email']
        #get file from upload file
        file_data = request.files['file']
        file = File(file_data)

        #read all emails in the file
        email_list = file.read_file()
        if email:  #check if email is empty or not
            msg = Message('hey there', recipients=[email])
            msg.html = """<h5> Hello world </h>
                        <p><a href="http://127.0.0.1:5000/form/%s">Click here</a> to fill the form</p>   
                    """%current_user.id
            mail.send(msg)
            flash('Email was sent successfully','success')
            return redirect(url_for('admin_panel'))
        elif email_list: #check if there are emails in the file
            with mail.connect() as con:
                for email in email_list:
                    msg = Message('Hey there',recipients=[email])
                    msg.html = """
                                <h5>Hello my fellows humans </h5>
                              <p><a href="http://127.0.0.1:5000/form">Click here</a> to fill the form</p>
                               """
                    con.send(msg)
                    flash('Email\'s were sent successfully','success')
                return redirect(url_for('admin_panel'))
        else:
            flash('You must enter email or upload file','error')
            return redirect(url_for('admin_panel'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/tables')
def tables():
    return render_template('tables.html')


def create_chart(one_counting,two_counting,three_counting,four_counting,five_counting,question):
    pie_chart = pygal.Pie()
    pie_chart.title = question.question
    pie_chart.add('Answer - 1', one_counting)
    pie_chart.add('Answer - 2', two_counting)
    pie_chart.add('Answer - 3', three_counting)
    pie_chart.add('Answer - 4', four_counting)
    pie_chart.add('Answer - 5', five_counting)
    return pie_chart.render_data_uri()
