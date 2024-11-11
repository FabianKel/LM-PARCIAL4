class TuringMachine:
    def __init__(self, config):
        self.states = config.get("Q", [])
        self.input_alphabet = config.get("Σ", [])
        self.tape_alphabet = config.get("Γ", [])
        self.initial_state = config.get("q0")
        self.accept_state = config.get("qaccept")
        self.reject_state = config.get("qreject")
        self.transitions = config.get("δ", {})
        self.current_state = self.initial_state
        self.tape = []
        self.head_position = 0

        self.validate_configuration(config)  # Pasar config como parámetro

    def validate_configuration(self, config):
        required_keys = ["Q", "Σ", "Γ", "q0", "qaccept", "qreject", "δ"]
        for key in required_keys:
            if key not in config:
                raise ValueError(f"Configuration missing required key: {key}")
        
        if self.accept_state not in self.states or self.reject_state not in self.states:
            raise ValueError("Accept and reject states must be defined in states.")

    def reset(self, input_string):
        self.tape = list(input_string) + ["_"]
        self.current_state = self.initial_state
        self.head_position = 0

    def step(self):
        symbol = self.tape[self.head_position]
        if self.current_state in self.transitions and symbol in self.transitions[self.current_state]:
            for (next_state, write_symbol, direction) in self.transitions[self.current_state][symbol]:
                yield next_state, write_symbol, direction
        else:
            yield None

    def is_accepting(self):
        return self.current_state == self.accept_state

    def is_rejecting(self):
        return self.current_state == self.reject_state
