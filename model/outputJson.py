def output_json():
    dict = {}
    error_messages = []
    log_messages = []

    def add(key, value):
        dict[key] = value

    def add_error(error_message):
        error_messages.append(error_message)

    def add_log(log_message):
        log_messages.append(log_message)

    def output():
        tmp1 = {}
        tmp2 = {}
        i = 1
        if len(error_messages) > 0:
            for msg in error_messages:
                tmp1[i] = msg
                i += 1

            dict["error_messages"] = tmp1
        i = 1
        if len(log_messages) > 0:
            for msg in log_messages:
                tmp2[i] = msg
                i += 1

            dict["log_messages"] = tmp2
        return dict

    return {"add": add, "add_error": add_error, "add_log": add_log, "output": output}
