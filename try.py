__author__ = 'santiago'


import delta_debugging



class Svs_tester:

    def test(self,data):

        aux="antiago"

        if data==aux or aux in data:
            return True
        else:
            return False


svs_tester=Svs_tester()

debu= delta_debugging.delta_debugger("Santiago lkjsff aaa Velez Saffon antiago",svs_tester)



print(debu.start())



