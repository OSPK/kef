from app import db

class Universities(db.Model):
    __tablename__ = 'universities'
    id = db.Column(db.Integer, primary_key=True)
    uni_name = db.Column(db.String(512), nullable=False)
    city = db.Column(db.String(512), nullable=False)
    province = db.Column(db.String(512), nullable=False)
    pub_pri = db.Column(db.String(32), nullable=False)
    website = db.Column(db.String(512))
    govt = db.Column(db.String(512), nullable=False)
    campuses = db.Column(db.Integer)

    # def __init__(self, username, email):
    #     self.username = username
    #     self.email = email

    # def __repr__(self):
    #     return '<User %r>' % self.username

class Programs(db.Model):
    __tablename__ = 'programs'
    id = db.Column(db.Integer, primary_key=True)
    uni_id = db.Column(db.Integer)
    degree = db.Column(db.Text())
    title = db.Column(db.Text())
    eligibility = db.Column(db.Text())
    institution_name = db.Column(db.Text())
    complation_requirement = db.Column(db.Text())
    scope = db.Column(db.Text())
    fees = db.Column(db.Text())
    scholarship = db.Column(db.Text())
    duration = db.Column(db.Text())
    credit_hours = db.Column(db.Text())
    teaching_system = db.Column(db.Text())
    seats = db.Column(db.Text())
    shift = db.Column(db.Text())
    session = db.Column(db.Text())
    regular_private = db.Column(db.Text())
    department = db.Column(db.Text())
    faculty = db.Column(db.Text())
    course_outline = db.Column(db.Text())
    campus = db.Column(db.Text())
    hec_ranking = db.Column(db.Text())
    hostel_facility = db.Column(db.Text())
    contact = db.Column(db.Text())
    location = db.Column(db.Text())
    affiliation = db.Column(db.Text())
    lectures_notes = db.Column(db.Text())
    reference_sites = db.Column(db.Text())
    web = db.Column(db.Text())
    alumni = db.Column(db.Text())
    city = db.Column(db.Text())
    district = db.Column(db.Text())
    province = db.Column(db.Text())
    institute_type = db.Column(db.Text())

    # def __init__(self, username, email):
    #     self.username = username
    #     self.email = email

    # def __repr__(self):
    #     return '<User %r>' % self.username