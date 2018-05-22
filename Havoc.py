import platform,subprocess,sys,os
import WindowsFun
def main():
    Platform = platform.system()
    currentPath = sys.argv[0]
    if(Platform == 'Windows'):
        WindowsFun.burrow(currentPath)



if __name__ == '__main__':
    main()

