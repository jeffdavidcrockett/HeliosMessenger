from pycomm.ab_comm.slc import Driver as SlcDriver


class HeliosBridge:
    def __init__(self):
        self.cur = SlcDriver()

        self.ip_address = None
        self.operators = None
        self.barcode = ''
        self.status_from_plc = 'B3:4/13'
        self.ready_status_to_plc = 'B3:4/14'
        self.current_operator_tag = 'N7:0'
        self.current_operator_str = None

        self.tag_dict = {'B3:4/10': None, 'B3:4/11': None, 'B3:4/2': None, 'B3:4/3': None,
                         'B3:4/4': None, 'B3:4/5': None, 'B3:4/6': None, 'B3:4/7': None,
                         'B3:4/8': None, 'B3:4/9': None, 'B3:4/0': None, 'B3:4/1': None,
                         'F8:5': None, 'F8:6': None, 'F8:7': None, 'F8:8': None,
                         'F8:9': None, 'F8:10': None, 'F8:11': None, 'F8:12': None,
                         'F8:13': None, 'F8:14': None, 'F8:15': None, 'F8:16': None,
                         'F8:17': None, 'F8:18': None, 'F8:19': None, 'F8:20': None,
                         'F8:21': None, 'F8:22': None}

        self.barcode_words = ['B11:0', 'B11:1', 'B11:2', 'B11:3', 'B11:4', 'B11:5',
                              'B11:6', 'B11:7', 'B11:8', 'B11:9']

    def _open_connection(self):
        self.cur.open(self.ip_address)

    def _close_connection(self):
        self.cur.close()

    # Delete this
    def read_test(self):
        return self.cur.read_tag('B3:0/0')

    def check_connection(self):
        try:
            if self.cur.open(self.ip_address):
                connection_state = True
                self.cur.close()
                return connection_state
        except Exception as e:
            return False

    def set_ip_address(self, ip):
        self.ip_address = ip

    def get_ip_address(self):
        return self.ip_address

    def set_operators(self, operators):
        self.operators = operators

    def get_operators(self):
        return self.operators

    def set_current_operator(self):
        self._open_connection()
        operator_int = self.cur.read_tag(self.current_operator_tag)
        self._close_connection()

        if operator_int == 0:
            self.current_operator_str = 'None'
        else:
            self.current_operator_str = self.operators[operator_int-1]

    def get_current_operator(self):
        return self.current_operator_str

    def clear_current_operator(self):
        self.current_operator_str = None

    def get_plc_test_status(self):
        return self.cur.read_tag(self.status_from_plc)

    def set_plc_ready_status(self):
        self.cur.write_tag(self.ready_status_to_plc, 1)

    def set_tag_values(self):
        self._open_connection()
        for key in self.tag_dict.keys():
            self.tag_dict[key] = self.cur.read_tag(key)
        self._close_connection()

    def get_tag_values(self):
        return self.tag_dict

    def clear_tag_values(self):
        self.tag_dict = {'B3:4/10': None, 'B3:4/11': None, 'B3:4/2': None, 'B3:4/3': None,
                         'B3:4/4': None, 'B3:4/5': None, 'B3:4/6': None, 'B3:4/7': None,
                         'B3:4/8': None, 'B3:4/9': None, 'B3:4/0': None, 'B3:4/1': None,
                         'F8:5': None, 'F8:6': None, 'F8:7': None, 'F8:8': None,
                         'F8:9': None, 'F8:10': None, 'F8:11': None, 'F8:12': None,
                         'F8:13': None, 'F8:14': None, 'F8:15': None, 'F8:16': None,
                         'F8:17': None, 'F8:18': None, 'F8:19': None, 'F8:20': None,
                         'F8:21': None, 'F8:22': None}

    def set_barcode(self):
        self._open_connection()
        for word in self.barcode_words:
            self.barcode += str(self.cur.read_tag(word))
        self._close_connection()

    def get_barcode(self):
        return self.barcode

    def clear_barcode(self):
        self.barcode = ''



