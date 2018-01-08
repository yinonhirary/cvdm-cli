from model import jsonLoad, global_var, sqllite
from api import cloudinary
import json


def export_json_file():
    json_data = {'notes': {}, 'image': 'https://imagelocation',
                 'expAndSkill': {'specillaztion': {}, 'previousCareer': {}},
                 'sortAcademic': {"1": {"post_doctoral": 0},"2": {"teaching_in_postscenodry": 0},"3": {"high_level_research": 0},"4": {"fellowship_grants": 0}}, 'phoneNumber': '',
                 'AcadmicHistory': {'education': {}, 'researchersAndProject': {}},
                 'status': {'1': {'hired': 0}, '3': {'onhold': 1}, '2': {'rejected': 0}},
                 'email': 'youreEmail@gmail.com',
                 'name': 'YoureFullName'}
    query = "SELECT * FROM `candidateInformation` WHERE `mid` == '{0}'".format(global_var.user_id)
    row = sqllite.query(query).fetchone()
    print(row[1])
    json_data['name'] = row[1]
    json_data['email'] = row[2]
    json_data['phoneNumber'] = row[3]
    json_data['image'] = row[6]
    filename = "candidate." + str(global_var.user_id)
    ################################## AcadmicHistory->education ###########################################
    query = "SELECT * FROM `education` WHERE `mid` == '{0}'".format(global_var.user_id)
    tmp = {}
    i = 1
    for row in sqllite.query(query).fetchall():
        print(row[2])
        tmp[i] = {}
        tmp[i]["date"] = row[1]
        tmp[i]["description"] = row[2]
        i+=1
    json_data["AcadmicHistory"]["education"] = tmp
    ################################## AcadmicHistory->researchersAndProject ###########################################
    query = "SELECT * FROM `researchersAndProject` WHERE `mid` == '{0}'".format(global_var.user_id)
    tmp = {}
    i = 1
    for row in sqllite.query(query).fetchall():
        print(row[2])
        tmp[i] = {}
        tmp[i]["date"] = row[1]
        tmp[i]["description"] = row[2]
        i+=1
    json_data["AcadmicHistory"]["researchersAndProject"] = tmp
    ################################## expAndSkill->specillaztion ###########################################
    query = "SELECT * FROM `specillaztion` WHERE `mid` == '{0}'".format(global_var.user_id)
    tmp = {}
    i = 1
    for row in sqllite.query(query).fetchall():
        print(row[2])
        tmp[i] = {}
        tmp[i]["date"] = row[1]
        tmp[i]["description"] = row[2]
        i += 1
    json_data["expAndSkill"]["specillaztion"] = tmp
    ################################## expAndSkill->previousCareer ###########################################
    query = "SELECT * FROM `previousCareer` WHERE `mid` == '{0}'".format(global_var.user_id)
    tmp = {}
    i = 1
    for row in sqllite.query(query).fetchall():
        print(row[2])
        tmp[i] = {}
        tmp[i]["date"] = row[1]
        tmp[i]["description"] = row[2]
        i += 1
    json_data["expAndSkill"]["specillaztion"] = tmp
    ################################## notes ###########################################
    query = "SELECT * FROM `notes` WHERE `mid` == '{0}'".format(global_var.user_id)
    tmp = {}
    i = 1
    for row in sqllite.query(query).fetchall():
        print(row[2])
        tmp[i] = {}
        tmp[i]["date"] = row[1]
        tmp[i]["description"] = row[2]
        i += 1
    json_data["notes"] = tmp
    ############################# save json file in files folder ###############################
    with open(("files/" + filename + '.json'), 'w') as outfile:
        json.dump(json_data, outfile, indent=2)
    ############################# log event ####################################################
    global_var.main_output["add"]("status", 9)
    global_var.main_output["add_log"](
        "candidate file saves as {0}.json in folder files.".format(filename))
    global_var.main_output["add"]("file_location", "files/" + filename+".json")

def import_json_file(file):
    json_data = jsonLoad.import_json(file)
    insert_candidate_information(json_data)


def empty_json_template():
    return {'notes': {'1': {'description': ''}, '2': {'description': ''}}, 'image': 'https://imagelocation',
            'expAndSkill': {'specillaztion': {'1': {'description': 'field description', 'date': '2015'},
                                              '3': {'description': 'field description', 'date': '2013'},
                                              '2': {'description': 'field description', 'date': '2014'}},
                            'previousCareer': {'1': {'description': 'field description', 'date': '2015'},
                                               '3': {'description': 'field description', 'date': '2013'},
                                               '2': {'description': 'field description', 'date': '2014'}}},
            'sortAcademic': {'1': {'post_doctoral': 1}, '4': {'fellowship_grants': 0}, '3': {'high_level_research': 0},
                             '2': {'teaching_in_postscenodry': 0}}, 'phoneNumber': '', 'AcadmicHistory': {
            'education': {'1': {'description': 'field description', 'date': '2015'},
                          '3': {'description': 'field description', 'date': '2013'},
                          '2': {'description': 'field description', 'date': '2014'}},
            'researchersAndProject': {'1': {'description': 'field description', 'date': '2015'},
                                      '3': {'description': 'field description', 'date': '2013'},
                                      '2': {'description': 'field description', 'date': '2014'}}},
            'status': {'1': {'hired': 0}, '3': {'onhold': 1}, '2': {'rejected': 0}}, 'email': 'youreEmail@gmail.com',
            'name': 'YoureFullName'}


def write_json_file(data, filename):
    with open(("files/" + filename + '.json'), 'w') as outfile:
        json.dump(data, outfile, indent=2)
    global_var.main_output["add"]("status", 7)
    global_var.main_output["add_log"](
        "template file saves as template.json, fill the template and import the file back.")


def insert_candidate_information(data, id = None):
    """"
    function storing data in the database
    """
    ######################################## delete old record ############################################
    if id == None:
        id = global_var.user_id
    query = "DELETE FROM `education` WHERE `mid`== {0}".format(id)
    sqllite.query(query)
    query = "DELETE FROM `notes` WHERE `mid`== {0}".format(id)
    sqllite.query(query)
    query = "DELETE FROM `previousCareer` WHERE `mid`== {0}".format(id)
    sqllite.query(query)
    query = "DELETE FROM `researchersAndProject` WHERE `mid`== {0}".format(id)
    sqllite.query(query)
    query = "DELETE FROM `specillaztion` WHERE `mid`== {0}".format(id)
    sqllite.query(query)

    ############################# AcadmicHistory->education #######################
    i = 1
    for k, v in data['AcadmicHistory']['education'].items():
        query1 = "INSERT INTO `education`(`id`,`date`,`description`,`mid`,`sn`) VALUES (NULL,'{0}','{1}','{2}',{3});".format(
            v["date"], v["description"], id, i)
        i += 1
        sqllite.insert__update_query(query1)
    ############################# AcadmicHistory->researchersAndProject ##############################################
    i = 1
    for k, v in data['AcadmicHistory']['researchersAndProject'].items():
        query1 = "INSERT INTO `researchersAndProject`(`id`,`date`,`description`,`mid`,`sn`) VALUES (NULL,'{0}','{1}','{2}',{3});".format(
            v["date"], v["description"], id, i)
        i += 1
        sqllite.insert__update_query(query1)
    ############################# expAndSkill->previousCareer ##############################################
    i = 1
    for k, v in data['expAndSkill']['previousCareer'].items():
        query1 = "INSERT INTO `previousCareer`(`id`,`date`,`description`,`mid`,`sn`) VALUES (NULL,'{0}','{1}','{2}',{3});".format(
            v["date"], v["description"], id, i)
        i += 1
        sqllite.insert__update_query(query1)
    ############################# expAndSkill->specillaztion ##############################################
    i = 1
    for k, v in data['expAndSkill']['specillaztion'].items():
        query1 = "INSERT INTO `specillaztion`(`id`,`date`,`description`,`mid`,`sn`) VALUES (NULL,'{0}','{1}','{2}',{3});".format(
            v["date"], v["description"], id, i)
        i += 1
        sqllite.insert__update_query(query1)
    ############################# note ##############################################
    i = 1
    for k, v in data['notes'].items():
        query1 = "INSERT INTO `notes`(`id`,`date`,`description`,`mid`,`sn`) VALUES (NULL,NULL,'{0}','{1}',{2});".format(
            v["description"], id, i)
        i += 1
        sqllite.insert__update_query(query1)
    query = "SELECT * FROM `candidateInformation` WHERE `mid` == '{0}'".format(id)
    if sqllite.countRow(sqllite.query(query)) == 0:
        query = "INSERT INTO `candidateInformation`(`id`,`name`,`email`,`phoneNumber`," \
                "`status`,`mid`,`image`) " \
                "VALUES (NULL ,'{0}','{1}','{2}',0,'{3}','{4}');".format(data['name'],
                                                                   data['email'],
                                                                   data['phoneNumber'],
                                                                   id,data['image'])

        sqllite.insert__update_query(query)
        #cloudinary.uploadImg(data['image'])
    else:
        query = "UPDATE `candidateInformation` SET `name` ='{0}', `email` ='{1}', `phoneNumber`='{2}', `image`='{3}'" \
                " WHERE `mid`='{4}';".format(data['name'], data['email'], data['phoneNumber'], data['image'], id)
        sqllite.insert__update_query(query)
