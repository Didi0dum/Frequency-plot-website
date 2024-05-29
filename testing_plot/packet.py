class Packet:
    def __init__(self, arg_header, arg_data, arg_tail, arg_device_number):
        self.header = arg_header
        self.data = arg_data
        self.tail = arg_tail
        self.device_number = arg_device_number
    
    def validate_packet(self):
        valid = True
        if(self.header[0:4] != b'\xff\xf0\xaaU'):
            valid = False
        if(int(self.header[4]) != self.device_number):
            valid = False
        return valid