#-*- coding:utf8 -*-

import mysql.connector
from dbconfig import db_cfg

def mysqltests(sql):
    '''
    >>> mysqltests('select count(*) from user')
    9
    >>>
    '''
    conn = mysql.connector.connect(host=db_cfg['host'],
                               user=db_cfg['user'],
                               password=db_cfg['password'],
                               database=db_cfg['database'],
                               use_unicode=True)
    cur = conn.cursor()
    cur.execute(sql)
    print cur.fetchone()[0]

if __name__ == '__main__':
    mysqltests('select count(*) from user')
    import doctest
    doctest.testmod()

