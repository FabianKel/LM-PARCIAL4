class TuringMachine:
    def __init__(self, config):
        self.states = config["Q"]
        self.input_alphabet = config['Σ']
        self.tape_alphabet = config["Γ"]
        self.initial_state = config["q0"]
        self.accept_state = config["qaccept"]
        self.reject_state = config["qreject"]
        self.transitions = config["δ"]
        self.current_state = self.initial_state
        self.tape = []
        self.head_position = 0

    def reset(self, input_string):
        self.tape = list(input_string) + ["_"]
        self.current_state = self.initial_state
        self.head_position = 0

    def step(self):
        symbol = self.tape[self.head_position]
        if self.current_state in self.transitions and symbol in self.transitions[self.current_state]:
            for (next_state, write_symbol, direction) in self.transitions[self.current_state][symbol]:
                # Ejecuta cada transición posible para un paso no determinista
                yield next_state, write_symbol, direction
        else:
            yield None  # No hay transición válida

    def is_accepting(self):
        return self.current_state == self.accept_state

    def is_rejecting(self):
        return self.current_state == self.reject_state
