import hashlib
from model import sqllite,global_var

def authentication(userName, password):
    global_var.user_name = userName
    global_var.user_password = str(password_encrypet(password))
    query1 = "select id from HR_users where user='"+str(global_var.user_name)+"' and password='"+str(password_encrypet(password))+"'"
    query2 = "select id from candidate_users where user='" + str(userName) + "' and password='" + global_var.user_password + "'"

    if sqllite.countRow(sqllite.query(query1)) == 1 or sqllite.countRow(sqllite.query(query2)) == 1:
        if(sqllite.countRow(sqllite.query(query1)) == 1):
            global_var.user_id = (sqllite.query(query1).fetchone()[0])
        elif sqllite.countRow(sqllite.query(query2)) == 1:
            global_var.user_id = (sqllite.query(query2).fetchone()[0])
        return True
    return False


def check_perrsmisson(userName, password):
    query = "select id from HR_users where user='" + str(userName) + "' and password='" + str(password_encrypet(password)) + "'"
    if sqllite.countRow(sqllite.query(query)) == 1:
        return True
    return False


def password_encrypet(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()


def check_user_exist(userName):
    query = "select * from candidate_users where user='"+str(userName)+"'"
    if sqllite.countRow(sqllite.query(query)) == 1:
        return True
    query = "select * from HR_users where user='"+str(userName)+"'"
    if sqllite.countRow(sqllite.query(query)) == 1:
        return True
    return False
