#!/usr/bin/python3

import os, cmd
#from menu.ConfigurationMenu import *
from menu.common_imports import *
from menu import common_imports

class MainMenu(cmd.Cmd):
    def __init__(self,args=None):
        cmd.Cmd.__init__(self)
        self.prompt='(nau) # '

    def do_configure(self, line):
        """Nau Configuration module"""
        ConfigurationMenu.HostConfiguration().cmdloop()

    def do_tap(self, line):
        """Nau Tap module"""
        TapMenu.TapMenu().cmdloop()

    def do_rules(self, line):
        """Nau Rules Module"""
        RulesMenu.RulesMenu().cmdloop()

    def do_inject(self, line):
        """NAU Injection Module"""
        InjectMenu.InjectMenu().cmdloop()


    def do_exit(self,line):
        """Exit the program"""
        common_imports.perform_exit()


if __name__ == '__main__':
    MainMenu().cmdloop()
