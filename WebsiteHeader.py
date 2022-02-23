#################################
#Import Requests Library
#################################
import requests

#################################
#Class WebsiteHeader
#Perform 'get' request and display website header
#################################
class WebsiteHeader:
    def __init__(self):
        #Call function to perform 'get' request
        GetRequest()
        #Call function to display website header
        Header()

################################
#Function GetRequest
#Perform 'get' request on given website
################################
def GetRequest():
    #perform 'get' request
    r = requests.get(website, headers=useragent)

    #Display return status
    print("Status code:")
    print("\t *", r.status_code)

    if r.status_code == 200:
        print('Status Code: OK')
    else:
        print('ERROR')

################################
#Function Header
#Display Header
################################
def Header():
    #Perform header response from website
    h = requests.head(website, headers=useragent)

    #Display website header
    print("Header:")
    print("############")

    #Loop response to display output line by line
    for x in h.headers:
        print("\t",x,":",h.headers[x])
    print('############')

###############################
#Main function
###############################

if __name__ == '__main__':

    #Modify User Agent
    useragent = {
        'User-Agent':'Mobile'
    }

    #Define website to retrieve data
    website = "http://192.168.182.143/spicyx"

    #Call function GetRequest
    GetRequest()

    #Call function Header
    Header()