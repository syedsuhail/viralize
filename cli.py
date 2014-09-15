import ConfigParser
import sys
from getpass import getpass
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



def status(results):
    for key,value in results.iteritems():
        print "==================",key,"==================="
        print "\t",value

def get_value(request):
    value = raw_input('\nEnter your %s :' %request)
    return value

def get_passwd(request):
    value = getpass('\nEnter your %s :' %request)
    return value

def warning(msg,request):
    y = raw_input('%s ' %msg)
    if y == 'no' or y == 'No' or y == 'NO':
        value = raw_input('\nEnter the %s :' %request)
    elif y == 'yes' or y == 'Yes' or y == 'YES':
        value = ''
    else:
        y = 'abcd'
        value = ''
    return y,value
        

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
    results = controller.viralize(data)
    status(results)

