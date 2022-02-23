##############################
#Import unittest and requests library
##############################
import unittest
import requests

##############################
#Class TestRequest
##############################
class TestRequest(unittest.TestCase):
    #Test for status code
    def test_GetRequest(self):
        #Website input
        website = "http://192.168.182.143/spicyx"

        #Perform 'get' request
        r = requests.get(website)

        #Test for 200 status code
        self.assertEqual(r.status_code, 200)

    def test_Header(self):
        #Website input
        website = "http://192.168.182.143/spicyx"

        #Perform header response from website
        h = requests.head(website)

        #Convert h.headers to string
        Server = str(h.headers)

        #Test for header
        self.assertEqual(Server[53:75], 'Apache/2.4.27 (Ubuntu)')

#####################################
#Main function
#####################################
if __name__ == '__main__':
    unittest.main()