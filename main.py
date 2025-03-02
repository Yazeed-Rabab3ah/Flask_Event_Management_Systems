
from datetime import datetime


from flask import Flask, render_template, request
from flask import url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import EventForm
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkeyyazeed123!'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(120))
    date_posted = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f"Event ( {self.title}, {self.date_posted} )"
    
@app.route('/')
@app.route('/home')
def home():
    events = Event.query.all()
    return render_template('index.html', events=events)

@app.route('/event/<int:event_id>')
def event_details(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template('event-details.html', event=event)

@app.route('/about')
def about():
    return render_template('about-us.html')
    
@app.route('/create', methods=['GET', 'POST'])
def create_events():
    form = EventForm()
    if form.validate_on_submit():  
        event = Event()
        event.title = form.title.data
        event.description = form.description.data
        event.location = form.location.data

        db.session.add(event)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('create.html', form=form)

@app.route('/update/<int:event_id>', methods=['GET', 'POST'])
def update_event(event_id):
    event = Event.query.get_or_404(event_id)  
    form = EventForm(obj=event)

    if form.validate_on_submit():  
        event = Event.query.get_or_404(event_id)
        event.title = form.title.data
        event.description = form.description.data
        event.location = form.location.data

        db.session.commit()
        return redirect(url_for('event_details', event_id=event_id))
    return render_template('update.html', form=form)

@app.route('/delete/<int:event_id>', methods=['GET','POST'])
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    #with app.app_context():
        #db.create_all()
    app.run(debug=True) #enables debug mode which restart the server automaticlly when the code changes