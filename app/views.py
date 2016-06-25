from flask import request, render_template
from .models import Universities, Colleges, Programs
from app import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


class MyModelView(ModelView):
    def __init__(self, model, session, name=None, category=None, endpoint=None, url=None, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        super(MyModelView, self).__init__(model, session, name=name, category=category, endpoint=endpoint, url=url)

    def is_accessible(self):
        # Logic
        return True


admin = Admin(app, template_mode='bootstrap3')
admin.add_view(MyModelView(Universities, db.session, list_columns=['id', 'uni_name', 'city', 'province']))
admin.add_view(MyModelView(Colleges, db.session, list_columns=['id', 'uni_name', 'city', 'province']))
admin.add_view(ModelView(Programs, db.session))


@app.route('/')
def index():
    cities = ['Abbottabad', 'Bagh', 'Bahawalpur', 'Bannu', 'Bhimber', 'Charsadda', 'D.I.Khan', 'Dera Ghazi Khan', 'Dir', 'Faisalabad', 'Gilgit', 'Gujranwala', 'Gujrat', 'Haripur', 'Hyderabad', 'Islamabad', 'Jamshoro', 'Karachi', 'Karak', 'Khairpur', 'Khuzdar', 'Kohat', 'Kotli', 'Lahore', 'Larkana', 'Lasbela', 'Loralai', 'Malakand', 'Manshera', 'Mardan', 'Mirpur', 'Multan', 'Muzaffarabad', 'Nawabshah', 'Nerain Sharif', 'Nowshera', 'Peshawar', 'Quetta', 'Rahim Yar Khan', 'Rawalakot', 'Rawalpindi', 'Sakrand', 'Sargodha', 'Sialkot', 'Sukkur', 'Swabi', 'Swat', 'Tandojam', 'Taxila', 'Topi', 'Turbat', 'Wah']
    provinces = ["Islamabad", "Khyber Pakhtunkhwa", "Punjab", "Sindh", "Balochistan", "Azad Jammu and Kashmir", "Gilgit-Baltistan"]
    return render_template('index.html', cities=cities, provinces=provinces)


@app.route('/universities')
def universities():
    universities = Universities.query.all()
    cities = ['Abbottabad', 'Bagh', 'Bahawalpur', 'Bannu', 'Bhimber', 'Charsadda', 'D.I.Khan', 'Dera Ghazi Khan', 'Dir', 'Faisalabad', 'Gilgit', 'Gujranwala', 'Gujrat', 'Haripur', 'Hyderabad', 'Islamabad', 'Jamshoro', 'Karachi', 'Karak', 'Khairpur', 'Khuzdar', 'Kohat', 'Kotli', 'Lahore', 'Larkana', 'Lasbela', 'Loralai', 'Malakand', 'Manshera', 'Mardan', 'Mirpur', 'Multan', 'Muzaffarabad', 'Nawabshah', 'Nerain Sharif', 'Nowshera', 'Peshawar', 'Quetta', 'Rahim Yar Khan', 'Rawalakot', 'Rawalpindi', 'Sakrand', 'Sargodha', 'Sialkot', 'Sukkur', 'Swabi', 'Swat', 'Tandojam', 'Taxila', 'Topi', 'Turbat', 'Wah']
    provinces = ["Islamabad", "Khyber Pakhtunkhwa", "Punjab", "Sindh", "Balochistan", "Azad Jammu and Kashmir", "Gilgit-Baltistan"]
    if request.args.get('city') is not None:
        universities = Universities.query.filter_by(city=request.args.get('city')).all()
    if request.args.get('province') is not None:
        universities = Universities.query.filter_by(province=request.args.get('province')).all()
    if request.args.get('pub_pri') is not None:
        universities = Universities.query.filter_by(pub_pri=request.args.get('pub_pri')).all()
    return render_template('universities.html', cities=cities, provinces=provinces, universities=universities)


@app.route('/programs/<int:uni_id>')
def programs(uni_id):
    university = Universities.query.get(uni_id)
    programs = Programs.query.filter_by(uni_id=uni_id).all()
    return render_template('programs.html', university=university, programs=programs)


@app.route('/program/<int:id>')
def program(id):
    program = Programs.query.filter_by(id=id).first()
    university = Universities.query.get(program.uni_id)
    return render_template('program.html', university=university, program=program)


@app.route('/programs/scholarships')
def scholarship():
    programs = Programs.query.filter(Programs.scholarship is not False).all()
    return render_template('scholarships.html', programs=programs, university=None)


@app.route('/programs/')
def all_programs():
    programs = Programs.query.filter(Programs.degree is not False, Programs.title is not False).all()
    return render_template('all_programs.html', programs=programs)
