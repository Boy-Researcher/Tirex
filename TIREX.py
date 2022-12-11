from colorama import init, Fore
import pyfiglet
import random
import os
init()
lower ='qwertyuiopasdfghjklzxcvbnm'
upper ='QWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '1234567890'
symbols = '[]{};:/\,._-+=)(*&^%$#@!'
all = lower+upper+numbers+symbols
os.system('pip install colorama')
print(Fore.GREEN+'\t    Password', Fore.WHITE+'List Making VPS', Fore.RED+'Random')
print(Fore.GREEN+pyfiglet.figlet_format('T I R E X'))
print(Fore.GREEN+'\t     Irani', Fore.WHITE+' Version', Fore.RED+' 1.0.0' )
xlarj = input('Enter passlist Name and .txt: ')
algoritm = input(Fore.BLUE+'Enter y / n or \help => ')
algoritm = algoritm.upper()
alex = random.randint(1, 10000)
if algoritm == 'Y':
    vmey = int(input('Enter number'))
    f = open(xlarj, '+a')
    while True:
        pasord = ''.join(random.sample(all, vmey))
        print(pasord)
        f.write(pasord + '\n')

    
    print ("\033[1;35m  Password List Maked in 'Password_List.lst' \033[1;m"+'\n')
if algoritm == 'N':
    print('Good Bay')
if algoritm == '\HELP':
    print('y > Next')
    print('n > Close')