#!/usr/bin/python3

import yaml

class ReadNauConfiguration():
    def __init__(self):
        pass

    def read_hostinfo_config(self, host_info_config='config/hostinfo.conf'):
        print("Reading: "+host_info_config)
        with open(host_info_config,"r") as stream:
            try:
                host_info=yaml.safe_load(stream)
                return host_info
            except yaml.YAMLError as exc:
                print(exc)

    def read_extracted_config(self, extracted_info_config='config/extracted_info.conf'):
        print("Reading: "+extracted_info_config)
        with open(extracted_info_config,"r") as stream:
            try:
                extracted_info=yaml.safe_load(stream)
                return extracted_info
            except yaml.YAMLError as exc:
                print(exc)

if __name__ == '__main__':
    h=ReadNauConfiguration()
    x=ReadNauConfiguration().read_hostinfo_config(host_info_config="config/hostinfo.conf")
    print(x)
    y=ReadNauConfiguration().read_extracted_config(extracted_info_config="config/extracted_info.conf")
    print(y)
