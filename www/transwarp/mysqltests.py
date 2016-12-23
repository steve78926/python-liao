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
    data = cur.fetchall()
    for row in data:
        for col in row:
            print col,  #变量加逗号，输出时不换行
        print "\n"

if __name__ == '__main__':
    #mysqltests('select * from user')
    import doctest
    doctest.testmod()

