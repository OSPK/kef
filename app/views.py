import os
import os.path as op
import datetime
from flask import request, render_template, redirect, url_for, flash
from .models import Universities, Colleges, Programs, User, Posts, Image, Video, Widgets
from app import app, db, login_manager
from flask_admin import Admin, form
from flask_admin.contrib.sqla import ModelView
from flask_login import login_user, logout_user,\
                        current_user, login_required
import re
from .forms import LoginForm, CKTextAreaField
from jinja2 import evalcontextfilter, Markup, escape
from sqlalchemy.event import listens_for
from flask_admin.contrib.fileadmin import FileAdmin
from flask.ext.admin.menu import MenuLink
from sqlalchemy import or_,  and_, desc

_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')

@login_manager.user_loader
def user_loader(user_id):
    return User.query.filter_by(username=user_id).first()


@app.template_filter()
@evalcontextfilter
def nl2br(eval_ctx, value):
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br>\n') \
        for p in _paragraph_re.split(escape(value)))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result


POSTS_PER_PAGE = 20


# Create directory for file fields to use
file_path = op.join(op.dirname(__file__), 'static')
try:
    os.mkdir(file_path)
except OSError:
    pass

class MyModelView(ModelView):
    def __init__(self, model, session, name=None, category=None, endpoint=None, url=None, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        super(MyModelView, self).__init__(model, session, name=name, category=category, endpoint=endpoint, url=url)

    def is_accessible(self):
        return current_user.is_authenticated

    column_list=['id', 'uni_name', 'city', 'province']

class UniModelView(MyModelView):
    column_searchable_list = ['uni_name']

class ProgAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    column_display_pk = True
    column_hide_backrefs = False
    column_list=['id', 'title', 'university.uni_name', 'degree']
    column_sortable_list=['id', 'title', 'university.uni_name', 'degree']
    column_searchable_list = ['title', 'university.uni_name']
    form_columns=['university','degree','title','city','district','province','institute_type','eligibility','complation_requirement','scope','fees','scholarship','duration','credit_hours','teaching_system','seats','shift','session','regular_private','department','faculty','course_outline','campus','hec_ranking','hostel_facility','contact','location','affiliation','lectures_notes','reference_sites','web','alumni']
    form_choices = {'degree': [ ('Bachelor', 'Bachelor'),
                                ('Master', 'Master'),
                                ('MS', 'MS'),
                                ('M.Phil', 'M.Phil'),
                                ('MS/M.Phil', 'MS/M.Phil'),
                                ('Phd', 'Phd'),
                                ('Diploma', 'Diploma')],
                    'scholarship':[('Available','Available'),('Not available','Not available')],
                    'teaching_system':[('Semester System', 'Semester System'),
                                        ('Annual system', 'Annual system'),
                                        ('Distance education system', 'Distance education system')],
                    'shift':[('morning','morning'),('evening','evening'),('afternoon','afternoon')],
                    'institute_type':[('university','university'),('college','college')]
                    }

    
class PostsView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    column_list=['id', 'title', 'post_date', 'post_type']
    column_filters = ['id', 'title', 'post_date', 'post_type']
    column_default_sort=('post_date', True)
    column_searchable_list = ['title', 'post_type', 'program.title' ,'university.uni_name']
    form_overrides = dict(text=CKTextAreaField)
    form_args = dict(
                post_date=dict(default=datetime.datetime.now())
            )
    create_template = 'edit.html'
    edit_template = 'edit.html'

    form_choices = {'post_type': [ ('articles', 'Article'),
                                ('past-papers', 'Past Paper'),
                                ('date-sheets', 'Date Sheet'),
                                ('syllabus', 'Syllabus'),
                                ('news', 'News'),
                                ('notes', 'Notes'),
                                ('results', 'Results'),
                                ('scholarships', 'Scholarships'),
                                ('career-counselling', 'Career Counselling'),
                                ('success-stories', 'Success Stories'),
                                ('my-teachers', 'My Teachers')
                                ]
                    }
    form_extra_fields = {
        'featured_image': form.ImageUploadField('Featured Image',
                                      base_path=file_path),
        'pdf_attachment': form.FileUploadField('PDF Attachment',
                                      base_path=file_path,
                                      allowed_extensions=["pdf"]),
    }


class ImageView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''
        img_thumb = form.thumbgen_filename(model.path).replace('_thumb', '')
        imgpath = url_for('static', filename=img_thumb)
        return Markup('<img width="100" height="100" src="%s">' % imgpath)
    def _list_path(view, context, model, name):
        if not model.path:
            return ''
        imgpath = url_for('static', filename=model.path)
        return Markup('<a href="{0}">{0}'.format(imgpath, imgpath))
    column_formatters = {
        'img': _list_thumbnail,
        'path': _list_path
    }
    column_list=['name', 'path', 'img']
    form_columns=['name', 'path']
    # Alternative way to contribute field is to override it completely.
    # In this case, Flask-Admin won't attempt to merge various parameters for the field.
    form_extra_fields = {
        'path': form.ImageUploadField('Image',
                                      base_path=file_path)
    }
@listens_for(Image, 'after_delete')
def del_image(mapper, connection, target):
    if target.path:
        # Delete image
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass

        # Delete thumbnail
        try:
            os.remove(op.join(file_path,
                              form.thumbgen_filename(target.path)))
        except OSError:
            pass

class MyFileAdmin(FileAdmin):
    def is_accessible(self):
        return current_user.is_authenticated

class UserModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    column_list=['id', 'username', 'role']
    form_columns=['username', 'password', 'role']

    def after_model_change(self, form, model, is_created):
         password = form.password.data
         print(password)
         model.set_password(password)
         db.session.commit()
         # if is_created: # create the table just once
         #     model.set_password(password)
         #     db.session.commit()
         #     #

class WidgetsView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    form_choices = {'homepage': [('yes', 'Yes - Show on Home Page'),
                                ('no', 'No - Dont show on homepage') ],
                    'allpages': [('yes', 'Yes - Show on All Page'),
                                ('no', 'No - Show only on specified pages') ],
                    'categories': [ ('all', 'All Categories'),
                                ('articles', 'Article'),
                                ('past-papers', 'Past Paper'),
                                ('date-sheets', 'Date Sheet'),
                                ('syllabus', 'Syllabus'),
                                ('news', 'News'),
                                ('notes', 'Notes'),
                                ('results', 'Results'),
                                ('scholarships', 'Scholarships'),
                                ('career-counselling', 'Career Counselling'),
                                ('success-stories', 'Success Stories'),
                                ('my-teachers', 'My Teachers'),
                                ('videos', 'Videos')
                                ]
                    }

    create_template = 'edit.html'
    edit_template = 'edit.html'

class VideosView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    form_extra_fields = {
        'img': form.ImageUploadField('Featured Image',
                                      base_path=file_path)
    }


admin = Admin(app, template_mode='bootstrap3')
admin.add_view(UserModelView(User, db.session))
admin.add_view(UniModelView(Universities, db.session))
admin.add_view(MyModelView(Colleges, db.session))
admin.add_view(ProgAdmin(Programs, db.session))
admin.add_view(PostsView(Posts, db.session))
admin.add_view(ImageView(Image, db.session))
admin.add_view(VideosView(Video, db.session))
admin.add_view(WidgetsView(Widgets, db.session))
admin.add_link(MenuLink(name='Site', category='', url="/"))
admin.add_link(MenuLink(name='Logout', category='', url="/logout"))
# admin.add_view(MyFileAdmin(file_path, '/static/', name='Static Files'))

CITIES = ['Abbottabad', 'Bagh', 'Bahawalpur', 'Bannu', 'Bhimber', 'Charsadda', 'D.I.Khan', 'Dera Ghazi Khan', 'Dir', 'Faisalabad', 'Gilgit', 'Gujranwala', 'Gujrat', 'Haripur', 'Hyderabad', 'Islamabad', 'Jamshoro', 'Karachi', 'Karak', 'Khairpur', 'Khuzdar', 'Kohat', 'Kotli', 'Lahore', 'Larkana', 'Lasbela', 'Loralai', 'Malakand', 'Manshera', 'Mardan', 'Mirpur', 'Multan', 'Muzaffarabad', 'Nawabshah', 'Nerain Sharif', 'Nowshera', 'Peshawar', 'Quetta', 'Rahim Yar Khan', 'Rawalakot', 'Rawalpindi', 'Sakrand', 'Sargodha', 'Sialkot', 'Sukkur', 'Swabi', 'Swat', 'Tandojam', 'Taxila', 'Topi', 'Turbat', 'Wah']
PROVINCES = ["Islamabad", "Khyber Pakhtunkhwa", "Punjab", "Sindh", "Balochistan", "Azad Jammu and Kashmir", "Gilgit-Baltistan"]

@app.context_processor
def ctites_provinces():
    return {'cities': CITIES, 'provinces': PROVINCES}


def widget_maker(placement, **kwargs):
    category = kwargs.get('category', '*')

    if placement=='homepage':
        widget = Widgets.query.filter(Widgets.homepage=='yes').all()

    if placement=='posts-list':
        widget = Widgets.query.filter((Widgets.allpages=='yes')\
                | (Widgets.categories==category)\
                | (Widgets.categories=='all')\
                ).all()

    return widget

app.jinja_env.globals.update(widget_maker=widget_maker)


#ROUTES

@app.route('/setup')
def setup():
    admin = User.query.filter_by(username="admin").first()
    if not admin:
        admin = User("admin", "123karwan")
        db.session.add(admin)
        db.session.commit()
        return "ready"
    else:
        return "already ready"

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash('Logged in successfully.')

            return redirect('/admin')
        else:
            flash('Unsuccessful.', 'warning')

    return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")


@app.route('/')
def index():
    types = {'news':'', 'articles':'', 'past-papers':'',
            'date-sheets':'', 'syllabus':'', 'notes':'',
            'results':'', 'scholarships':'', 'career-counselling':'',
            'success-stories':'', 'my-teachers':''
            }
    for type in types:
        types[type] = Posts.query.filter_by(post_type=type).order_by(desc(Posts.post_date)).limit(4).all()

    videos = Video.query.order_by(desc(Video.id)).limit(4).all()
    return render_template('index2.html', types=types, videos=videos)


@app.route('/<type>')
@app.route('/<type>/<int:page>')
def posts(type, page=1):
    posts = Posts.query.filter_by(post_type=type).order_by(desc(Posts.post_date)).paginate(page, POSTS_PER_PAGE, False)
    return render_template('posts.html', pcont=pcont, posts=posts.items, type=type)

@app.route('/videos')
def videos():
    videos = Video.query.order_by(desc(Video.id)).all()
    return render_template('videos.html', videos=videos)

@app.route('/search/')
def search():
    query = request.args.get('s')
    s = "%{0}%".format(query)
    province = request.args.get('province', '*')
    city = request.args.get('city')
    program = request.args.get('p')
    

    if program is not None:
        program = "%{0}%".format(program)
        programs = Programs.query.filter(Programs.title.ilike(program)).\
                   all()
        return render_template('programs-list.html', programs=programs)
    else:
        if city and province and query:
            universities = Universities.query.filter(and_(Universities.uni_name.ilike(s),\
                           Universities.city==city,\
                           Universities.province==province,\
                           )).all()
        elif city and query:
            universities = Universities.query.filter(and_(Universities.uni_name.ilike(s),\
                           Universities.city==city,\
                           )).all()
        elif province and query:
            universities = Universities.query.filter(and_(Universities.uni_name.ilike(s),\
                           Universities.province==province,\
                           )).all()
        elif city and province:
            universities = Universities.query.filter(Universities.province==province).filter(Universities.city==city).all()
        elif city:
            universities = Universities.query.filter(Universities.city==city).all()
        elif province:
            universities = Universities.query.filter(Universities.province==province).all()
        elif query:
            universities = Universities.query.filter(Universities.uni_name.ilike(s)).all()
        else:
            universities = Universities.query.all()

    return render_template('universities.html', universities=universities)


@app.route('/universities')
def universities():
    universities = Universities.query.all()

    if request.args.get('city') is not None:
        universities = Universities.query.filter_by(city=request.args.get('city')).all()
    if request.args.get('province') is not None:
        universities = Universities.query.filter_by(province=request.args.get('province')).all()
    if request.args.get('pub_pri') is not None:
        universities = Universities.query.filter_by(pub_pri=request.args.get('pub_pri')).all()
    return render_template('universities.html', universities=universities)


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

@app.route('/program/<int:id>/add', methods=['POST'])
@login_required
def program_add(id):
    program = Programs()
    program.uni_id = id
    program.title = "New Program"
    db.session.add(program)
    db.session.commit()
    return redirect(url_for('programs', uni_id=id))


@app.route('/program/<int:id>/delete', methods=['POST'])
@login_required
def program_delete(id):
    program = Programs.query.filter_by(id=id).first()
    uni = program.uni_id
    db.session.delete(program)
    db.session.commit()
    return redirect(url_for('programs', uni_id=uni))


@app.route('/programs/scholarships')
def scholarship():
    programs = Programs.query.filter(Programs.scholarship is not False).all()
    return render_template('scholarships.html', programs=programs, university=None)


@app.route('/programs/')
def all_programs():
    programs = Programs.query.filter(Programs.degree is not False, Programs.title is not False).all()
    return render_template('all_programs.html', programs=programs)


@app.route('/<type>/<int:id>/<slug>')
def article(id, slug, type):
    post = Posts.query.get(id)
    related = Posts.query.filter_by(post_type=type).order_by(desc(Posts.post_date)).limit(5).all()
    return render_template('article.html', post=post, related=related)