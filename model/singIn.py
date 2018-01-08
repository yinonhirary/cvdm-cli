from model import authentication
from model import global_var


def sign_in(user_name, user_password):
    """"
    function sign in
    @:param: user_name
    @:type: str
    @:param user_password
    @:type: str
    @:return result of sign in hr/ca/none
    @:rtype str
    """
    if authentication.authentication(user_name, user_password):
        if authentication.check_perrsmisson(user_name, user_password) == True:
            global_var.main_output["add"]("permission", 1)
            return "hr"
        else:
            global_var.main_output["add"]("permission", 2)
            return "ca"
    else:
        global_var.main_output["add"]("permission", 0)
        global_var.main_output["add"]("status", 3)
        global_var.main_output["add_error"]("user name or password are wrong")
        return None
