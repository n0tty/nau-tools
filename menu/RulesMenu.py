#!/bin/usr/env python3


import os, cmd

from menu.common_imports import *
from core.common_imports import *
from menu import common_imports

class RulesMenu(cmd.Cmd):
    def __init__(self, args=None):
        cmd.Cmd.__init__(self)
        self.prompt='(nau rules) # '
        
    def do_create_rule(self, line):
        """
        Create a rule to perform injection
        :Usage: create_rule <tcp/ udp> <portnumber>
        """
        rules_input = line.split(" ")
        err_msg="[-] Error in input. Usage: set_rule \"protocol type\" \"port number\""
        if (len(rules_input)==2):
            if(rules_input[0].lower() in ['tcp','udp']):
                try:
                    print(rules_input)
                    NauRules.NauRules().create_rule(rules_input[0],rules_input[1])
                except:
                    print(err_msg)
            else:
                print("Protocols can only be \'tcp\' or \'udp\' please")
        else:
            print(err_msg)

    def do_show_rules(self, line):
        """
        Shows all the prerouting rules
        """
        NauRules.NauRules().list_rules()

    def do_delete_rule(self, line):
        """
        Delete one rule or all rules
        :param line: 'line number' in rule or 'all'
        """
        NauRules.NauRules().delete_rule(line)

    def do_back(self, line):
        """
        Go back to main menu
        """
        common_imports.MainMenuLoop()

    def do_exit(self, line):
        """Exit the program"""
        # perform_exit()
        common_imports.perform_exit()

