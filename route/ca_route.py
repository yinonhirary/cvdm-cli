from model import cliArgument, candidate


def ca_route():
    """"
        candidate route function
    """
    if cliArgument.args.fimport:  # import json candidate data file option
        candidate.import_json_file(cliArgument.args.fimport)
    elif cliArgument.args.fexport:  # export json candidate file option
        candidate.export_json_file()
    elif cliArgument.args.jsonformat:  # sending empty json file to new candidate option
        candidate.write_json_file(candidate.empty_json_template(), "template")
