class Terminal:
    
    # x_offset = horizontal difference between relay and terminal
    # y_offset = vertical difference between relay and terminal
    # initial 0 = nothing plugged into terminal
    def __init__(self, x_offset, y_offset):
        self.inputs = {
            "in_1" : [x_offset, y_offset, 0],
            "in_2" : [x_offset + 10, y_offset, 0],
            "in_3" : [x_offset + 20, y_offset, 0],
            "in_4" : [x_offset + 30, y_offset, 0],
            "in_5" : [x_offset + 40, y_offset, 0],
            "in_6" : [x_offset + 50, y_offset, 0],
            "in_7" : [x_offset + 60, y_offset, 0],
            "in_8" : [x_offset + 70, y_offset, 0],
            "in_9" : [x_offset + 80, y_offset, 0],
            "in_10" : [x_offset + 90, y_offset, 0],
            "in_11" : [x_offset + 100, y_offset, 0],
            "in_12" : [x_offset + 110, y_offset, 0]
            }

    def plug(self, wire):
        self.inputs[wire][2] = wire

    def relay_thru_wire(self, wire):
        return self.inputs[wire].relay

    def __str__(self):        
        return self.inputs

    