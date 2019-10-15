#!/usr/bin/python3
from core.common_imports import *
import os, sys

class NauTap():
    def __init__(self):
        try:
            # To test if this works
            self.host_info = NauConfigRead.ReadNauConfiguration().read_hostinfo_config(host_info_config='config/hostinfo.conf')
        except:
            print("[-] Error in reading host configuration files")

    def get_host_info(self):
        return self.host_info

    def get_extracted_network_info(self):
        try:
            self.extracted_info = NauConfigRead.ReadNauConfiguration().read_extracted_config(extracted_info_config='config/extracted_info.conf')
        except:
            print("[-] Some problem with extracting configuration")
        return self.extracted_info

    def check_if_root():
        if not os.geteuid()==0:
            sys.exit('[-] This script must be running as root!')

    def rename_hostname(self):
        host_file=open("/etc/host", "w")
        host_file.write(self.host_info['hostname'])
        host_file.close()
        os.system("hostname "+self.host_info['hostname'])

    def turn_off_service(self, service_name):
        os.system("service "+service_name+" stop")

    def turn_on_service(self, service_name):
        os.system("service "+service_name+" start")

    def turn_off_network_interface(self, interface_name):
        os.system("ifconfig "+interface_name+" down")

    def turn_on_network_interface(self, interface_name):
        os.system("ifconfig "+interface_name+" up")

    def interface_promisc_mode(self, interface_name, ip_address):
        os.system("ifconfig "+interface_name+" "+ip_address+" up promisc")

    def interface_change_mac_address(self, mac_address, interface_name):
        os.system("macchanger -m "+mac_address+" "+interface_name)

    def reset_interface(self, interface_name):
        os.system("mii-tool -r "+interface_name)

    def disable_ipv6_patch(self):
        os.system("echo \"net.ipv6.conf.all.disable_ipv6 = 1\" > /etc/sysctl.conf")
        os.system("sysctl -p")

    def setup_system_patches(self):
        os.system("echo 8 > /sys/class/net/"+self.host_info['bridge_interface']+"/bridge/group_fwd_mask")
        os.system("modprobe br_netfilter")
        #os.system("echo 1 > /proc/sys/net/bridge/bridge-nf-call-iptables")
        print("[*] Applying patch for all bridge traffic to route with IP Tables")
        os.system("sysctl net.bridge.bridge-nf-call-tables=1")

    def add_default_route(self):
        command_string="arp -s -i "+self.host_info['bridge_interface']+" "+self.host_info['bridge_gw_address']+" "+self.extracted_info['gateway_mac_address']
        os.system(command_string)
        command_string="route add default gw "+self.host_info['bridge_gw_address']

    def build_bridge_interface(self):
        os.system("brctl addbr "+self.host_info['bridge_interface'])
        os.system("brctl addif "+self.host_info['bridge_interface']+" "+self.host_info['computer_interface'])
        os.system("brctl addif "+self.host_info['bridge_interface']+" "+self.host_info['switch_interface'])

    def iptables_prerouting_management_ports(self):
        # SSH
        command_string="iptables -t nat -A PREROUTING -i "+self.host_info['bridge_interface']+" -d "+self.extracted_info['computer_ip_address']+" -p tcp --dport "+str(self.host_info['ssh_callback_port'])+" -j DNAT --to "+self.host_info['bridge_ip_address']+":22"
        os.system(command_string)
        # TTYd
        command_string="iptables -t nat -A PREROUTING -i "+self.host_info['bridge_interface']+" -d "+self.extracted_info['computer_ip_address']+" -p tcp --dport "+str(self.host_info['ttyd_callback_port'])+" -j DNAT --to "+self.host_info['bridge_ip_address']+":8053"
        os.system(command_string)

    def ebtables_portrouting(self,interface_name):
        command_string="ebtables -t nat -A POSTROUTING -s "+self.host_info['switch_mac_address']+" -o "+interface_name+" -j snat --to-src "+self.extracted_info['computer_mac_address']
        print(command_string)
        os.system(command_string)

    def iptables_postrouting(self, protocol_name):
        if(protocol_name=='icmp'):
            command_string="iptables -t nat -A POSTROUTING -o "+self.host_info['bridge_interface']+" -s "+self.host_info['bridge_ip_address']+" -p "+protocol_name+" -j SNAT --to "+self.extracted_info['computer_ip_address']
            print(command_string)
            os.system(command_string)
        else:
            command_string="iptables -t nat -A POSTROUTING -o "+self.host_info['bridge_interface']+" -s "+self.host_info['bridge_ip_address']+" -p "+protocol_name+" -j SNAT --to "+self.extracted_info['computer_ip_address']+":"+str(self.host_info['min_nat_range'])+"-"+str(self.host_info['max_nat_range'])
            print(command_string)
            os.system(command_string)

    def disable_traffic_flow(self):
        os.system("arptables -A OUTPUT -j DROP")
        os.system("iptables -A OUTPUT -j DROP")

    def enable_traffic_flow(self):
        os.system("arptables -D OUTPUT -j DROP")
        os.system("iptables -D OUTPUT -j DROP")

    def set_dns_server(self):
        os.system("echo nameserver "+self.extracted_info['dns_server']+" > /etc/resolv.conf")


if __name__ == '__main__':
    NauTap().check_if_root()
