#!/usr/bin/python3

import os, yaml
from core.common_imports import *
from menu.common_imports import *


class NauExtractedConfiguration():
    def __init__(self, captured_pcap_file="start_capture.pcap", port_number=53, protocol_type="udp"):
        self.extracted_configuration_information={'computer_mac_address':'','gateway_mac_address':'','computer_ip_address':'','dns_server':''}
        self.captured_pcap_file="$HOME/.nautools/tmp/"+captured_pcap_file
        self.port_number=port_number
        self.protocol_type=protocol_type.lower()
        try:
            self.host_info=NauConfigRead.ReadNauConfiguration().read_hostinfo_config(host_info_config='config/hostinfo.conf')
        except:
            print("[-] First generate the hostinfo.conf")

    def setup_config_extract_tap(self):
        command_string="tcpdump -i "+self.host_info['computer_interface']+" -s0 -w "+self.captured_pcap_file+" -c1 "+self.protocol_type+" dst port "+str(self.port_number)
        os.system(command_string)
        
    def extract_computer_mac_address(self):
        command_string="tcpdump -r "+self.captured_pcap_file+" -nne -c 1 "+self.protocol_type+" dst port "+str(self.port_number)+" | awk \'{print $2\",\"$4$10}\' | cut -f 1-4 -d.| awk -F \',\' \'{print $1}\'"
        #print(command_string)
        self.extracted_configuration_information['computer_mac_address']=os.popen(command_string).read().strip('\n')

    def extract_gateway_mac_address(self):
        command_string="tcpdump -r "+self.captured_pcap_file+" -nne -c 1 "+self.protocol_type+" dst port "+str(self.port_number)+" | awk \'{print $2\",\"$4$10}\' | cut -f 1-4 -d.| awk -F \',\' \'{print $2}\'"
        #print(command_string)
        self.extracted_configuration_information['gateway_mac_address']=os.popen(command_string).read().strip('\n')

    def extract_computer_ip_address(self):
        command_string="tcpdump -r "+self.captured_pcap_file+" -nne -c 1 "+self.protocol_type+" dst port "+str(self.port_number)+" | awk \'{print $3\",\"$4$10}\' | cut -f 1-4 -d.| awk -F \',\' \'{print $3}\'"
        #print(command_string)
        self.extracted_configuration_information['computer_ip_address']=os.popen(command_string).read().strip('\n')

    def extract_dns_server(self):
        if(self.port_number==53):
            command_string="tcpdump -r "+self.captured_pcap_file+" -nne -c 1 "+self.protocol_type+" dst port "+str(self.port_number)+" | awk \'{print $2\",\"$2$12}\' | cut -f 1-4 -d.| awk -F \',\' \'{print $2}\'"
            #print(command_string)
            self.extracted_info.conf['dns_server'] = os.popen(command_string).read().strip('\n')
        else:
            print("Looks like capturing traffic wasn't done with DNS(port 53)")

    def write_extracted_configuration(self):
        all_values_present=0
        for i in self.extracted_configuration_information.keys():
            if(self.extracted_configuration_information == ''):
                print("[-] We are missing "+i+" option!")
            else:
                all_values_present=all_values_present+1
        if (all_values_present>=3):
            home_dir=os.path.expanduser("~")
            config_path=home_dir+'/.nautools/config/extracted_info.conf'
            print (self.extracted_configuration_information)
            with open(config_path, 'w') as outfile:
                yamDump=yaml.dump(self.extracted_configuration_information)
                print(yamDump)
                outfile.write(yamDump)
                #, default_flow_style=False)
        else:
            print("Configurations has not been extracted. Please set all the options.")


if __name__ == '__main__':
    #x=NauExtractedConfiguration()
    #x.setup_config_extract_tap()
    #x.extract_computer_mac_address()
    #x.extract_gateway_mac_address()
    #x.extract_computer_ip_address()
    #x.extract_dns_server()
    #x.write_extracted_configuration()
    pass
