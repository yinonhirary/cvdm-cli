from model import cliArgument, hr


def hr_route():
    """"
        candidate route function
    """
    if cliArgument.args.get:  # get candidate card (json file)
        hr.get_candidate_card(cliArgument.args.get)
    elif cliArgument.args.update:  # get candidate card (json file)
        hr.update_candidate_card(cliArgument.args.update)
    elif cliArgument.args.search and cliArgument.args.search_v:
        hr.search(cliArgument.args.search,cliArgument.args.search_v)
