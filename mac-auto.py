# created by // plague
#-*- coding: utf-8 -*-

import os

class cols:
    r = '\033[1;31m'
    g = '\033[1;32m'
    c = '\033[1;36m'

def main():
    # banner
    print(cols.c + '''
    
    ╭━╮╭━┳━━━┳━━━╮╱╱╭━━━┳╮╱╭┳━━━━┳━━━╮
    ┃┃╰╯┃┃╭━╮┃╭━╮┃╱╱┃╭━╮┃┃╱┃┃╭╮╭╮┃╭━╮┃
    ┃╭╮╭╮┃┃╱┃┃┃╱╰╯╱╱┃┃╱┃┃┃╱┃┣╯┃┃╰┫┃╱┃┃
    ┃┃┃┃┃┃╰━╯┃┃╱╭┳━━┫╰━╯┃┃╱┃┃╱┃┃╱┃┃╱┃┃
    ┃┃┃┃┃┃╭━╮┃╰━╯┣━━┫╭━╮┃╰━╯┃╱┃┃╱┃╰━╯┃
    ╰╯╰╯╰┻╯╱╰┻━━━╯╱╱╰╯╱╰┻━━━╯╱╰╯╱╰━━━╯
    +- - - - - - - - - - - - - - - - +
    ''')
    
    print(cols.c + "- - - - - - - - - - - - - - - - - - - - - - - - - -")
    print(cols.c + " "                                                  )
    print(cols.c + "Options:"                                           )
    print(cols.c + "s --show         prints current MAC"                )
    print(cols.c + "a --another	Set random vendor MAC of the same kind" )
    print(cols.c + "A 		set random vendor MAC of any kind"          )
    print(cols.c + "p --permenant	restore MAC to default"             )
    print(cols.c + "r --random	set fully random MAC"                   )
    print(cols.c + " "                                                  )
    print(cols.c + "- - - - - - - - - - - - - - - - - - - - - - - - - -")


    networkInterface = input(cols.g + '\nWhat is your Network Interface called? (eth0 ens33 ens32 wlan0): ')
    
    # macchanger commands

    option = input(cols.g + 'What option would you like to choose? (letter only {letters are case sensitive}): ')
    
    if option == 's':
        print(cols.c + 'Showing MAC address')
        os.system('macchanger -s ' + networkInterface)
    
    elif option == 'a':
        print('Setting random vendor of same type')
        os.system('sudo ifconfig ' + networkInterface + ' down')
        os.system('macchanger -a ' + networkInterface)
        print(cols.c + 'Showing MAC address')
        os.system('macchanger -s ' + networkInterface)
        print(cols.g + "\nBringing back up Network Interface!\n")
        os.system("ifconfig " + networkInterface + " up")
    
    elif option == 'A':
        print('Setting random vendor of any type')
        os.system('sudo ifconfig ' + networkInterface + ' down')
        os.system('macchanger -A ' + networkInterface)
        print(cols.c + 'Showing MAC address')
        os.system('macchanger -s ' + networkInterface)
        print(cols.g + "\nBringing back up Network Interface!\n")
        os.system("ifconfig " + networkInterface + " up")
    
    elif option == 'r':
        print('Setting a random MAC address')
        os.system('sudo ifconfig ' + networkInterface + ' down')
        os.system('macchanger -r ' + networkInterface)
        print(cols.c + 'Showing MAC address')
        os.system('macchanger -s ' + networkInterface)
        print(cols.g + "\nBringing back up Network Interface!\n")
        os.system("ifconfig " + networkInterface + " up")

    elif option == 'p':
        print('Resetting MAC address to default!')
        os.system('sudo ifconfig ' + networkInterface + ' down')
        os.system('macchanger -p ' + networkInterface)
        print(cols.c + 'Showing MAC address')
        os.system('macchanger -s ' + networkInterface)
        print(cols.g + "\nBringing back up Network Interface!\n")
        os.system("ifconfig " + networkInterface + " up")

    else:
        print(cols.r + '\n[!] Wrong key pressed! Please re-run this program and check info is correct!\n')

main()
