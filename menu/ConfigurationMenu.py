#!/usr/bin/python3

import cmd
import yaml
import os
from menu.common_imports import *
#from MainMenu import *

class HostConfiguration(cmd.Cmd):
    def __init__(self, args=None):
        cmd.Cmd.__init__(self)
        self.prompt='(nau_config) # '
        self.configuration_options = { 'hostname':'', 'switch_interface':'', 'switch_mac_address':'', 'computer_interface':'', 'bridge_interface':'', 'bridge_ip_address':'169.254.13.37', 'bridge_gw_address':'169.254.13.1', 'ssh_callback_port':2222, 'ttyd_callback_port':3333, 'min_nat_range':61000, 'max_nat_range':62000 }

    def switch_interface_mac_address(self):
        """
        Set the MAC address of the switch interface
        """
        if (self.configurations_options['switch_interface'] != ''):
            self.configuration_options['switch_mac_address'] = os.popen("ifconfig "+self.configuration_options['switch_interface']+" | grep -i ether | awk \'{ print $2 }\'").read()
        else:
            print("seems like switch interface has not yet been set")

    def do_set_hostname(self, text):
        """
        Set the hostname of the raspberry pi
        """
        self.configuration_options['hostname']=text

    def do_set_switch_interface(self, text):
        """
        Set the interface that is to be used to connect to the switch. This will auto retrieve the switch interface mac address
        """
        self.configuration_options['switch_interface'] = text
        try:
            if (self.configurations_options['switch_interface'] != ''):
                self.configuration_options['switch_mac_address'] = os.popen("ifconfig "+self.configuration_options['switch_interface']+" | grep -i ether | awk \'{ print $2 }\'").read()
            else:
                print("seems like switch interface has not yet been set")
        except:
            print("Could not get get switch_mac_address, make sure to manually set it")

    def do_set_switch_mac_address(self, text):
        """
        Set MAC address of the switch interface
        """
        self.configuration_options['switch_mac_address']=text

    def do_set_computer_interface(self, text):
        """
        Set the interface that is to be used to connect to the computer
        """
        self.configuration_options['computer_interface']=text

    def do_set_bridge_interface(self, text):
        """
        Set the interface name of the bridge
        """
        self.configuration_options['bridge_interface'] = text

    def do_set_bridge_ip(self, text):
        """
        Set IP address of bridge. default=169.254.13.37
        """
        self.configuration_options['bridge_ip_address'] = text

    def do_set_bridge_gw_address(self, text):
        """
        Set bridge gateway address
        """
        self.configuration_options['bridge_gw_address'] = text

    def do_set_ssh_callback_port(self, text):
        """
        Set the interface for callback port. Default= 2222
        """
        self.configuration_options['ssh_callback_port'] = int(text)

    def do_set_ttyd_callback_port(self, text):
        """
        Set the interface for callback port. Default= 2222
        """
        self.configuration_options['ttyd_callback_port'] = int(text)

    def do_set_min_nat_range(self, text):
        """
        Min NAT. Default 61000
        """
        self.configuration_options['min_nat_range'] = int(text)

    def do_set_max_nat_range(self, text):
        """
        Max NAT. Default 62000
        """
        self.configuration_options['max_nat_range'] = int(text)

    def do_generate_host_info_config(self, config_list):
        """
        This will generate your yaml configuration for NAU
        """
        all_values_present=0
        for i in self.configuration_options.keys():
            if(self.configuration_options[i]==''):
                print("[-] We are missing "+i+" option!")
            else:
                all_values_present=all_values_present+1
        if (all_values_present == 11):
            home_dir=os.path.expanduser("~")
            #config_path=home_dir+'/.nautools/config/hostinfo.conf'
            config_path='config/hostinfo.conf'
            with open(config_path, 'w') as outfile:
                yaml.dump(self.configuration_options, outfile, default_flow_style=False)
        else:
            print("Configuration file has not been generated. Please set all the options.")

    def do_exit(self, arg):
        """
        Simply exit the prompt
        """
        exit(0)

    def do_back(self, text):
        """Go back to main menu"""
        MainMenu.MainMenu().cmdloop()



if __name__ == '__main__':
    #HostConfiguration().cmdloop()
    pass
