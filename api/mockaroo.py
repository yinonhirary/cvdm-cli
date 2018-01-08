from model import jsonLoad, sqllite, signup, candidate,authentication

def sign_up_multi(file_path):
    """"
    function sign up multiply user with one json data file which generate with mockaroo service
    @:param: file_path: location to the mockaroo json file
    @:type: str
    """
    data = jsonLoad.import_json(file_path)
    for row in data:
        signup.sign_up(row['userName'],str(row['userPassword']))
        query = "select id from candidate_users where user='" + str(row['userName']) + "" \
            "' and password='" + authentication.password_encrypet(str(row['userPassword'])) + "'"
        candidate.insert_candidate_information(row,(sqllite.query(query).fetchone())[0])