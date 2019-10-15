#!/usr/bin/python3

import os, cmd
#from menu.ConfigurationMenu import *
from menu.common_imports import *
from core.common_imports import *
from menu import common_imports
import time

class TapMenu(cmd.Cmd):
    def __init__(self,args=None):
        cmd.Cmd.__init__(self)
        self.prompt='(nau Tap) # '

    def do_begin(self, line):
        """
        Begin network Tap
        :param line: begin <port number> <protocol type>
        """
        usage_msg = "Usage: begin <port number> <protocol type>"
        if(len(line.split(' '))== 2):
            try:
                temp_var = int(line.split(' ')[0])
            except:
                print("[-] " + usage_msg)
            if line.split(' ')[1].lower() in ['tcp','udp']:
                print("[*] Creating TAP Object")
                print("[*] Importing configuration")
                print("[*] Imported host configuration")
                tap_object = NauTap.NauTap()
                print("[*] host configuration")
                host_config = tap_object.get_host_info()
                print("[*] Turning off network service")
                tap_object.turn_off_service('network-manager')
                print("[*] Disabling IPv6")
                print("[*] sysctl -p ")
                tap_object.disable_ipv6_patch()
                print("[*] Renaming hostname")
                tap_object.rename_hostname()
                print("[+] Ground work complete!")
                print("[*] Setting up network bridge")
                tap_object.build_bridge_interface()
                print("[*] Setting up rules to forward EAP packets")
                tap_object.setup_system_patches()
                print("[*] Setting up interfaces in promiscuous mode")
                tap_object.interface_promisc_mode(host_config['computer_interface'],'0.0.0.0')
                tap_object.interface_promisc_mode(host_config['switch_interface'],'0.0.0.0')
                print("[+] Bridge configured successfully")
                print("[*] Setting up MAC Address for bridge interface")
                tap_object.interface_change_mac_address('13:37:13:37:13:37',host_config['bridge_interface'])
                tap_object.interface_change_mac_address(host_config['switch_mac_address'],host_config['bridge_interface'])
                print("[*] Bringing up bridge interface")
                tap_object.interface_promisc_mode(host_config['bridge_interface'],'0.0.0.0')
                print("[+] Plug in the ethernet chords now")
                time.sleep(5)
                print("[*] Resetting connection")
                tap_object.reset_interface(host_config['computer_interface'])
                tap_object.reset_interface(host_config['switch_interface'])
                print("[*] Beginning to extract configuration from the network.")
                network_config_extractor = NauExtractConfig.NauExtractedConfiguration(captured_pcap_file="start_capture.pcap",
                                                                                      port_number=53, protocol_type="udp")
                network_config_extractor.setup_config_extract_tap()
                network_config_extractor.extract_computer_mac_address()
                network_config_extractor.extract_gateway_mac_address()
                network_config_extractor.extract_computer_ip_address()
                try:
                    network_config_extractor.extract_dns_server()
                except:
                    print("[!] Unable to extract DNS server at the current point of time.")
                network_config_extractor.write_extracted_configuration()
                network_config = tap_object.get_extracted_network_info()
                print("[*] Go stealthy")
                tap_object.disable_traffic_flow()
                print("[*] Bringing up bridge interface in promiscuous")
                tap_object.interface_promisc_mode(host_config['bridge_interface'],host_config['bridge_ip_address'])
                print("[*] Creating layer 2 re-write postrouting rules")
                tap_object.ebtables_portrouting(host_config['switch_interface'])
                tap_object.ebtables_portrouting(host_config['bridge_interface'])
                print("[*] Adding default routes")
                tap_object.add_default_route()
                print("[!] Setting up management callbacks. This might not be OpSec safe, and could be detected.")
                tap_object.iptables_prerouting_management_ports()
                print("[*] Creating Layer 3 re-write postrouting rules")
                tap_object.iptables_postrouting('tcp')
                tap_object.iptables_postrouting('udp')
                tap_object.iptables_postrouting('icmp')
                print("[*] Starting management services")
                tap_object.turn_on_service('ssh')
                #check for ttyd
                print("[*] Starting Network Manager")
                try:
                    tap_object.turn_on_service('network-manager')
                except:
                    try:
                        tap_object.turn_on_service('NetworkManager')
                    except:
                        pass
                print("Re-enabling the flow")
                tap_object.enable_traffic_flow()
                print("Resetting DNS server")
                tap_object.set_dns_server()
                print("[+] Setup completed successfully")
                print("[*] Starting the side channel...")
                os.system("ifconfig wlan0 up")
                print("[+] Wireless channel is now up")
                print("[*] Attempting to turn on ttyd")
                try:
                    os.system("./utils/bin/ttyd_server 2121 &")
                    print("[*] TTYd server started on port 2121")
                except:
                    print("[-] Error starting TTYd server")
            else:
                print("[-] " + usage_msg)

    def do_back(self,line):
        """Go back to main menu"""
        common_imports.MainMenuLoop()

    def do_exit(self,line):
        """Exit the program"""
        common_imports.perform_exit()


if __name__ == '__main__':
    TapMenu().cmdloop()
