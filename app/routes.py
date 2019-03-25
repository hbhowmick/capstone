from app import app, db
from flask import render_template, url_for, redirect, request, jsonify
from app.forms import AddressForm


@app.route('/')
@app.route('/index')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form_Address = AddressForm()
    if form_Address.validate_on_submit():
        street = form_Address.street.data
        city = form_Address.city.data
        state = form_Address.state.data
        zip = form_Address.zip.data
        return redirect('sceneview.html', form_Address=form_Address, street=street, city=city, state=state, zip=zip)

    def extents(fc):
        extent = arcpy.Describe(fc).extent
        west = extent.XMin
        south = extent.YMin
        east = extent.XMax
        north = extent.YMax
        return west, south, east, north

    return render_template('index.html', title='Home', form_Address=form_Address)

@app.route('/sceneview')
def sceneview():
    metadata = {'keywords': 'viewport', 'description':'initial-scale=1, maximum-scale=1, user-scalable=no'}
    return render_template('sceneview.html', title='3D Scene')

@app.route('/switch')
def switch():
    metadata = {'keywords': 'viewport', 'description':'initial-scale=1, maximum-scale=1, user-scalable=no'}
    return render_template('switch.html', title='Switch 2D to 3D')

@app.route('/form')
def form():
    metadata = {'keywords': 'viewport', 'description':'initial-scale=1, maximum-scale=1, user-scalable=no'}
    return render_template('form.html', title='Feature Form')

@app.route('/sketch')
def sketch():
    metadata = {'keywords': 'viewport', 'description':'initial-scale=1, maximum-scale=1, user-scalable=no'}
    return render_template('sketch.html', title='Sketch Footprint')
