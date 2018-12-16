from app_mic import app
from flask import render_template, flash, redirect, request, url_for
from app_mic.forms import LoginForm, MethodForm
from wtforms import SubmitField

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form_method = MethodForm()
    methods = [
                {'method_url' : 'fractiles',
                 'method_name' : 'Fractiles'
                },

                {'method_url' : 'gamblelike',
                 'method_name' : 'Gamblelike'
                },

                {'method_url' : 'probawheel',
                 'method_name' : 'Probability Wheel'
                }
            ]
    m_choice = request.form.get("method_choice")
    if form_method.validate_on_submit():
        print(m_choice, 'redirected')
        return redirect(url_for(m_choice))
    return render_template('index.html', title='Home', methods=methods, form=form_method)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/fractiles')
def fractiles():
    probas = {'lottery': 'voyage'}
    return render_template('fractiles.html', title='Fractiles')

@app.route('/gamblelike')
def gamblelike():
    probas = {'lottery': 'voyage'}
    return render_template('gamblelike.html', title='Gamblelike')

@app.route('/probawheel')
def probawheel():
    probas = {'lottery': 'voyage'}
    return render_template('probawheel.html', title='Probability Wheel')
