#!/usr/bin/evn python
#-*- coding:utf-8 -*-
'''
Created on 2018年6月21日

@author: jinfeng
'''
import sqlite3

def connect_to_mssql(dbfile):
    try:
        conn = sqlite3.connect(dbfile)
        return conn
    except:
        return 0

def send_commit(conn,commit):
    cursor = conn.cursor()
    cursor.execute(commit)
    conn.commit()
    
def check_table(conn):
    commit = "select * from sqlite_master where type='table' and name = 'informationtable'"
    result = send_select(conn,commit)
    if len(result)==0:
        commit = """
    CREATE TABLE informationtable (
    姓名 NVARCHAR(255) NOT NULL,
    性别 NVARCHAR(255),
    出生年月 NVARCHAR(255),
    身份证号 NVARCHAR(255) NOT NULL,
    组别 NVARCHAR(255),
    农保 NVARCHAR(255),
    社保 NVARCHAR(255),
    医保 NVARCHAR(255),
    学历 NVARCHAR(255),
    政治面貌 NVARCHAR(255),
    工作单位 NVARCHAR(255),
    联系方式 NVARCHAR(255),
    备注 NVARCHAR(255)
)
"""
        send_commit(conn,commit)
    

def send_select(conn,commit):
    result = []
    cursor = conn.cursor()
    cursor.execute(commit)
    row = cursor.fetchone()
    while row:
        result.append(row)
        row = cursor.fetchone()
    return result

def get_rowname(conn):
    commit = "PRAGMA table_info(informationtable)"
    result = []
    cursor = conn.cursor()
    cursor.execute(commit)
    row = cursor.fetchone()
    while row:
        result.append(row[1])
        row = cursor.fetchone()
    return result

def insert_value(conn,ls):
    commit = "INSERT INTO informationtable VALUES (%s)" % ("'"+"','".join(ls)+"'").replace("'Null'","Null")
    print(commit)
    send_commit(conn,commit)

if __name__ == "__main__":
    conn = connect_to_mssql('test.db')
    commit = "select * from sqlite_master"
    result = send_select(conn, commit)
    print(result)
    ls = ['张三','男','19920406','410183199204060055','2','Null','Null','Null','大学','党员','Null','Null','Null']
    commit = "'"+"','".join(ls)+"'"

    insert_value(conn,ls)
     
    commit = "select * from sqlite_master"
    result = get_rowname(conn)
    print(result)
    result = send_select(conn, 'select * from informationtable')
    print(result)
        
        

