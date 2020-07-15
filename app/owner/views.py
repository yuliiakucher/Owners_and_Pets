from app.owner import owner
from flask import render_template, redirect, url_for, request
from app.owner.forms import PetForm, OwnerForm
# from .models import Pet, Owner
from app import db
from .models_db import Owners, Pets


@owner.route('/')
def start():
    db.create_all()
    if Owners.query.all():
        owners_from_db = Owners.query.all()
        return render_template('owner/index.html', owners=owners_from_db)
    else:
        return redirect(url_for('owner.owner_register'))


@owner.route('/reg', methods=['GET', 'POST'])
def owner_register():
    db.create_all()
    form = OwnerForm(request.form)
    if request.method == 'POST' and form.validate():
        data = dict(request.form)
        del data['save']
        owner_from_db = Owners(name=data['name'], age=data['age'], city=data['city'])
        db.session.add(owner_from_db)
        db.session.commit()
        return redirect(url_for('owner.start'))
    return render_template('owner/owner_register.html', form=form)


@owner.route('/<int:index>/pets')
def show_pets_by_owner(index):
    single_owner = Owners.query.filter_by(id=index).first()
    if not Pets.query.filter(Pets.owner_id.contains(index)):
        return redirect(url_for('owner.pet_register', index=index))
    return render_template('owner/show_pets.html', index=index, single_owner=single_owner)


@owner.route('/<int:index>/pets/pet_reg', methods=['GET', 'POST'])
def pet_register(index):
    form = PetForm(request.form)
    if request.method == 'POST' and form.validate():
        data = dict(request.form)
        del data['save']
        pets_for_db = Pets(owner_id=index, name=data['name'], age=data['age'], type=data['type'])
        db.session.add(pets_for_db)
        db.session.commit()
        return redirect(url_for('owner.show_pets_by_owner', index=index))
    return render_template('owner/pet_register.html', form=form)


@owner.route('/<int:index>/pets/<int:pet_index>')
def del_pet(index, pet_index):
    delete = Pets.query.filter_by(id=pet_index).first()
    db.session.delete(delete)
    db.session.commit()
    return redirect(url_for('owner.show_pets_by_owner', index=index))


@owner.route('/<int:index>')
def del_owner(index):
    delete = Owners.query.filter_by(id=index).first()
    db.session.delete(delete)
    db.session.commit()
    return redirect(url_for('owner.start'))


@owner.route('pets/<string:type>')
def show_owner_by_type(type):
    count = 0
    result = []
    rez = Pets.query.filter_by(type=type).all()
    for r in rez:
        result.append(r.owner)
        count += 1
    return render_template('owner/index.html', owners=result, count=count, type=type)


@owner.route('/search_result', methods=['POST', 'GET'])
def search_result():
    result = ''
    if request.method == 'POST':
        result = Owners.query.filter(Owners.name.contains(request.form['search'])).all()
    return render_template('owner/index.html', owners=result)
