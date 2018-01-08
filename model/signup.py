from model import authentication, sqllite, global_var


def sign_up(user_name, user_password):
    """"
    function sign up new user
    """
    if authentication.check_user_exist(user_name):
        global_var.main_output["add_error"]("User name already exist")
    else:
        add_new_candidate(user_name, user_password)
        global_var.main_output["add_error"]("you successful sign up")


def add_new_candidate(user_name, user_password):
    """"
    function adding the candidate user to database table
    """
    query = "INSERT INTO `candidate_users` (`id`,`user`,`password`) VALUES (NULL ,'" + str(user_name) + "','" + str(
        authentication.password_encrypet(user_password)) + "')"
    sqllite.insert__update_query(query)
