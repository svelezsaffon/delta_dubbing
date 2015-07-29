__author__ = 'Santiago Velez Saffon'


import Queue

class delta_debugger:



    def __init__(self,initial_input):

        #This queue will handle the next input for the algorithm
        self.next_input=Queue()

        #This name will have the innitial input test case
        self.initial_input=initial_input


        