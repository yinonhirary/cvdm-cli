from model import cliArgument
from route import main_route


def driver():
    cliArgument.arg_command()
    main_route.default_route()


if __name__ == "__main__":
    driver()
