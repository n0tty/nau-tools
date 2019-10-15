#!/usr/bin/env python3
from core.common_imports import *

class SideChannelInjection:
    def __init__(self):
        pass

    def forward_port_to_attack(self, local_port, remote_port, remote_ip):
        pass


class UtilityInteractionModule:
    def __init__(self, module_name=''):
        self.module_name = module_name.lower()

    def use_module(self):
        if(self.module_name == 'rdp'):
            NauToolsRules.RdpRules
        elif(self.module_name == 'responder'):
            NauToolsRules.ResponderRules
        elif(self.module_name == 'crackmapexec' or self.module_name == 'smb'):
            NauToolsRules.CrackMapExecRules
        elif(self.module_name == 'msf'):
            NauToolsRules.TomcatRules
        else:
            print("[-] There seems to be no module present for this rule\n")


if __name__ == '__main__':
    pass

