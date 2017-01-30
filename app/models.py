from app import db
from flask_login import UserMixin
from werkzeug import generate_password_hash, check_password_hash

relationship_table=db.Table('relationship_table',                            
                             db.Column('post_id', db.Integer,db.ForeignKey('posts.id'), nullable=True),
                             db.Column('widget_id',db.Integer,db.ForeignKey('widgets.id'),nullable=True),
                             db.PrimaryKeyConstraint('post_id', 'widget_id') )

relationship_table2=db.Table('relationship_table2',                            
                             db.Column('university_id', db.Integer,db.ForeignKey('universities.id'), nullable=True),
                             db.Column('widget_id',db.Integer,db.ForeignKey('widgets.id'),nullable=True),
                             db.PrimaryKeyConstraint('university_id', 'widget_id') )

relationship_table3=db.Table('relationship_table3',                            
                             db.Column('program_id', db.Integer,db.ForeignKey('programs.id'), nullable=True),
                             db.Column('widget_id',db.Integer,db.ForeignKey('widgets.id'),nullable=True),
                             db.PrimaryKeyConstraint('program_id', 'widget_id') )

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, primary_key=True)
    password = db.Column(db.String(264))
    role = db.Column(db.String(264))

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
    __searchable__ = ['programs', 'uni_name']
    id = db.Column(db.Integer, primary_key=True)
    programs = db.relationship('Programs', backref='university', lazy='joined')
    colleges = db.relationship('Colleges', backref='university', lazy='joined')
    posts    = db.relationship('Posts', backref='university', lazy='joined')
    widgets    = db.relationship('Widgets', secondary=relationship_table2, backref='university', lazy='joined')
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

    # def __init__(self, username, email):
    #     self.username = username
    #     self.email = email

    def __repr__(self):
        return self.college_name


class Programs(db.Model):
    __tablename__ = 'programs'
    id = db.Column(db.Integer, primary_key=True)
    uni_id = db.Column(db.Integer, db.ForeignKey('universities.id'))
    degree = db.Column(db.Text())
    # posts = db.relationship('Posts', backref='program', lazy='dynamic')
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
    posts    = db.relationship('Posts', backref='program', lazy='joined')
    widgets    = db.relationship('Widgets', secondary=relationship_table3, backref='program', lazy='joined')
    

    # def __init__(self, username, email):
    #     self.username = username
    #     self.email = email

    def __repr__(self):
        return self.title + " - " + str(self.university)


class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    post_type = db.Column(db.String(512), nullable=False)
    post_date = db.Column(db.DateTime, nullable=True)
    title = db.Column(db.String(512), nullable=False)
    university_id = db.Column(db.Integer, db.ForeignKey('universities.id'))
    program_id = db.Column(db.Integer, db.ForeignKey('programs.id'))
    subject = db.Column(db.String(512))
    meta_title = db.Column(db.String(512))
    meta_description = db.Column(db.String(512))
    featured_image = db.Column(db.Unicode(218), nullable=False)
    content = db.Column(db.Text())
    widgets    = db.relationship('Widgets', secondary=relationship_table, backref='posts', lazy='joined')
    

    def __init__(self, **kwargs):
        super(Posts, self).__init__(**kwargs)
        # if not post_date:
        #     self.post_date = datetime.datetime.now()

    def __repr__(self):
        return self.title

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    path = db.Column(db.Unicode(128))
    img = db.Column(db.Unicode(128))

    def __repr__(self):
        return self.name


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(64))
    embed_code = db.Column(db.Unicode(1528))
    img = db.Column(db.Unicode(128))

    def __repr__(self):
        return self.title

class Widgets(db.Model):
    __tablename__ = 'widgets'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(64))
    content = db.Column(db.Text())
    homepage = db.Column(db.Unicode(64))
    allpages = db.Column(db.Unicode(64))
    categories = db.Column(db.Unicode(64))

    def __repr__(self):
        return self.title
