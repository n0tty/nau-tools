#!/usr/bin/python3
from core.common_imports import *


class ResponderRules:
    def __init__(self):
        self.tcp_ports=['137','5355','5353','445','80','443','88','138']
        self.udp_ports=[]

    def create_responder_rules(self):
        for port_number in self.tcp_ports:
            new_rule = NauRules.NauRules()
            new_rule.create_rule('tcp',port_number)

class RdpRules:
    def __init__(self):
        self.tcp_ports=['3389']
        self.udp_ports=[]

    def create_rdp_rules(self):
        for port_number in self.tcp_ports:
            new_rule=NauRules.NauRules()
            new_rule.create_rule('tcp',port_number)



class TomcatRules:
    def __init__(self):
        """ This will only open port for default tomcat configuration port"""
        self.tcp_ports=['8080']
        self.udp_ports=[]

    def create_tomcat_rule(self):
        for port_number in self.tcp_ports:
            new_rule = NauRules.NauRules()
            new_rule.create_rule('tcp', port_number)



class CrackMapExecRules:
    def __init__(self):
        self.tcp_ports=['445']
        self.udp_ports=[]

    def create_crack_map_exec_rules(self):
        for port_number in self.tcp_ports:
            new_rule=NauRules.NauRules()
            new_rule.create_rule('tcp',port_number)
