
import sys
import psutil
import shutil

def Main():
    opt = sys.argv[1]
    print_option(opt)

def print_option(opt):
    if (opt == 'd' or opt == 'D'):
        stats = shutil.disk_usage("/")
        print("Disk usage stats:", stats)
    elif(opt == 'c' or opt == 'C'):
        print('The CPU usage is:', psutil.cpu_percent(4))
    elif (opt == 'r' or opt == 'R'):
        print('RAM memory % used:', psutil.virtual_memory()[2])
    else:
        print("Invalid Option")
        exit()


if __name__ == '__main__': Main()



