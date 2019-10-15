#!/usr/bin/python3
#import NauConfigRead
import os
from core.common_imports import *

class NauRules():
    def __init__(self):
        try:
            self.host_info = NauConfigRead.ReadNauConfiguration.read_hostinfo_config('config/hostinfo.conf')
            self.extracted_info = NauConfigRead.ReadNauConfiguration.read_extracted_config('config/extracted_info.conf')
        except:
            print("[-] There is an error in reading configuration files")
            pass

    def create_rule(self, protocol_type, port_number):
        try:
            command_string="iptables -t nat -A PREROUTING -i "+self.host_info['bridge_interface']+" -d "+self.extracted_info['computer_ip_address']+" -p "+protocol_type+" --dport "+port_number+" -j DNAT --to "+self.host_info['bridge_ip_address']+":"+port_number
            print(command_string)
            os.system(command_string)
            print("[+] Rule created successfully.")
        except:
            print("[!] An unexpected error occurred while creating the rule")

    def list_rules(self):
        print("\nThe below listed rules are only pre-routing rules\n")
        command_string="iptables -t nat -v -L PREROUTING -n --line-number"
        rule_list=os.popen(command_string).read()
        rule_iterate=rule_list
        print(rule_iterate)
        #for eachRule in rule_iterate:
        #    print(eachRule)

    def delete_rule(self, line_number):
        if(line_number=='all'):
            print("[!] Flushing all rules\n")
            command_string="iptables -F"
        else:
            try:
                test_integer=int(line_number)
                print("[!] Deleting the rule\n")
                command_string="iptables -t nat -D PREROUTING "+line_number
            except:
                print("[-] Line number needs to be an integer")
        os.system(command_string)

if __name__ == '__main__':
    pass
