from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.urls import url_parse

from .forms import LoginForm, RegisterForm
#from . import db
from flask import current_app as app
#from .models import User


#this is the routing to the main home page
#when the app is launched in the local host, with out a routing, they are directed to home.html
#when app launched with /home, user is directed to home.html
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():

    name = 'hewan'
    title = 'Home'
    form = LoginForm()

    return render_template('home.html', title=title, name=name, form=form)


#the routing when user presses logout
#directly headed to the home page
#the home page is shown by being directed to home.html
@app.route('/logout')
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('home'))


#THE routing to the landing page
#landing page is where the main process of filtering is happening
#when user is approved at signin, they are directed to landing.html
@app.route('/landing')
@login_required
def landing():
    title = 'Landing Page'
    return render_template('landing.html', title=title)



#the routing to the register page
#when user presses signup, automatically redirected tothe signup.html
@app.route('/signup', methods=['GET', 'POST'])
def register():

    title = 'Register | FilterApp'
    form = RegisterForm()
    if form.validate_on_submit(): #if correct info is entered
        users = User(username=form.username.data, email=form.email.data)
        users.set_password(form.password.data)
        db.session.add(users)
        db.session.commit()

        # message = Markup()
        flash('Account Created!' + str(users.first_name))
        # print("Account!")
        return redirect(url_for('signin'))
    return render_template('signup.html', title=title, form=form)


#routing to the signin page
#up on pressing sign in button, the user is directed to signin.html
#in signin.html the user is asked to provide auth info inorder to signin
@app.route('/signin', methods=['GET', 'POST'])
def login():

    title = 'Login | FilterApp'

    print('testing')
    user = User.query.all()

    for u in user:
        print(u.username)

    print('end testing')
    if current_user.is_authenticated:
        return redirect(url_for('landing'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).username()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('signin'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('signin')

        return redirect(next_page)

    return render_template('signin.html', title=title, form=form)
