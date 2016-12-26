from app import db
from flask_login import UserMixin
from werkzeug import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, primary_key=True)
    password = db.Column(db.String(264))

    def __init__(self, username=None, password=None):
        if username is not None:
            self.username = username
        if password is not None:
            self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        if self.password is None:
            return check_password_hash('', password) #need to improve this
        return check_password_hash(self.password, password)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.username

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False


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
    posts = db.relationship('Posts', backref='university', lazy='dynamic')
    programs = db.relationship('Programs', backref='university', lazy='dynamic')
    colleges = db.relationship('Colleges', backref='university', lazy='dynamic')

    # def __init__(self, username, email):
    #     self.username = username
    #     self.email = email

    def __repr__(self):
        return self.uni_name

class Colleges(db.Model):
    __tablename__ = 'colleges'
    id = db.Column(db.Integer, primary_key=True)
    college_name = db.Column(db.String(512), nullable=False)
    university_id = db.Column(db.Integer, db.ForeignKey('universities.id'))
    city = db.Column(db.String(512), nullable=False)
    province = db.Column(db.String(512), nullable=False)
    pub_pri = db.Column(db.String(32), nullable=False)
    website = db.Column(db.String(512))
    govt = db.Column(db.String(512), nullable=False)
    campuses = db.Column(db.Integer)
    posts = db.relationship('Posts', backref='college', lazy='dynamic')

    # def __init__(self, username, email):
    #     self.username = username
    #     self.email = email

    def __repr__(self):
        return self.college_name


class Programs(db.Model):
    __tablename__ = 'programs'
    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.Text())
    uni_id = db.Column(db.Integer, db.ForeignKey('universities.id'))
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
    posts = db.relationship('Posts', backref='program', lazy='dynamic')

    # def __init__(self, username, email):
    #     self.username = username
    #     self.email = email

    def __repr__(self):
        return self.title


class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    post_type = db.Column(db.String(512), nullable=False)
    post_date = db.Column(db.DateTime, nullable=True)
    title = db.Column(db.String(512), nullable=False)
    meta_title = db.Column(db.String(512))
    meta_description = db.Column(db.String(512))
    content = db.Column(db.Text())
    uni_id = db.Column(db.Integer, db.ForeignKey('universities.id'))
    college_id = db.Column(db.Integer, db.ForeignKey('colleges.id'))
    program_id = db.Column(db.Integer, db.ForeignKey('programs.id'))


    def __init__(self, post):
        for k, v in post.items():
            setattr(self, k, v)