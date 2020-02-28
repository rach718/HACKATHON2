
<<<<<<< HEAD

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(40),nullable=False)
    email = db.Column(db.DateTime, default=datetime.now, nullable=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    company_name = db.Column(db.String(30), nullable=False)
    area_of_business = db.Column(db.string(40), nullable=False)
    office_address = db.Column(db.String(40), nullable=False)
    phone_number = db.Column(db.Int(25),nullable=False)
    company_role = db.Column(db.String(20), nullable=False)
    num_employees = db.Column(db.Int(30), nullable=False)
    num_departments = db.Column(db.Int(30), nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.now, nullable=True)

    def __repr__(self):
        return f"<Admin: {self.username}>"


class results_data(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    admin_id = db.Column(db.Integer,db.ForeignKey("Admin.id"),nullable=False)

=======
>>>>>>> 443cc9ef3e0d0ab3c2fb9285af392e0839cb8a51
