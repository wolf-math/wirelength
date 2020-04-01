import length

relay_inputs = {
    "wet1" : 8,
    "wet2" : 11.5,
    "in1" : 15 0,

    "gnd1" : 18,
    "in2" : 22.5,
    "gnd2" : 26,
    
    "in3" : 30,
    "gnd3" : 33.5,

    "in4" : 37.5,
    "gnd4" : 41,

    "nc1" : 45,
    "no1" : 48.5,
    "com1" : 52,

    "nc2" : 56,
    "no2" : 59.5,
    "com2" : 63,

    "nc3" : 67,
    "no3" : 70.5,
    "com3" : 74,

    "power_12v" : 78,
    "power_24v" : 81.5
}

terminal_inputs = {
    "in_1" : x_offset,
    "in_2" : x_offset + 10,
    "in_3" : x_offset + 20,
    "in_4" : x_offset + 30,
    "in_5" : x_offset + 40,
    "in_6" : x_offset + 50,
    "in_7" : x_offset + 60,
    "in_8" : x_offset + 70,
    "in_9" : x_offset + 80,
    "in_10" : x_offset + 90,
    "in_11" : x_offset + 100,
    "in_12" : x_offset + 110
}


y_offset = int(input("vertical offset (mm): "))
x_offset = int(input("horizontal offset (mm): "))
print("which relay input are you using? Select from the following")
relay_selection = int(input("(1) wet1 (2) wet2 (3) in1 (4) gnd1 (5) in2 (6) gnd2 (7) in3 (8) gnd3 (9) in4 (10) gnd4 (11) nc1 (12) no1 (13) com1 (14) nc2 (15) no2 (16) com2 (17) nc3 (18) no3 (19) com3 (20) power 12v (21) power_24v "))
terminal_selection = int(input("which terminal input are you using? "))

relay_x = relay_inputs
length.length()