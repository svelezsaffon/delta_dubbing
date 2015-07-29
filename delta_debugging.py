__author__ = 'Santiago Velez Saffon'


import Queue
import threading



class default_tester:

    def test(self,data):

        aux="ff aaa"

        if data==aux or aux in data:
            return True
        else:
            return False


class default_divider:


    def divide(self,data,granularity):

        chunk=len(data)/granularity + 1;

        answer=[data[i:i+chunk] for i in range(0, len(data), chunk)]

        return answer

    def paste(self,set,remove):
        value=""

        for a in range(0,len(set)):
            if a!=remove:
                value+=set[a]


        return value



class Case:

    def __init__(self):
        self.data=""
        self.granularity=0

    def set_test(self,tests):
        self.data=tests

    def set_granularity(self,gran):

        self.granularity=gran




class delta_debugger:



    def __init__(self,initial_input,tester=default_tester(),divider=default_divider()):

        #This queue will handle the next input for the algorithm
        self.next_input=[]

        #This name will have the innitial input test case
        self.initial_input=initial_input

        #This set will hold all the failed test inputs
        self.min_sets=set()

        #This Queue will hold the next inputs that make the test faill.
        self.failed_input=[]

        #This counter will count how many iterations have been made
        self.iterations=0

        #This is the files used for the output
        self.output=""

        #This is the default tester, the user can provide a tester class
        self.tester=tester

        #This is a divider class, the user would be able to provide a diverder clas, in cass he want to make
        #a more suitable divider
        self.divider=divider


    def _print__(self,data):
        print(data)



    def start(self):

        if not self.tester.test(self.initial_input):

            self._print__("The input does not fail, initially. terminating search!")

            return False

        else:

            case=Case()

            case.set_granularity(2)

            case.set_test(self.initial_input)

            self._minimize_(case,2)

    def _minimize_(self,cxam,gran):

        out=False

        cases=[]
        cases.append(cxam)

        while len(cases)>0 and not out :

            cxa=cases.pop()

            cx=self.divider.divide(cxa.data,cxa.granularity)

            passing=[]


            for test_aux in cx:

                if self.tester.test(test_aux):
                    passing.append(test_aux)



            if len(passing) == 0:
                #Test didnt pass, So we need to increase granularity or stop the process

                #first we need to check the complements

                passing_com=[]


                for sub_case in range(0,len(cx)):
                    aux_case=self.divider.paste(cx,sub_case)

                    if self.tester.test(aux_case):
                        passing_com.append(aux_case)



                if len(passing_com) == 0:

                    if cxa.granularity < len(cxa.data):

                        cxa.set_granularity(min(len(cxa.data),2*cxa.granularity))

                        cases.append(cxa)

                    else:
                        out=True
                else:

                    for pas_com in passing_com:

                        new_case=Case()
                        new_case.data=pas_com
                        new_case.granularity=cxa.granularity

                        cases.append(new_case)

                    self._print__("--------------passing complements------------")
                    self._print__(passing_com)
                    self._print__("---------------------------------------------")

            else:

                self._print__("--------------passing initially--------------")
                self._print__(passing)
                self._print__("---------------------------------------------")














































