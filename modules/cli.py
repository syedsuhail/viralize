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
    dict1={}
    for section in config.sections():
        options = config.options(section)
        dict1["section"]=section
        for option in options:
            if config.get(section,option) == '':
                print "In section %s, %s value is empty"%(section,option)
            try:
                dict1[option] = config.get(section,option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                print("exception on %s!" %option)
                dict1[option]=None
            data.append(dict1)
    return data


                         

            
