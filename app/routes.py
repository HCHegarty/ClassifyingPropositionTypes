from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import DataEntryForm

@app.route('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = DataEntryForm()
    if form.validate_on_submit():
        flash('Analysis requested for text {}'.format(
            form.text.data))
        return redirect(url_for('index'))
    return render_template('data_entry.html', title='Enter Text', form=form)


@app.route('/index')
def index():
    user = {'username': 'Christian'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

