import ConfigParser
import sys
import getpass
from sys import argv
from binascii import hexlify
import viralize
data_file = 'viral.ini'
def get_user_data(filename):
    '''Gets relevant data from ini file and returns a list of dictionaries'''
    config = ConfigParser.ConfigParser()
    data=[]
    try:
        config.read(filename)
    except Exception:
        print "File does not exist"
        return
    for section in config.sections():
        dict1={}
        dict1["channel"]=section
        options = config.options(section)
        for option in options:
            try:
                dict1[option] = config.get(section,option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
                if config.get(section,option) == '':
                    print "In section %s, %s value is empty"%(section,option)
            except:
                print("exception on %s!" %option)
                dict1[option]=None
        data.append(dict1)
    return data


def get_username_pass(service):
    username= hexlify(raw_input('Enter username for %s '%service))
    password = hexlify(getpass.getpass('Password for %s $:'%service))
    return username,password

def status(results):
    for key,value in results.iteritems():
        print key,value

def get_value(request):
    value = raw_input('Enter your %s' %request)
    return value

    

def main():
    data=get_user_data(data_file)
    results = viralize.viralize(data)
    status(results)

if __name__=='__main__':
    try:
        filename = argv[1]
    except Exception:
        print "Needs argument"
        raise
    get_user_data(filename)

            
