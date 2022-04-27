from app import *
from flask import redirect, url_for
from app.models.user import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(int(user_id))


class LoginForm(FlaskForm):
    nickname = StringField('nickname', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=10)])
    remember = BooleanField('Remember Me')


class SignUp(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=30)])
    nickname = StringField('nickname', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=10)])
    gender = RadioField('gender', choices=[('female'), ('male')])
    robot = BooleanField('I\'m not a robot')


@app.route('/')
def main():
    return render_template('main.html', title='Головна сторінка')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(nickname=form.nickname.data).first()
        if user:
            if user.password == form.password.data:
                login_user(user, remember=form.remember.data)
                return redirect(url_for('homepage'))
        return '<h1>Invalid username or password</h1>'
    return render_template('login.html', title='Увійти', form=form)


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = SignUp()

    if form.validate_on_submit():
        hashed_psw = generate_password_hash(form.password.data, method='sha256')
        new_user = User(nickname=form.nickname.data,
                        password=hashed_psw,
                        email=form.email.data,
                        gender=form.gender.data)
        db.session.add(new_user)
        db.session.commit()
        return 'new_user has beent created'
    return render_template('signup.html', title='Реєстрація', form=form)


@app.route('/homepage')
@login_required
def homepage():
    return render_template('homepage.html', name=current_user.nickname)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
