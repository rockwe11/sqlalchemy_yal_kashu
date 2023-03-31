import flask
from flask import jsonify, request

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('job', 'work_size', 'category', 'user.surname', 'user.name'))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:news_id>', methods=['GET'])
def get_one_news(news_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(news_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'jobs': jobs.to_dict(only=(
                'job', 'work_size', 'category', 'user.surname', 'user.name'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['job', 'work_size', 'team_leader', 'collaborators', 'category', 'is_finished']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.job == request.json['job']).first()
    if job:
        return jsonify({'error': 'Job already exists'})
    jobs = Jobs(
        job=request.json['job'],
        work_size=request.json['work_size'],
        team_leader=request.json['team_leader'],
        collaborators=request.json['collaborators'],
        category=request.json['category'],
        is_finished=request.json['is_finished']
    )
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_jobs(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    db_sess.delete(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs', methods=['PUT'])
def edit_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'job', 'work_size', 'team_leader', 'collaborators', 'category', 'is_finished']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(request.json['id'])
    if not jobs:
        return jsonify({'error': 'Not found'})
    jobs.job = request.json['job']
    jobs.work_size = request.json['work_size']
    jobs.team_leader = request.json['team_leader']
    jobs.collaborators = request.json['collaborators']
    jobs.category = request.json['category']
    jobs.is_finished = request.json['is_finished']
    db_sess.commit()
    return jsonify({'success': 'OK'})
