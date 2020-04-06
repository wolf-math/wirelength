class Connection:
    def __init__(self, length, relay, relay_pin, terminal, terminal_pin):
        self.length = length
        self.relay = relay
        relay.connect_wire(relay_pin, self)
        self.terminal = terminal
        terminal.connect_wire(terminal_pin, self)