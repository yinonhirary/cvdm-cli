from model import jsonLoad, global_var, sqllite
import json


def get_candidate_card(id):
    json_data = {'notes': {}, 'image': 'https://imagelocation',
                 'expAndSkill': {'specillaztion': {}, 'previousCareer': {}},
                 'sortAcademic': {}, 'phoneNumber': '',
                 'AcadmicHistory': {'education': {}, 'researchersAndProject': {}},
                 'status': {'1': {'hired': 0}, '3': {'onhold': 1}, '2': {'rejected': 0}},
                 'email': 'youreEmail@gmail.com',
                 'name': 'YoureFullName'}
    query = "SELECT * FROM `candidateInformation` WHERE `mid` == '{0}'".format(id)
    if sqllite.countRow(sqllite.query(query)) == 0:
        global_var.main_output["add"]("status", 10)
        global_var.main_output["add_log"](
            "candidate {0} not exist.".format(id))
        return
    row = sqllite.query(query).fetchone()
    json_data['id'] = row[5]
    json_data['name'] = row[1]
    json_data['email'] = row[2]
    json_data['phoneNumber'] = row[3]
    json_data['image'] = row[6]
    filename = "candidate." + str(id)
    ################################## AcadmicHistory->education ###########################################
    query = "SELECT * FROM `education` WHERE `mid` == '{0}'".format(id)
    tmp = {}
    i = 1
    for row in sqllite.query(query).fetchall():
        tmp[i] = {}
        tmp[i]["date"] = row[1]
        tmp[i]["description"] = row[2]
        i += 1
    json_data["AcadmicHistory"]["education"] = tmp
    ################################## AcadmicHistory->researchersAndProject ###########################################
    query = "SELECT * FROM `researchersAndProject` WHERE `mid` == '{0}'".format(id)
    tmp = {}
    i = 1
    for row in sqllite.query(query).fetchall():
        tmp[i] = {}
        tmp[i]["date"] = row[1]
        tmp[i]["description"] = row[2]
        i += 1
    json_data["AcadmicHistory"]["researchersAndProject"] = tmp
    ################################## expAndSkill->specillaztion ###########################################
    query = "SELECT * FROM `specillaztion` WHERE `mid` == '{0}'".format(id)
    tmp = {}
    i = 1
    for row in sqllite.query(query).fetchall():
        tmp[i] = {}
        tmp[i]["date"] = row[1]
        tmp[i]["description"] = row[2]
        i += 1
    json_data["expAndSkill"]["specillaztion"] = tmp
    ################################## expAndSkill->previousCareer ###########################################
    query = "SELECT * FROM `previousCareer` WHERE `mid` == '{0}'".format(id)
    tmp = {}
    i = 1
    for row in sqllite.query(query).fetchall():
        tmp[i] = {}
        tmp[i]["date"] = row[1]
        tmp[i]["description"] = row[2]
        i += 1
    json_data["expAndSkill"]["specillaztion"] = tmp
    ################################## notes ###########################################
    query = "SELECT * FROM `notes` WHERE `mid` == '{0}'".format(id)
    tmp = {}
    i = 1
    for row in sqllite.query(query).fetchall():
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
    global_var.main_output["add"]("file_location", "files/" + filename+".json")
    global_var.main_output["add_log"](
        "candidate file saves as {0}.json in folder files.".format(filename))

    def insert_candidate_information(data):
        """"
        function storing data in the database
        """
        ######################################## delete old record ############################################
        query = "DELETE FROM `education` WHERE `mid`== {0}".format(global_var.user_id)
        sqllite.query(query)
        query = "DELETE FROM `notes` WHERE `mid`== {0}".format(global_var.user_id)
        sqllite.query(query)
        query = "DELETE FROM `previousCareer` WHERE `mid`== {0}".format(global_var.user_id)
        sqllite.query(query)
        query = "DELETE FROM `researchersAndProject` WHERE `mid`== {0}".format(global_var.user_id)
        sqllite.query(query)
        query = "DELETE FROM `specillaztion` WHERE `mid`== {0}".format(global_var.user_id)
        sqllite.query(query)

        ############################# AcadmicHistory - >education #######################
        i = 1
        for k, v in data['AcadmicHistory']['education'].items():
            query1 = "INSERT INTO `education`(`id`,`date`,`description`,`mid`,`sn`) VALUES (NULL,'{0}','{1}','{2}',{3});".format(
                v["date"], v["description"], global_var.user_id, i)
            i += 1
            sqllite.insert__update_query(query1)
        ############################# AcadmicHistory->researchersAndProject ##############################################
        i = 1
        for k, v in data['AcadmicHistory']['researchersAndProject'].items():
            query1 = "INSERT INTO `researchersAndProject`(`id`,`date`,`description`,`mid`,`sn`) VALUES (NULL,'{0}','{1}','{2}',{3});".format(
                v["date"], v["description"], global_var.user_id, i)
            i += 1
            sqllite.insert__update_query(query1)
        ############################# expAndSkill->previousCareer ##############################################
        i = 1
        for k, v in data['expAndSkill']['previousCareer'].items():
            query1 = "INSERT INTO `previousCareer`(`id`,`date`,`description`,`mid`,`sn`) VALUES (NULL,'{0}','{1}','{2}',{3});".format(
                v["date"], v["description"], global_var.user_id, i)
            i += 1
            sqllite.insert__update_query(query1)
        ############################# expAndSkill->specillaztion ##############################################
        i = 1
        for k, v in data['expAndSkill']['specillaztion'].items():
            query1 = "INSERT INTO `specillaztion`(`id`,`date`,`description`,`mid`,`sn`) VALUES (NULL,'{0}','{1}','{2}',{3});".format(
                v["date"], v["description"], global_var.user_id, i)
            i += 1
            sqllite.insert__update_query(query1)
        ############################# note ##############################################
        i = 1
        for k, v in data['notes'].items():
            query1 = "INSERT INTO `notes`(`id`,`date`,`description`,`mid`,`sn`) VALUES (NULL,NULL,'{0}','{1}',{2});".format(
                v["description"], global_var.user_id, i)
            i += 1
            sqllite.insert__update_query(query1)
        query = "SELECT * FROM `candidateInformation` WHERE `mid` == '{0}'".format(global_var.user_id)
        if sqllite.countRow(sqllite.query(query)) == 0:
            query = "INSERT INTO `candidateInformation`(`id`,`name`,`email`,`phoneNumber`," \
                    "`status`,`mid`) " \
                    "VALUES (NULL ,'{0}','{1}','{2}',0,'{3}');".format(data['name'],
                                                                       data['email'],
                                                                       data['phoneNumber'],
                                                                       global_var.user_id)

            sqllite.insert__update_query(query)
        else:
            query = "UPDATE `candidateInformation` SET `name` ='{0}', `email` ='{1}', `phoneNumber`='{2}'" \
                    " WHERE `mid`='{3}';".format(data['name'], data['email'], data['phoneNumber'], global_var.user_id)
            sqllite.insert__update_query(query)


def insert_candidate_information(data):
    """"
    function storing data in the database
    """
    ######################################## delete old record ############################################
    query = "DELETE FROM `education` WHERE `mid`== {0}".format(data['id'])
    sqllite.query(query)
    query = "DELETE FROM `notes` WHERE `mid`== {0}".format(data['id'])
    sqllite.query(query)
    query = "DELETE FROM `previousCareer` WHERE `mid`== {0}".format(data['id'])
    sqllite.query(query)
    query = "DELETE FROM `researchersAndProject` WHERE `mid`== {0}".format(data['id'])
    sqllite.query(query)
    query = "DELETE FROM `specillaztion` WHERE `mid`== {0}".format(data['id'])
    sqllite.query(query)

    ############################# AcadmicHistory - >education #######################
    i = 1
    for k, v in data['AcadmicHistory']['education'].items():
        query1 = "INSERT INTO `education`(`id`,`date`,`description`,`mid`,`sn`) VALUES (NULL,'{0}','{1}','{2}',{3});".format(
            v["date"], v["description"], data['id'], i)
        i += 1
        sqllite.insert__update_query(query1)
    ############################# AcadmicHistory->researchersAndProject ##############################################
    i = 1
    for k, v in data['AcadmicHistory']['researchersAndProject'].items():
        query1 = "INSERT INTO `researchersAndProject`(`id`,`date`,`description`,`mid`,`sn`) VALUES (NULL,'{0}','{1}','{2}',{3});".format(
            v["date"], v["description"], data['id'], i)
        i += 1
        sqllite.insert__update_query(query1)
    ############################# expAndSkill->previousCareer ##############################################
    i = 1
    for k, v in data['expAndSkill']['previousCareer'].items():
        query1 = "INSERT INTO `previousCareer`(`id`,`date`,`description`,`mid`,`sn`) VALUES (NULL,'{0}','{1}','{2}',{3});".format(
            v["date"], v["description"], data['id'], i)
        i += 1
        sqllite.insert__update_query(query1)
    ############################# expAndSkill->specillaztion ##############################################
    i = 1
    for k, v in data['expAndSkill']['specillaztion'].items():
        query1 = "INSERT INTO `specillaztion`(`id`,`date`,`description`,`mid`,`sn`) VALUES (NULL,'{0}','{1}','{2}',{3});".format(
            v["date"], v["description"], data['id'], i)
        i += 1
        sqllite.insert__update_query(query1)
    ############################# note ##############################################
    i = 1
    for k, v in data['notes'].items():
        query1 = "INSERT INTO `notes`(`id`,`date`,`description`,`mid`,`sn`) VALUES (NULL,NULL,'{0}','{1}',{2});".format(
            v["description"], data['id'], i)
        i += 1
        sqllite.insert__update_query(query1)
    query = "SELECT * FROM `candidateInformation` WHERE `mid` == '{0}'".format(data['id'])
    status = 0
    if data['status']['1']['hired'] == 1:
        print('hired')
        status = 1
    elif data['status']['2']['rejected'] == 1:
        print('rejected')
        status = 2
    elif data['status']['3']['onhold'] == 1:
        status = 3
    if sqllite.countRow(sqllite.query(query)) == 0:
        query = "INSERT INTO `candidateInformation`(`id`,`name`,`email`,`phoneNumber`," \
                "`status`,`mid`,`status`) " \
                "VALUES (NULL ,'{0}','{1}','{2}',0,'{3},{4}');".format(data['name'],
                                                                   data['email'],
                                                                   data['phoneNumber'],
                                                                   data['id'],
                                                                       status)

        sqllite.insert__update_query(query)
    else:
        query = "UPDATE `candidateInformation` SET `name` ='{0}', `email` ='{1}', `phoneNumber`='{2}', `status`='{3}'" \
                " WHERE `mid`='{4}';".format(data['name'], data['email'], data['phoneNumber'], status, data['id'])
        sqllite.insert__update_query(query)

def update_candidate_card(file):
    json_data = jsonLoad.import_json(file)
    insert_candidate_information(json_data)

def search(searchType,searchValue = None):
    searchType = int(searchType)
    if searchType == 1:## sort acedmic seach
        query = "SELECT id FROM `candidateInformation` WHERE `sortAcademic` == {0}".format(int(searchValue))
        if sqllite.countRow(sqllite.query(query)) == 0:
            global_var.main_output["add"]("status", 15)
            global_var.main_output["add_log"]("0 row found for this searching query.")
        else:
            global_var.main_output["add"]("status", 16)
            global_var.main_output["add_log"]("{0} row found for this searching query.".format(sqllite.countRow(sqllite.query(query))))
            resualt = ""
            rows = sqllite.query(query).fetchall()
            for row in rows:
                resualt += str(row[0]) +","
            resualt = resualt[:-1]
            global_var.main_output["add"]("result",resualt)
            rows = sqllite.query(query).fetchall()

    elif searchType == 2:## academic history search
        query = "SELECT id FROM `researchersAndProject` WHERE `description` == {0}".format(int(searchValue))
        if sqllite.countRow(sqllite.query(query)) == 0:
            global_var.main_output["add"]("status", 15)
            global_var.main_output["add_log"]("0 row found for this searching query.")
        else:
            pass
    elif searchType == 3:
        pass
