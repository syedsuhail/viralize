import ConfigParser
import sys
from configobj import ConfigObj
from getpass import getpass
from sys import argv
from binascii import hexlify
import controller
data_file = 'viral.ini'
import viralize

def get_user_data(filename):
    '''Gets relevant data from ini file and returns a list of dictionaries'''
    config = ConfigParser.ConfigParser()
    data=[]
    config.read(filename)
    for section in config.sections():
        dict1={}
        dict1["channel"]=section
        options = config.options(section)
        for option in options:
            dict1[option] = config.get(section,option)
            if dict1[option] == -1:
                print("skip: %s" % option)
            if config.get(section,option) == '':
                print "In section %s, %s value is empty"%(section,option)
            
        data.append(dict1)
    return data



def status(results):
    for key,value in results.iteritems():
        print key,value

def get_value(request):
    value = raw_input('Enter your %s :' %request)
    return value

def get_passwd(request):
    value = getpass('Enter your %s :' %request)
    return hexlify(value)

def warning(msg,request):
    y = raw_input('%s ' %msg)
    if y == 'no' or y == 'No' or y == 'NO':
        value = raw_input('Enter the %s :' %request)
    elif y == 'yes' or y == 'Yes' or y == 'YES':
        value = ''
    else:
        y = 'abcd'
        value = ''
    return y,value
        


if __name__=='__main__':
    try:
        filename = argv[1]
    except Exception:
        print "Needs argument"
        raise
    data = get_user_data(filename)
    results = viralize.viralize(data)
    status(results)

