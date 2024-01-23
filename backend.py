from flask import Flask, render_template, request, flash 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'dev'

db = SQLAlchemy()
db_name = 'database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

class Ticket(db.Model):
    __tablename__ = 'ticket'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    mail = db.Column(db.String) 
    message = db.Column(db.String)
    date = db.Column(db.String)

    def __init__(self, name, mail, message, date):
        self.name = name 
        self.mail = mail 
        self.message = message
        self.date = date 

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return new_ticket()
    return render_template('index.html')

def new_ticket():
    name =request.form['name']
    mail = request.form['mail']
    message = request.form['message']
    date = datetime.now()
    new_record = Ticket(
        name=name,
        mail=mail,
        message=message,
        date=date
    )
    db.session.add(new_record)
    db.session.commit()
    success = True
    return render_template('index.html', success=success, mail=mail)


@app.route('/g-g/page1')
def page1():
    title = 'Guidet gjennomgang'
    video = '/static/videos/Kom i gang med Microsoft Teams.mp4'
    next_page = 'page2'
    prev_page = 'page1'
    page_content = 'Introduksjon'

    return render_template('vid_page.html', 
                           title=title, 
                           video=video,
                           next_page=next_page,
                           page_content=page_content,
                           prev_page=prev_page,
                           )

@app.route('/g-g/page2')
def page2():
    title = 'Guidet gjennomgang'
    video = '/static/videos/Microsoft Teams - Chat in Teams Tips and Tricks.mp4'
    next_page = 'page3'
    prev_page = 'page1'
    page_content = 'Chat i Teams'

    return render_template('vid_page.html', 
                           title=title, 
                           video=video,
                           next_page=next_page,
                           page_content=page_content,
                           prev_page=prev_page,
                           )

@app.route('/g-g/page3')
def page3():
    title = 'Guidet gjennomgang'
    video = '/static/videos/🧙_♂️ Top 20 Microsoft Teams Meeting Tips & Tricks.mp4'
    next_page = 'page4'
    prev_page = 'page2'
    page_content = 'Sett opp og administrer møter'

    return render_template('vid_page.html', 
                           title=title, 
                           video=video,
                           next_page=next_page,
                           page_content=page_content,
                           prev_page=prev_page,
                           )

@app.route('/g-g/page4')
def page4():
    title = 'Guidet gjennomgang'
    video = '/static/videos/How to use Microsoft SharePoint.mp4'
    next_page = 'page5'
    prev_page = 'page3'
    page_content = 'Microsoft sharepoint'

    return render_template('vid_page.html', 
                           title=title, 
                           video=video,
                           next_page=next_page,
                           page_content=page_content,
                           prev_page=prev_page,
                           )

@app.route('/g-g/page5')
def page5():
    title = 'Guidet gjennomgang'
    video = '/static/videos/Easy Guide to Collaboration in Microsoft 365.mp4'
    next_page = 'page6'
    prev_page = 'page4'
    page_content = 'Samarbeid i Office 365'

    return render_template('vid_page.html', 
                           title=title, 
                           video=video,
                           next_page=next_page,
                           page_content=page_content,
                           prev_page=prev_page,
                           )

@app.route('/g-g/page6')
def page6():
    title = 'Guidet gjennomgang'
    video = '/static/videos/Microsoft OneDrive Tutorial All You Need to Know.mp4'
    next_page = 'test'
    prev_page = 'page5'
    page_content = 'Onedrive'

    return render_template('vid_page.html', 
                           title=title, 
                           video=video,
                           next_page=next_page,
                           page_content=page_content,
                           prev_page=prev_page,
                           )

@app.route('/g-g/test', methods=['POST', 'GET'])
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)