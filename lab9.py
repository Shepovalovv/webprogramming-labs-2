from flask import Blueprint, redirect, url_for, render_template, request
lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def lab():
    return render_template('lab9/index.html')


@lab9.app_errorhandler(404)
def not_found(er):
    return render_template('lab9/error.html')


@lab9.app_errorhandler(500)
def error500(er):
    return render_template('lab9/error.html')

