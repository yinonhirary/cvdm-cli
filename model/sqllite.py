import sqlite3
databaseName =""
password =""
conn = None
c = None


def connectDatabase():
    """
    function connecting to the database
    :return:
    """
    global c
    global conn
    conn = sqlite3.connect('cvdm.db')
    c = conn.cursor()
    

def disConnectDataBase():
    """
    function disconnect the dataBase
    :return:
    """
    conn.close()


def query(queryString):
    """
    function run query on our database
    :param queryString:
    :return:
    """
    c.execute(queryString)
    return c


def insert__update_query(queryString):
    """
    function run query on our database
    :param queryString:
    :return:
    """
    c.execute(queryString)
    conn.commit()
    return c

def countRow(queryResualt):
    """"
    function counting query row number and return the count
    @:return int
    """
    return len(queryResualt.fetchall())