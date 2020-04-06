class Relay:

    # input values = [horizontal distance (mm) from left edge, plugged].
    # by default nothing is plugged in (0)
    def __init__(self):
    
        self.wet1 = [8,0]
        self.wet2 = [11.5, 0]
        self.in1 = [15 0]

        self.gnd1 = [18, 0]
        self.in2 = [22.5, 0]
        self.gnd2 = [26, 0]
        
        self.in3 = [30, 0]
        self.gnd3 = [33.5, 0]

        self.in4 = [37.5, 0]
        self.gnd4 = [41, 0]

        self.nc1 = [45, 0]
        self.no1 = [48.5, 0]
        self.com1 = [52, 0]

        self.nc2 = [56, 0]
        self.no2 = [59.5, 0]
        self.com2 = [63, 0]

        self.nc3 = [67, 0]
        self.no3 = [70.5, 0]
        self.com3 = [74, 0]

        self.power_12v = [78, 0]
        self.power_24v = [81.5, 0]

    # changes 2nd value in relay input value to 1, meaning it's plugged in
    def plug(self, wire):
        self.inputs[wire][2] = 1

    def connection(self, input, wire):
        self.wires[input] = wire  # This needs to change because of the init
    
    def terminal_thru_wire(self, wire):
        return self.wires[pin].terminal # This also needs to change