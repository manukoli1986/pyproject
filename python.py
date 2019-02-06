import urllib.request
import time, ssl
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)
local = 1

def check_url(URL):
    for i in URL:
        try:
            time1 = time.time()
            response = urllib.request.urlopen(i)
            code = response.getcode()
            time2 = time.time()
            final = (time2 - time1)
            print(i + " : " + str(code) + " And {0} time took".format(final))
            ssl._create_default_https_context = ssl._create_unverified_context

        except Exception as e:
            print(i + " : " + str(e))

URL1 = ['https://abc.com/dashboard.json','https://abc:8080/testurl','https://abc.com/login.action']





print("############################ Application IP ###############################")
print(check_url(URL1))

print("############################ Build Tools ###################################")
print(check_url(URL2))


