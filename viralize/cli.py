import ConfigParser
import sys

#filename = sys.argv[1]
#filename='../scrap/viral.ini'

def get_user_data(filename):
    '''Gets relevant data from ini file and returns a list of dictionaries'''
    config = ConfigParser.ConfigParser()
    data=[]
    try:
        config.read(filename)
    except:
        print "File does not exist"
    for section in config.sections():
        dict1={}
        dict1["channel"]=section
        options = config.options(section)
        print dict1['channel']
        for option in options:
            try:
                print config.get(section,option)
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




            
