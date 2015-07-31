__author__ = 'santiago'


import delta_debugging_core



class http_tester:

    def __init__(self,host):
        self.host=host

    def test(self,data):


        import urllib2

        complete =self.host + data

        print complete


        try:

            content = urllib2.urlopen(complete)

            content.read()



            if content.getcode() is 200:
                return True

            return False

        except urllib2.HTTPError as e:
            print e.code
            print e.read()





tester=http_tester("https://maps.googleapis.com/maps/api/staticmap?")

debu= delta_debugging_core.delta_debugger("center=Berkeley&zoom=14&size=412x411x300",tester)

debu.all_test=True

debu.iter_limits=True

debu.iterations=4


print(debu.start())
