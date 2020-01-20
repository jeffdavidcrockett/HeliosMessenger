from pycomm.ab_comm.slc import Driver as SlcDriver
import logging
from time import sleep


test_dict = {'B3:4/3': None, 'B3:4/2': None}

c = SlcDriver()
if c.open('192.168.1.20'):
    for key in test_dict.keys():
        test_dict[key] = c.read_tag(key)

print test_dict

# ************************************************************************************************

# stuff = ''
#
# test_list = [1, 2, 3, 4]
#
# for val in test_list:
#     stuff += str(val)
#
# print stuff

# ************************************************************************************************

# from communications import HeliosStation
# import configparser
#
#
# class FileParser:
#     def __init__(self):
#         self.c = configparser.ConfigParser()
#         self.file_name = 'config.txt'
#
#     def read_config(self):
#         self.c.read(self.file_name)
#
#     def config_section_map(self, section):
#         config_dict = {}
#         options = self.c.options(section)
#         for option in options:
#             config_dict[option] = self.c.get(section, option)
#
#         return config_dict
#
#     def get_operators(self):
#         self.read_config()
#         operators = self.config_section_map('SectionOne')['operators']
#         return str(operators).split()
#
#     def get_ip_addresses(self):
#         self.read_config()
#         ips = self.config_section_map('SectionTwo')['ips']
#         return str(ips).split()
#
#
# def create_plc_dict():
#     plc_dict = {}
#     nodes = parser.get_ip_addresses()
#     for node in nodes:
#         plc_dict[node] = HeliosStation
#
#     return plc_dict
#
#
# def create_plc_objects():
#     plcs = []
#     plc_dict = create_plc_dict()
#     for node in plc_dict.keys():
#         plc_instance = plc_dict[node](node)
#         plcs.append(plc_instance)
#
#     return plcs
#
#
# def attach_operators_to_plc(plcs):
#     for plc in plcs:
#         plc.set_operators(parser.get_operators())
#
#
# def main():
#     plcs = create_plc_objects()
#     attach_operators_to_plc(plcs)
#     plcs[0].set_barcode()
#     print plcs[0].barcode
#
#
#
#
#
# parser = FileParser()
# main()
