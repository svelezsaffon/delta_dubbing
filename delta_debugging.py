__author__ = 'santiago'

#---------------IMPORTS--------------
import delta_debugging_console
import os
#--------------ALL IMPORTS-----------



def include(filename):
    if os.path.exists(filename):
        execfile(filename)

def main():
    cmd=delta_debugging_console.command_line()


    if cmd.args.controller is not False:
        include(cmd.args.controller)
    else:
        print("[WARNING] not including external controller")

        import delta_debugging_core

        file = open(cmd.args.test_input, 'r')

        test_input=file.read()

        file.close()

        debu= delta_debugging_core.delta_debugger(test_input)


        if cmd.args.all is not True:
            debu.all_test=False


        min_cases=debu.start()

        if cmd.args.test_out is not False:

            filew = open(cmd.args.test_out, "w")

            for mcase in min_cases:
                filew.write(mcase)
                filew.write("\n")

            filew.close()

        else:
            print(min_cases)




if __name__ == "__main__": main()