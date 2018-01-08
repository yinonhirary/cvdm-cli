from model import singIn, signup, sqllite, cliArgument, jsonLoad, outputJson
from model import global_var
from route import hr_route, ca_route
from api import mockaroo


def default_route():
    """"
        default route function
    """
    global_var.main_output = outputJson.output_json()
    sqllite.connectDatabase()
    user_name = cliArgument.args.user
    user_password = cliArgument.args.password

    global_var.main_output["add"]("status", 0)  # not logged yet
    if cliArgument.args.login:  # login option
        if user_name and user_password:
            response = singIn.sign_in(user_name, user_password)  # check if user exist and what is permission
            if response == "hr":
                global_var.user_permission = 1
                global_var.main_output["add"]("status", 1)
                hr_route.hr_route()
            elif response == "ca":
                global_var.user_permission = 2
                global_var.main_output["add"]("status", 1)
                ca_route.ca_route()
        else:  # if user or password are missing
            global_var.main_output["add"]("status", 2)
            global_var.main_output["add_error"]("user name or password are missing")
    elif cliArgument.args.sign_up:  # signup option
        if user_name and user_password:
            signup.sign_up(user_name, user_password)
        else: # if user or password are missing
            global_var.main_output["add"]("status", 2)
            global_var.main_output["add_error"]("user name and password must entry")
    elif cliArgument.args.sign_up_multi:
        mockaroo.sign_up_multi(cliArgument.args.sign_up_multi)


    jsonLoad.preetyPrintJson(global_var.main_output["output"]())
    sqllite.disConnectDataBase()
