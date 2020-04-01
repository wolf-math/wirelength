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

relays = ["wet1", "wet2", "in1", "gnd1", "in2", "gnd2", "in3", "gnd3", "in4", "gnd4", "nc1", "no1", "com1", "nc2", "no2", "com2", "nc3", "no3", "com3", "power 12v", "power_24v"]

y_offset = int(input("vertical offset (mm): "))
x_offset = int(input("horizontal offset (mm): "))
print("which relay input are you using? Type one of the following")
relay_selection = int(input(relays))
while relay_selction not in relays:
    relay_selection = input("That's not one of the options, try again: ")
terminal_selection = int(input("which terminal input are you using? (counting left to right) "))

relay_x = 

length.length()