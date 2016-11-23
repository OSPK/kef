from flask import request, render_template, redirect, url_for
from .models import Universities, Colleges, Programs
from app import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import re
from jinja2 import evalcontextfilter, Markup, escape

_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')

@app.template_filter()
@evalcontextfilter
def nl2br(eval_ctx, value):
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br>\n') \
        for p in _paragraph_re.split(escape(value)))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result

class MyModelView(ModelView):
    def __init__(self, model, session, name=None, category=None, endpoint=None, url=None, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        super(MyModelView, self).__init__(model, session, name=name, category=category, endpoint=endpoint, url=url)

    def is_accessible(self):
        # Logic
        return True

class ProgAdmin(ModelView):
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


admin = Admin(app, template_mode='bootstrap3')
admin.add_view(MyModelView(Universities, db.session, list_columns=['id', 'uni_name', 'city', 'province']))
admin.add_view(MyModelView(Colleges, db.session, list_columns=['id', 'uni_name', 'city', 'province']))
admin.add_view(ProgAdmin(Programs, db.session))


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

@app.route('/program/<int:id>/add', methods=['POST'])
def program_add(id):
    program = Programs()
    program.uni_id = id
    program.title = "New Program"
    db.session.add(program)
    db.session.commit()
    return redirect(url_for('programs', uni_id=id))


@app.route('/program/<int:id>/delete', methods=['POST'])
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