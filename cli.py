import ConfigParser
import sys
import getpass
from sys import argv
import controller

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
                print "\nIn section %s, %s value is empty"%(section,option)
            
        data.append(dict1)
    return data

def status(results,key):
    print "\033[1;32m==================",key,"=========================\033[1;m"
    print "Status : ",results


def get_value(request):
    value = raw_input('\nEnter your %s :' %request)
    return value

def get_passwd(request):
    value = getpass.getpass('\nEnter your %s :' %request)
    return value
        

def main():
    data = get_user_data(data_file)
    results = controller.viralize(data)
    status(results)

if __name__=='__main__':
    try:
        filename = argv[1]
    except Exception:
        print "Needs argument"
        raise
    data = get_user_data(filename)
    abc = controller.viralize(data)
    

