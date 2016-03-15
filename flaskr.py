# flaskr microblogging app

import dataset

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# connecting to a SQLite database
db = dataset.connect('sqlite:///myflaskr.db')
table = db['postings']

# create the application
app = Flask(__name__)

# show all the posting


@app.route("/")
def show_postings():
    postings = table.find() # to reverse order, table.find(order_by='-id')
    return render_template('show_postings.html', postings=postings)


@app.route("/add", methods=['POST']) # only accept connections which POST
def add_posting():
    table.insert(dict(title=request.form['title'], text=request.form['text']))
    flash("New posting successful")
    return redirect(url_for('show_postings'))

if __name__ == '__main__':
    app.debug = "TRUE"
    app.secret_key = "secret"
    app.run()
