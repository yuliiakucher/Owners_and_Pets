from app.owner import owner
from flask import render_template, redirect, url_for, request
from app.db import owners
from app.owner.forms import PetForm, OwnerForm
from .models import Pet, Owner
from app import owners_db
from .models_db import Owners


@owner.route('/')
def start():
    owners_db.create_all()
    if Owners.query.all():
        owners_from_db = Owners.query.all()
        return render_template('owner/index.html', owners=owners_from_db)
    else:
        return redirect(url_for('owner.owner_register'))


@owner.route('/reg', methods=['GET', 'POST'])
def owner_register():
    owners_db.create_all()
    form = OwnerForm(request.form)
    if request.method == 'POST' and form.validate():
        data = dict(request.form)
        del data['save']
        print(data['name'])
        owner_from_db = Owners(name=data['name'], age=data['age'], city=data['city'])
        # owner_from_db = Owners(name='ddddd', age=18, city='kyiv')

        owners.append(Owner(**data))
        owners_db.session.add(owner_from_db)
        owners_db.session.commit()
        return redirect(url_for('owner.start'))
    return render_template('owner/owner_register.html', form=form)


@owner.route('/<int:index>/pets')
def show_pets_by_owner(index):
    data = owners[index]
    if not data.pets:
        return redirect(url_for('owner.pet_register', index=index))
    return render_template('owner/show_pets.html', owner=data, index=index)


@owner.route('/<int:index>/pets/pet_reg', methods=['GET', 'POST'])
def pet_register(index):
    form = PetForm(request.form)
    if request.method == 'POST' and form.validate():
        data = dict(request.form)
        del data['save']
        owners[index].add_pet(**data)
        return redirect(url_for('owner.show_pets_by_owner', index=index))
    return render_template('owner/pet_register.html', form=form)


@owner.route('/<int:index>/pets/<int:pet_index>')
def del_pet(index, pet_index):
    owners[index].del_pet(pet_index)
    return redirect(url_for('owner.show_pets_by_owner', index=index))


@owner.route('pets/<string:type>')
def show_owner_by_type(type):
    rez = []
    count = 0
    for owner_item in owners:
        for pet in owner_item.pets:
            if pet.type == type:
                count += 1
                rez.append(owner_item)
    return render_template('owner/index.html', owners=rez, count=count, type=type)


@owner.route('/search_result', methods=['POST', 'GET'])
def search_result():
    result = ''
    if request.method == 'POST':
        print(request.form['search'])
        result = Owners.query.filter(Owners.name.contains(request.form['search'])).all()
        print(result)
    # return render_template('owner/search_result.html', result=result)
    return redirect(url_for('owner.start', owners=result))
