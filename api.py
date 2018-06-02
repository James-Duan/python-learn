import requests
import sys
__author__ = 'DuanZJ'


class Employee:
    pass


class API:
    def __init__(self):
        pass

    @staticmethod
    def url_splice(interface, search):
        base_address = "http://preview.emi-cube.ad.xiaomi.srv/api/"
        address = ""
        if interface != "" and search != "":
            address = base_address + interface + "?" + search
        return address

    @staticmethod
    def request(address):
        result = requests.get(address)
        if result.status_code not in (400, 404, 500, 502):
            return result
        else:
            print "URL Error with : %s" % result.status_code
            sys.exit(0)


if __name__ == '__main__':
    j = Employee()
    interface1 = "getCustomerData"
    search_word = "customerId=54062&sDate=2018-05-01&eDate=2018-05-01"
    r = API.request(API.url_splice(interface1, search_word))
    s = r.json()["result"]["total"]
    for i in s:
        print i + ":" + str(s[i])
