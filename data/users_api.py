import flask
from flask import jsonify, request

from . import db_session
from .jobs import Jobs
from .users import User

blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=('surname', 'name', 'age', 'city_from', 'position', 'speciality', 'address',
                                    'email', 'modified_date'))
                 for item in users]
        }
    )


@blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'users': user.to_dict(only=('surname', 'name', 'age', 'city_from', 'position', 'speciality', 'address',
                                        'email', 'modified_date'))
        }
    )


@blueprint.route('/api/users', methods=['POST'])
def create_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['surname', 'name', 'age', 'city_from', 'position', 'speciality', 'address',
                  'email', 'modified_date']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.email == request.json['email']).first()
    if user:
        return jsonify({'error': 'User already exists'})
    user = User(
        surname=request.json['surname'],
        name=request.json['name'],
        age=request.json['age'],
        city_from=request.json['city_from'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        address=request.json['address'],
        email=request.json['email'],
        modified_date=request.json['modified_date']
    )
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(Jobs).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users', methods=['PUT'])
def edit_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'surname', 'name', 'city_from', 'age', 'position', 'speciality', 'address',
                  'email', 'modified_date']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(request.json['id'])
    if not user:
        return jsonify({'error': 'Not found'})
    user.surname = request.json['surname']
    user.name = request.json['name']
    user.city_from = request.json['city_from']
    user.age = request.json['age']
    user.position = request.json['position']
    user.speciality = request.json['speciality']
    user.address = request.json['address']
    user.email = request.json['email']
    user.modified_date = request.json['modified_date']
    db_sess.commit()
    return jsonify({'success': 'OK'})
