import glob
from os.path import basename, splitext
import importlib
import cli
 
channels_dir='channels/'

def get_channels(channels_dir):
    '''Given a channel directory the function scans the directory and returns a list of channels'''
    channels={}
    chan=[]
    channel_files = glob.glob("{}/*.py".format(channels_dir))
    for channel_file in channel_files:
        if channel_file.endswith("__init__.py"):
            continue
        name, ext = splitext(basename(channel_file))
        module_name = "channels.{}".format(name)
        module = importlib.import_module(module_name)
        chan.append(module)
    return chan
        

def viralize(data):
    '''The data is sent to appropriate channels where data is a list of dictionaries'''
    channels = get_channels(channels_dir)
    success={}
    for channel in channels:
        name=channel.__name__.split('.')[1].split('_')[0]
        for d in data:
            if d['channel'].lower() == name:
                res = channel.publish(d)
                success[name] = res
    return success

def get_data(request):
    '''Get value from user from command line.Returnts the value'''
    value = cli.get_value(request)
    return value

def get_password(request):
    '''pass password request to command line'''
    value = cli.get_passwd(request)
    return value

def warning(msg,request):
    y,value = cli.warning(msg,request)
    return y,value
    
