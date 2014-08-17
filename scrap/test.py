import ConfigParser
import sys
import json

filename =sys.argv[1]  
config = ConfigParser.ConfigParser()
try:
    config.read(filename)
except IndexError:
    print "enter Filename"
lis = []


def ConfigSectionMap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            if config.get(section,option) == '':
                print "In section %s , %s value is empty"% (section,option)
                exit(1)
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    dict1["channel"]=section
    
    
    return dict1

for section in config.sections():
    lis.append(ConfigSectionMap(section))

print "%s" % lis
