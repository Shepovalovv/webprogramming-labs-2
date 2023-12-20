from flask import Blueprint, redirect, url_for, render_template, request
lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def lab():
    return render_template('lab9/index.html')


