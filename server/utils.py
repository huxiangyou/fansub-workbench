import hashlib
from os import urandom
import sqlite3

db = sqlite3.connect('database.db')
db.close()

def md5(a: str) -> str:
    return hashlib.md5(a.encode()).hexdigest()

def salt(length: int = 3) -> str:
    return urandom(length).hex()

def sql(query: str, params: tuple = None, *, many: bool = False) -> list | None:
    while True:
        try:
            db = sqlite3.connect('database.db')
            dbc = db.cursor()
            dbc.execute('PRAGMA journal_mode=TRUNCATE')
            if params != None:
                if type(params) not in (tuple, list, dict):
                    params = (params, )
                (dbc.executemany if many else dbc.execute)(query, params)
            else:
                dbc.execute(query)
            if query.lower().startswith('select'):
                r = dbc.fetchall()
                if r and not query[:query.lower().index('from')].count(
                    ','
                ) and not query.lower().startswith('select *'):
                    r = list(next(zip(*r)))
            else:
                db.commit()
                r = None
            db.close()
        except sqlite3.OperationalError as error:
            print(query, params)
            print(error)
        else:
            return r

def sqlIn(query: str, inParams: tuple = ()) -> list | None:
    if len(inParams) > 1:
        return sql(query + ' IN {}'.format(tuple(inParams)))
    elif len(inParams) == 1:
        return sql(query + '=?', *inParams)
    else:
        return []
