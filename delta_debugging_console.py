__author__ = 'Santiago Velez Saffon'

#All the imports

import argparse

#end of imports


class command_line:


    def __init__(self):
        self.parser=argparse.ArgumentParser(description="This is the command line for delta debugging")

        self.parser.add_argument('--all', dest='all',default=True,help='Store all variables')

        self.parser.add_argument('--test', dest='test_input.txt',default=False,help='file of the test case')

        self.parser.add_argument('--out', dest='test_input.txt',default=1,help='Where the output should go, default will print on console!')

        args = self.parser.parse_args()
        print(args)


def main():
    cmd=command_line()




if __name__ == "__main__": main()
