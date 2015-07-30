__author__ = 'Santiago Velez Saffon'

#All the imports

import argparse

#end of imports


class command_line:


    def __init__(self):
        self.parser=argparse.ArgumentParser(description="This is the command line for delta debugging")

        self.parser.add_argument('--controller', dest='controller',default=False,help='New definitions of tester and divider')

        self.parser.add_argument('--all', dest='all',default=True,help='Store all test cases')

        self.parser.add_argument('--test', dest='test_input',default='test_in.txt',help='file of the test case')

        self.parser.add_argument('--out', dest='test_out',default=False,help='Where the output should go, default will print on console!')

        self.args = self.parser.parse_args()


def main():
    cmd=command_line()

    print(cmd.args)

if __name__ == "__main__": main()
