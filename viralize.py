import glob
from os.path import basename, splitext
import importlib

channels_dir='channels/'

def get_channels(channels_dir):
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
        #plugin = module.__plugin__(parser)
        #plugins[module.__cname__] = plugin


def viralize(data):
    channels = get_channels(channels_dir)
    success={}
    for channel in channels:
        name=channel.__name__.split('.')[1].split('_')[0]
        for d in data:
            if d['channel'].lower() == name:
                print 'doing %s' %name
                try:
                    res=getattr(channel,'publish')(d)
                    success[name]= res
                except Exception:
                    print 'couldnt'
                    continue
    return success


if __name__=='__main__':
    viralize()
