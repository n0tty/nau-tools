#!/usr/bin/env python

import os
import core
#from menu import MainMenu
#from menu import *
from core import *
from random import choice
from menu.common_imports import *
#from menu.ConfigurationMenu import *
#from menu import MainMenu
#from menu import ConfigurationMenu



def banner_call_1():
    print("""
 __    __   ______   __    __ 
/  \  /  | /      \ /  |  /  |
$$  \ $$ |/$$$$$$  |$$ |  $$ |
$$$  \$$ |$$ |__$$ |$$ |  $$ |
$$$$  $$ |$$    $$ |$$ |  $$ |
$$ $$ $$ |$$$$$$$$ |$$ |  $$ |
$$ |$$$$ |$$ |  $$ |$$ \__$$ |
$$ | $$$ |$$ |  $$ |$$    $$/ 
$$/   $$/ $$/   $$/  $$$$$$/  

Network    Access   Unlocked
""")


def banner_call_2():
    print("""
ooooo      ooo       .o.       ooooo     ooo 
`888b.     `8'      .888.      `888'     `8' 
 8 `88b.    8      .8"888.      888       8  
 8   `88b.  8     .8' `888.     888       8  
 8     `88b.8    .88   8888.    888       8  
 8       `888   .8'     `888.   `88.    .8'  
o8o        `8  o88ooooooo8888o    `YbodP'    
   Network         Access        Unlocked
""")


def banner_call_3():
    print("""
 .-----------------. .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| | ____  _____  | || |      __      | || | _____  _____ | |
| ||_   \|_   _| | || |     /  \     | || ||_   _||_   _|| |
| |  |   \ | |   | || |    / /\ \    | || |  | |    | |  | |
| |  | |\ \| |   | || |   / ____ \   | || |  | '    ' |  | |
| | _| |_\   |_  | || | _/ /    \ \_ | || |   \ `--' /   | |
| ||_____|\____| | || ||____|  |____|| || |    `.__.'    | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----Network-------' '-----Access------' '----Unlocked----' 
""")

    
def author_information_banner():
    print("""
Author: @TanoyBose

Project Repo: https://github.com/n0tty/nau-tools
Read The Wiki: https://github.cim/n0tty/nau-tools/wiki
""")

def nau_tools():
    os.system("clear")
    a=[banner_call_1,banner_call_2,banner_call_3]
    choice(a)()
    author_information_banner()
    m = MainMenu.MainMenu().cmdloop()
    m.cmdloop()


if __name__ == '__main__':
    #core.NauTap.NauTap().check_if_root()
    nau_tools()
