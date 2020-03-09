from app import db
from datetime import datetime
from flask_login import UserMixin

class Admin(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(40), nullable=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    company_name = db.Column(db.String(30), nullable=False)
    area_of_business = db.Column(db.String(40), nullable=False)
    office_address = db.Column(db.String(40), nullable=False)
    phone_number = db.Column(db.Integer,nullable=False)
    company_role = db.Column(db.String(20), nullable=False)
    num_employees = db.Column(db.Integer, nullable=False)
    num_departments = db.Column(db.Integer, nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.now, nullable=True)

    def __repr__(self):
        return f"<Admin: {self.username}>"


class results_data(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    admin_id = db.Column(db.Integer,db.ForeignKey(Admin.id),nullable=False)


