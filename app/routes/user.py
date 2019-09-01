from flask import flash, render_template, redirect, url_for, request, session, g
from werkzeug.security import check_password_hash, generate_password_hash

from app import app, db
from app.forms.user import LoginForm, RegisterationForm
from app.models.user import User

@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data

        error = None
        user = User.query.filter_by(username=username).first()

        if user is None:
            error = 'Incorrect username.'
        #elif not check_password_hash(user.password, password):
        elif not (user.password == password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user.id

            return redirect(url_for('index'))

        flash(error)

    return render_template('user/login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterationForm(request.form)

    if request.method == 'POST' and form.validate():
        username = request.form['username']
        password = request.form['password']
        nickname = request.form['nickname']

        #users = User(nickname=nickname, username=username, password=generate_password_hash(password))
        users = User(nickname=nickname, username=username, password=password)
        db.session.add(users)
        db.session.commit()
        flash('성공')
        return redirect(url_for('login'))

    return render_template('user/register.html', form=form)


@app.before_request
def before_request():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).all()


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
