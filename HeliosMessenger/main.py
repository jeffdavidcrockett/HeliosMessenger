from station import HeliosBridge
import configparser


class FileParser:
    def __init__(self):
        self.c = configparser.ConfigParser()
        self.file_name = 'config.txt'

    def read_config(self):
        self.c.read(self.file_name)

    def config_section_map(self, section):
        config_dict = {}
        options = self.c.options(section)
        for option in options:
            config_dict[option] = self.c.get(section, option)

        return config_dict

    def get_operators(self):
        self.read_config()
        operators = self.config_section_map('SectionOne')['operators']
        return str(operators).split()

    def get_ip_address(self):
        self.read_config()
        return self.config_section_map('SectionTwo')['ip']


def look_for_finished_plc_state():
    while True:
        # read physical RPi input pin, look for True/High state
        # if input pin is True, return True
        break


def check_ip_validity():
    valid_connection = plc_bridge.check_connection()
    if not valid_connection:
        # send digital signal to PLC for connection error,
        # then do something, sit in limbo, I don't know
        pass


def send_to_netsuite():
    pass


def main():
    # Pull operators from config file and set in plc_bridge object
    plc_bridge.set_operators(parser.get_operators())

    # Pull plc ip address from config file and set in plc_bridge object
    plc_bridge.set_ip_address(parser.get_ip_address())

    # Check to make sure ip in config file is correct
    check_ip_validity()

    # look_for_finished_plc_state()
    # Code here

    # Pull the current operator val from plc and set in plc_bridge object
    plc_bridge.set_current_operator()

    # Pull barcode data from plc and set in plc_bridge object
    plc_bridge.set_barcode()

    # Pull test data from plc and set in plc_bridge object
    plc_bridge.set_tag_values()

    # Send data to netsuite
    send_to_netsuite()

    # Backup data in txt file on raspberry pi
    # Code here

    # Clear barcode in plc_bridge object
    plc_bridge.clear_barcode()

    # Clear most recent test data in plc_bridge object
    plc_bridge.clear_tag_values()

    # Clear current operator in plc_bridge object
    plc_bridge.clear_current_operator()

    # Start over
    main()


parser = FileParser()
plc_bridge = HeliosBridge()
main()
