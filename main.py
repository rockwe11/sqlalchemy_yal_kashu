from flask import Flask, render_template, redirect
from data import db_session
from data.news import News

from data.users import User
from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


# @app.route("/")
# def index():
#     db_sess = db_session.create_session()
#     news = db_sess.query(News).filter(News.is_private != True)
#     return render_template("index.html", news=news)
#
#
# @app.route('/register', methods=['GET', 'POST'])
# def reqister():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         if form.password.data != form.password_again.data:
#             return render_template('register.html', title='Регистрация',
#                                    form=form,
#                                    message="Пароли не совпадают")
#         db_sess = db_session.create_session()
#         if db_sess.query(User).filter(User.email == form.email.data).first():
#             return render_template('register.html', title='Регистрация',
#                                    form=form,
#                                    message="Такой пользователь уже есть")
#         user = User(
#             name=form.name.data,
#             email=form.email.data,
#             about=form.about.data
#         )
#         user.set_password(form.password.data)
#         db_sess.add(user)
#         db_sess.commit()
#         return redirect('/login')
#     return render_template('register.html', title='Регистрация', form=form)


def main():
    db_session.global_init("db/ship.db")
    db_sess = db_session.create_session()
    captain = User(surname="Scott", name="Ridley", age=21, position="captain", speciality="research engineer",
                   address="module_1", email="scott_chief@mars.org")
    col1 = User(surname="Weir", name="Andy", age=22, position="colonist", speciality="chief scientist",
                address="module_1", email="weir_chief@mars.org")
    col2 = User(surname="Bean", name="Sean", age=17, position="colonist", speciality="middle scientist",
                address="module_1", email="beaner@mars.org")
    col3 = User(surname="Kapoor", name="Venkat", age=15, position="colonist", speciality="industrial engineer",
                address="module_1", email="kapporich@mars.org")
    db_sess.add(captain)
    db_sess.add(col1)
    db_sess.add(col2)
    db_sess.add(col3)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()