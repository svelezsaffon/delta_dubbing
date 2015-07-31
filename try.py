__author__ = 'santiago'



import delta_debugging_core



class Svs_tester:

    def test(self,data):

        aux="Jorge"

        if data==aux or aux in data:
            return True
        else:
            return False


svs_tester=Svs_tester()

debu= delta_debugging_core.delta_debugger("Santiago lkjsff aaa Velez Saffon antiago",svs_tester)

debu.all_test=False



print(debu.start())



