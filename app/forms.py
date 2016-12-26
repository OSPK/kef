from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, DateTimeField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea
from .models import User
from flask_login import login_user, logout_user,\
                        current_user, login_required
import datetime

class LoginForm(Form):
    username = StringField("Username", validators=[DataRequired("Please enter your username."), Length(min=3, max=14)])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, max=14, message="Password must be at least 6 characters")])
    submit = SubmitField("Sign In")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(username=self.username.data.lower()).first()
        if user and user.check_password(self.password.data):
            login_user(user, True)
            return True
        else:
            self.username.errors.append("Invalid username or password")
            return False


class PostForm(Form):
    post_date = DateTimeField('Published Date', default=datetime.date.today())
    title = StringField("Title", validators=[DataRequired("Please enter title.")])
    post_type = StringField("Title", validators=[DataRequired("Please enter post type.")])
    content = StringField("Title", validators=[DataRequired("Please enter content.")])
    university_id = StringField("University ID")
    college_id = StringField("College ID")
    program_id = StringField("Program ID")

    submit = SubmitField("Submit")