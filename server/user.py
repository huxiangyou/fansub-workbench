from app import app
from flask import request
from flask import session
import utils

app.secret_key = utils.salt(16)
'''
About password and salt:
1. Get a salt. When sign up, generate on frontend. When login, get loginSalt() from database.
2. Frontend: md5(md5(password) + salt) -> login()
3. md5(... + salt) -> compare with database
'''

@app.route('/api/signUp', methods=['POST'])
def signUp():
    username = request.json.get('username')
    passwordSalt = request.json.get('passwordSalt')
    passwordHashReceived = request.json.get('passwordHash')

    if utils.sql('SELECT username FROM users WHERE username=?', username):
        return {'result': False, 'message': '同名用户已注册'}

    userId = utils.salt()
    utils.sql(
        'INSERT INTO users VALUES (?, ?, ?, ?, 0)', (
            userId, username, passwordSalt,
            utils.md5(passwordHashReceived + passwordSalt)
        )
    )

    return {'result': True}

@app.route('/api/loginSalt', methods=['GET'])
def loginSalt():
    username = request.json.get('username')

    if not utils.sql('SELECT username FROM users WHERE username=?', username):
        return {'result': False, 'message': '未注册此用户'}

    passwordSalt, = utils.sql(
        'SELECT passwordSalt FROM users WHERE username=?', username
    )

    return {
        'result': True,
        'message': '',
        'data': {
            'passwordSalt': passwordSalt
        }
    }

@app.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('username')
    passwordHashReceived = request.json.get('passwordHash')
    newPasswordSalt = request.json.get('newPasswordSalt')
    newPasswordHashReceived = request.json.get('newPasswordHash')

    if not utils.sql('SELECT username FROM users WHERE username=?', username):
        return {'result': False, 'message': '未注册此用户'}

    (userId, passwordSalt, passwordHash), = utils.sql(
        'SELECT userId, passwordSalt, passwordHash FROM users WHERE username=?',
        username
    )
    if not utils.md5(passwordHashReceived + passwordSalt) == passwordHash:
        return {'result': False, 'message': '密码错误'}

    utils.sql(
        'UPDATE users SET passwordSalt=?, passwordHash=? WHERE userId=?', (
            newPasswordSalt,
            utils.md5(newPasswordHashReceived + newPasswordSalt), userId
        )
    )

    session['userId'] = userId

    return {'result': True}

@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('userId', None)

    return {'result': True}

@app.route('/api/changeUsername', methods=['POST'])
def changeUsername():
    newUsername = request.json.get('newUsername')

    if not session.get('userId'):
        return {'result': False, 'message': '未登录'}

    utils.sql(
        'UPDATE users SET username=? WHERE userId=?',
        (newUsername, session.get('userId'))
    )

    return {'result': True}

@app.route('/api/changePassword', methods=['POST'])
def changePassword():
    newPasswordSalt = request.json.get('newPasswordSalt')
    passwordHashReceived = request.json.get('newPasswordHash')

    if not session.get('userId'):
        return {'result': False, 'message': '未登录'}

    utils.sql(
        'UPDATE users SET passwordSalt=?, passwordHash=? WHERE userId=?', (
            newPasswordSalt, utils.md5(passwordHashReceived + newPasswordSalt),
            session.get('userId')
        )
    )

    return {'result': True}
