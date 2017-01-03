import os
import os.path as op
from flask import request, render_template, redirect, url_for, flash
from .models import Universities, Colleges, Programs, User, Posts, Image
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
from sqlalchemy import or_,  and_

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

    column_list=['id', 'title', 'post_date']

    form_overrides = dict(text=CKTextAreaField)

    create_template = 'edit.html'
    edit_template = 'edit.html'

    form_choices = {'post_type': [ ('articles', 'Article'),
                                ('past-papers', 'Past Paper'),
                                ('date-sheets', 'Date Sheet'),
                                ('syllabus', 'Syllabus'),
                                ('news', 'News'),
                                ('notes', 'Notes')]
                    }
    form_extra_fields = {
        'featured_image': form.ImageUploadField('Featured Image',
                                      base_path=file_path)
    }


class ImageView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''
        imgpath = url_for('static', filename=form.thumbgen_filename(model.path))
        return Markup('<img src="%s">' % imgpath)
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

admin = Admin(app, template_mode='bootstrap3')
admin.add_view(UniModelView(Universities, db.session))
admin.add_view(MyModelView(Colleges, db.session))
admin.add_view(ProgAdmin(Programs, db.session))
admin.add_view(PostsView(Posts, db.session))
admin.add_view(ImageView(Image, db.session))
admin.add_view(MyFileAdmin(file_path, '/static/', name='Static Files'))

CITIES = ['Abbottabad', 'Bagh', 'Bahawalpur', 'Bannu', 'Bhimber', 'Charsadda', 'D.I.Khan', 'Dera Ghazi Khan', 'Dir', 'Faisalabad', 'Gilgit', 'Gujranwala', 'Gujrat', 'Haripur', 'Hyderabad', 'Islamabad', 'Jamshoro', 'Karachi', 'Karak', 'Khairpur', 'Khuzdar', 'Kohat', 'Kotli', 'Lahore', 'Larkana', 'Lasbela', 'Loralai', 'Malakand', 'Manshera', 'Mardan', 'Mirpur', 'Multan', 'Muzaffarabad', 'Nawabshah', 'Nerain Sharif', 'Nowshera', 'Peshawar', 'Quetta', 'Rahim Yar Khan', 'Rawalakot', 'Rawalpindi', 'Sakrand', 'Sargodha', 'Sialkot', 'Sukkur', 'Swabi', 'Swat', 'Tandojam', 'Taxila', 'Topi', 'Turbat', 'Wah']
PROVINCES = ["Islamabad", "Khyber Pakhtunkhwa", "Punjab", "Sindh", "Balochistan", "Azad Jammu and Kashmir", "Gilgit-Baltistan"]

@app.context_processor
def ctites_provinces():
    return {'cities': CITIES, 'provinces': PROVINCES}

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
    posts = Posts.query.all()
    return render_template('index2.html', posts=posts)


@app.route('/<type>')
def posts(type):
    posts = Posts.query.filter_by(post_type=type).all()
    return render_template('posts2.html', posts=posts)

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

    return render_template('universities2.html', universities=universities)


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


@app.route('/article/<slug>')
def article(slug):
    content = {}
    heading = {}
    image = {}
    content[1] = """
    Source:  APP Published in Education on Friday, March 18, 2016

    LAHORE - Punjab Chief Minister Shehbaz Sharif has said that enrolment target of every child of the province will be achieved till 2018 through hard work and commitment.


    While presiding a meeting, which reviewed the progress on educational reforms programme under Punjab Schools Reforms Roadmap, he said that achievement of the targets fixed for promotion of education was the collective responsibility and effective measures would have to be taken in this regard. The chief minister said that it was national responsibility to achieve targets of “Parho Punjab Barho Punjab Programme.”

    CM Shehbaz said that a comprehensive programme should be evolved for the training of teachers and steps should be taken for its immediate implementation. He said that provision of resources for the promotion of education was a useful investment and access to quality education was the right of every child.

    He said that funds worth of billions rupees had been given for repair and construction of the dilapidated buildings of schools and completion of this work within stipulated period would be ensured. He said that the officers failing in achieving the educational targets had no right to stay on their posts.

    He expressed indignation over not taking timely measures for the teachers’ training, adding that teachers the programme was an important element of educational reforms roadmap.

    While speaking on the occasion, Sir Michael Barber appreciated the efforts of the chief minister and his team for the development of education sector. The Department for International Development’s (DFID) head Joanna Reid said on the occasion that time given by the chief minister for the uplift of education sector was a proof of his commitment.
    """
    heading[1] = "CM reviews progress on educational reforms programme"
    image[1] = "/static/images/shahbaz-sharif.jpg"

    heading[2] = "Govt asked to remove controversial lesson from course book"
    image[2] = "/static/images/girls.gif"
    content[2] = """
    SWABI: Political and civil society activists have threatened that if the Khyber Pakhtunkhwa Textbook Board doesn’t remove a controversial lesson about Pakhtun hero Malik Kalu Khan from the ninth grade English book, then they would take the case to court.

    Addressing a convention on ‘Kalu Khan, a hero of Pakhtuns’, at Haqqani Library Hall here on Sunday, they maintained that Yousafzai Action Committee (YAC), formed for this purpose by political parties, would move court against the textbook board officials and the book’s writer if the ‘insulting’ lesson was not removed.

    It was decided that members of the action committee would meet KP Assembly Speaker Asad Qaisar, officials of the textbook board and provincial education minister soon in Peshawar to discuss the matter.

    The action committee has a member from each political party and literary organisation.

    On the occasion, Mohammad Jamil Advocate, a columnist and founder of the drive to get the lesson removed from the book, said Kalu Khan fought against Mughal Emperor Akbar so bravely that the latter was forced to build the Attock Fort at the edge of the Indus for his defence.

    Leaders at Swabi convention threaten to move court

    “Though the Mughals were looters the Pakhtuns were portrayed as looters in the said lesson titled ‘Snare’,” he pointed out.

    Awwal Sher Khan, former forest minister, said the lesson was written and included in the book under a well-thought out conspiracy to distort the character of Kalu Khan and twist the facts about Pakhtun leaders. Ghafoor Khan Jadoon, former provincial food minister, said YAC members should meet the lawmakers and appraised them about the facts. “A resolution for removal of the lesson should be moved by them in the provincial assembly,” he demanded.

    Saleem Khan Advocate of QWP said Pakhtun terrains were called by British and other invaders as ‘diamond necklace’ because these were full of natural resources. Due to economic reasons various invaders invaded the region but Pakhtun supermen like Malik Kalu Khan, Malik Gaju Khan and Malik Ahmad fought and pushed them back bravely.

    Najeem Khan of JUI-Nazriati said it was high time for Pakhtuns to unite against all those who were bent upon defaming them and their heroes.

    District nazim Aamir Rehman said they rejected the book which presented Kalu Khan as a looter. He said the district government would help the YAC in achieving its objective.

    Tehsil Razaar Nasim Ghulam Haqqani announced that his government would build mausoleum of Kalu Khan.

    Tehsil Swabi Nazim Wahid Shah said the writer was enemy of the entire Pakhtun nation.

    Iftikhar Ahmad Khan of PML-N, Mehmoodul Hassan of JI, Rangaiz of PTI, Javid Inqilabi of PPP, Mohammad Ali Dagaiwal of Pakhtunkhwa Ulasi Tehreek, Mohammad Jalil of Abaseen Union of Journalists, Mohammad Sagheer of Swabi bar, Aziz Minerwal of Qam Qalam, and others also spoke on the occasion.

    Through three resolutions, the participants of the convention demanded to replace on the lesson with tales of Pakhtun heroes, action against the writer and introduction of Pashto as compulsory subject in schools.
    """

    heading[3] = "81pc of all schools in Pakistan are primary"
    image[3] = "/static/images/data.gif"
    content[3] = """
    ISLAMABAD: A staggering 81pc of all government schools in Pakistan are primary schools, which implies that after the primary level, most children have limited opportunities to continue their studies.

    This statistic was revealed in the District Education Rankings 2016, jointly launched by education campaigners Alif Ailaan and the Sustainable Development Policy Institute (SDPI) on Tuesday.

    This is a worrying statistic, and according to researchers who worked on the report, one that has been historically observed. Observers say that, as with most other problems in the country, political interests seem to be root cause of this issue as well.

    “Politicians have stacked the public sector with low quality primary school teachers for decades - once hired, these primary school teachers needed schools. It is much harder to find and employ higher skill set teachers for middle and high schools,” said Mosharraf Zaidi, who heads the Alif Ailaan campaign.

    In the past, MNAs and MPAs have an easier time getting approval for primary schools than secondary or higher schools. “All you need is a two-room building, a teacher who doubles as the headmaster and a peon or two and you’re set,” a district education official told Dawn.

    Experts say schoolchildren have nowhere to go after grade 5; Islamabad tops district education rankings, Lahore and Rawalpindi’s scores decline

    This effectively means that there are not enough secondary schools to cater to the large number of students who complete their primary education, leading to dropouts.

    A.H. Nayyer, a leading educationist, puts the onus for ensuring student retention squarely on the state’s shoulders.

    “According to Article 25A of the Constitution (which deals with the right to education), the state is bound to provide education to all children aged between five and 16. A child who completes primary education is much younger than 16, so the state’s responsibility does not end at the primary level.”

    If these statistics are true, Mr Nayyer told Dawn, the state would have to build more secondary and middle schools to accommodate those children. “The state will have to fulfill this responsibility,” he concluded.

    Speaking at the report’s launch, PTI MNA Arif Alvi said that it was absolutely necessary for politicians to take ownership of schools and children in their respective constituencies at an individual level.

    ANP leader Mian Ifttikhar Hussain called for a population census, which was key to getting a reliable baseline for ranking districts and tracking the Sustainable Development Goal-targets.

    UNDP Country Director Marc-Andre Franche said: “The rankings highlight the systematic inequalities among the districts and the regions in Pakistan. The state of education in the districts of South Punjab, Balochistan and Fata is worse than some of the sub-Saharan African countries, while the districts of North Punjab emulate developed countries like Canada”.
    """

    heading[4] = "NUST stands among world’s top 150 young universities"
    image[4] = "/static/images/nust.gif"
    content[4] = """
    LAHORE – The National University of Science and Technology (NUST) stands among the top world 150 young universities in a ranking unveiled by The Times Higher Education (THE).

    The ranking of the world’s top universities, under 50 years of age has École Polytechnique Fédérale de Lausanne, founded in 1969 in Switzerland, at the top spot, reflecting a European dominance of this forward-looking ranking of young universities.

    NUST, founded in 1991, has 9,808 students with a 7.8 student-staff ratio. Of its total enrollment, three percent of the students are international whereas female-male ratio is 27:73.

    “The 150 Under 50 ranking is led by young, exciting and dynamic institutions – half of the universities in the top 10 are 30 years or under - from nations investing heavily in creating world-class institutions, for example, Hong Kong, South Korea and Singapore,” said Phil Bety, editor at the The Times Higher Education.

    “As the pendulum swings, the traditionally dominant US and UK will have to raise their games to continue to compete in future years.” NUST earned the place because of its outstanding faculty, international outlook, industry income, research and citations.

    East Asian institutions take four of the next five places. These include Nanyang Technological University, Singapore (2nd), Hong Kong University of Science and Technology (3rd), Pohang University of Science and Technology, South Korea (5th) and Korea Advanced Institute of Science and Technology (KAIST), South Korea (6th).

    THE 150 Under 50 reveals those nations and regions challenging the traditional dominance of universities located in the US and UK, whose institutions occupy 30 places in the overall ranking. By contrast, Continental European and Asian institutions account for 95 of those placed in THE 150 Under 50, with a further 20 located in Australia or New Zealand, four in Canada and one in Brazil.
    """

    heading[5] = "Govt to distribute tabs among students of class 5, 8"
    image[5] = "/static/images/tablet.gif"
    content[5] = """
    LAHORE- Punjab Schools Education Department (SED) will award tabs (tablets) to students of class 5 and class 8 over performance in their annual examination.

    SED has prepared a list of 54,000 students and 2,400 teachers, who are teaching science subjects to class 5 and class 8. However teachers of others subjects are likely to be ignored in the distribution of tabs.

    According to sources, students who will get good grades in the ongoing Punjab Examination Commission (PEC) exams of class 5 and 8 will be awarded with tabs featuring latest specifications.

    Sources further told that the teachers possess better students pass ratio will be only eligible for getting these tabs. 
    """

    heading[6] = "Nigerian academicians visits Open University, sign MoU for partnership"
    image[6] = "/static/images/aiou.gif"
    content[6] = """
    ISLAMABAD – About 11-member delegation from Nigeria’s Sokoto State University on Monday visited AllamaI qbal Open University (AIOU) and signed a memorandum of understanding for developing cooperative partnership in the field of research and professional development.

    The MoU was signed by Sokoto University Vice Chancellor Professor Nuhu O Yaqub and AIOU Vice Chancellor Professor Dr Shahid Siddiqui at a ceremony that was also attended by the academicians from both the sides. The Nigerian delegation comprising senior professors appreciated the AIOU’s efforts of providing affordable quality education to country’s big population (1.3 million) through distance learning system. The Nigerian side accepted DrSiddiqui’s offer of jointly organising a international conference on social sciences next year.

    The two Universities, under the MoU, will develop a framework of collaboration in the area of science, technology, humanity and capacity development. They will exchange variety of educational programs to promote knowledge and technical know-how for the benefit of their students.

    It was decided that they will specially focus on conducting research-based study in the areas of common interest. The MoU also covered a mechanism for exchange of visits by students and faculty members to each other universities.

    The delegation that included Deputy VC Prof Malami Buba and Registrar Amina G Yusuf visited various departments of the university including Institute of Educational Technology and Print and Production Unit. They evinced keen interest in the Accessibility Centre set up at Central Library for visually impaired students.

    On arrival, Dr Shahid Siddiqui briefed the delegation on University’s academic activities and the initiatives taken recently for its professional development. In-charge International collaboration department Zahid Majeed gave a presentation on the university’s overall working. Registrar Dr Muhammad Naeem Qureshi was also present on the occasion.
    """

    return render_template('article.html', slug=slug, content=content, image=image, heading=heading)