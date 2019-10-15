#!/bin/usr/env python3
#!/usr/bin/python3

import os, cmd
from menu.common_imports import *
from core.common_imports import *
from menu import common_imports

class InjectMenu(cmd.Cmd):
    def __init__(self, args=None):
        cmd.Cmd.__init__(self)
        self.prompt='(nau-inject) # '

    def do_inject_protocol(self, line):
        """Usage inject_protocol <protocol type>"""
        #if(line.lower() == 'rdp' or line.lower() == 'smb' or line.lower() == 'responder' or line.lower() == 'crackmapexec' or line.lower() == 'tomcat'):
        #    NauInject.UtilityInteractionModule.use_module(line)
        #else:
        #    print("[-] We can only inject preset protocols - rdp, smb, responder, tomcat(port 8080)")
        
        try:
            injector = NauInject.UtilityInteractionModule(module_name=line)
            injector.use_module()
            print("[+] Success in injecting "+line+" rule.")
        except:
            print("[-] We can only inject preset protocols - rdp, smb, crackmapexec, responder, msf(reverse tcp on port 8080)")

    def do_inject_sshpivot(self, line):
        """Usage: inject_sshpivot lport rhost rport username password attacker_ip"""
        input_val=line.split(" ")
        if (len(input_val) == 6):
            try:
                command_string="sshpass -p \'"+input_val[4]+"\' ssh -L "+input_val[0]+":"+input_val[1]+":"+input_val[2]+" "+input_val[3]+"@"+input_val[5]
                print(command_string)
                print("[*] Adding pivot. You can now attack the system on localhost:"+input_val[0])
                os.system(command_string)
            except:
                print("[-] Some error occured")
        else:
            print("[-] Usage Error. Please use inject_sshpivot lport rhost rport username password")

    def do_back(self,line):
        """Go back to the main menu"""
        common_imports.MainMenuLoop()

    def do_exit(self,line):
        """Exit the program"""
        common_imports.perform_exit()


if __name__ == '__main__':
    InjectMenu().cmdloop()
