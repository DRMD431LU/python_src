import os, configparser
#Check if .pyscholar exists and create it if necessary
chmod(0777)
pyscholarDir = os.path.join(os.path.expanduser("~user"), "pyscholar")
if not os.path.exists(pyscholarDir):
    os.makedirs(pyscholarDir)

#Same for .pyscholar/keys.cfg
if not os.path.exists(os.path.join(pyscholarDir, "keys.cfg")):
    keysParser = configparser.configparser()
    keysParser.add_section("Keys")
    keysParser.set('Keys', 'Scopus', "")
    originalMask = os.umask(0)
    keysDescriptor = os.open(os.path.join(pyscholarDir,"keys.cfg"),os.O_WRONLY | os.O_CREAT)
    keysFile = os.fdopen(keysDescriptor, 'w')
    os.umask(originalMask)
    keysParser.write(keysFile)
    keysFile.close()

#import scopus
#import network