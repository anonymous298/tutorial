from flask import Flask, render_template, request, session, redirect, url_for, flash

# from flask_sqlalchemy import SQLAlchemyk
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'mysecretkey'
app.permanent_session_lifetime = timedelta(minutes=5)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# class users(db.Model):  # Renamed class to User for convention
#     id = db.Column(db.Integer, primary_key=True)  # Changed _id to id for convention
#     name = db.Column(db.String(100))
#     email = db.Column(db.String(100))
#     login_password = db.Column(db.String(100))
# 
    # def __init__(self, name, email, login_password):
    #     self.name = name
    #     self.email = email
    #     self.login_password = login_password

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        name = request.form['name']
        session['username'] = name

        return redirect(url_for('user'))
    else:
        return render_template('index.html')
    
@app.route('/user')
def user():
    if 'username' in session:
        username = session['username']
        return f'<h1>{username}</h1>'
    else:
        if 'username' in session:
            return redirect(url_for('user'))
        
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():    
    if 'username' in session:
        user = session['username']
        flash(f'You have been logged out {user}', 'info')

    session.pop('username', None)
    return redirect(url_for('login'))

# @app.route('/view')
# def view():
#     return render_template('view.html', values=users.query.all())

if __name__ == '__main__':
    # with app.app_context():  # Ensure app context is available
    #     db.create_all()  # Create database tables
    app.run(debug=True, host='0.0.0.0')
