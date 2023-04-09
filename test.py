from requests import get, post, delete, put

print(get('http://localhost:5000/api/v2/users').json())  # все пользователи

print(get('http://localhost:5000/api/v2/users/1').json())  # один пользователь

print(post('http://localhost:5000/api/v2/users',  # добавить пользователя
           json={'surname': 'surname123',
                 'name': 'name123',
                 'email': 'email_not_registered@mars.org',
                 'age': 25,
                 'city_from': 'city_he_from',
                 'position': "admin2",
                 'speciality': 'speciality_he_is',
                 'address': "member_1"}).json())

print(delete('http://localhost:5000/api/v2/users/2'))  # удалить пользователя
