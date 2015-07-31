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
        print ("[ERROR]This tool needs an external controller, please refer to manual.");




if __name__ == "__main__": main()