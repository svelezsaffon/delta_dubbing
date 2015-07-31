__author__ = 'Santiago Velez Saffon'

#All the imports

import argparse

#end of imports


class command_line:


    def __init__(self):
        self.parser=argparse.ArgumentParser(description="This is the command line for delta debugging")

        self.parser.add_argument('--controller', dest='controller',required=True,help='New definitions of tester and divider')

        self.args = self.parser.parse_args()


def main():
    cmd=command_line()

    print(cmd.args)

if __name__ == "__main__": main()
