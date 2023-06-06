# Run this file when the first time to init the program

import utils

utils.sql(
    '''CREATE TABLE users (
        userId TEXT UNIQUE,
        username TEXT,
        passwordSalt TEXT,
        passwordHash TEXT,
        approved INTEGER
    )'''
)
