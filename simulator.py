class Simulator:
    def __init__(self, turing_machine):
        self.tm = turing_machine
        self.visited_states = set()

    def simulate(self, input_string):
        self.tm.reset(input_string)
        configurations = [(self.tm.current_state, self.tm.head_position, self.tm.tape)]

        while configurations:
            state, position, tape = configurations.pop(0)  # BFS usando `pop(0)`
            self.tm.current_state, self.tm.head_position, self.tm.tape = state, position, tape

            # Se imprime el estado actual de la simulación
            print(f"Current state: {state}, Head position: {position}, Tape: {''.join(tape)}")

            if self.tm.is_accepting():
                return "Accepted"
            elif self.tm.is_rejecting():
                return "Rejected"
            elif (state, position) in self.visited_states:
                continue  # Salta si ya visitó este estado y posición para evitar bucles infinitos
            else:
                self.visited_states.add((state, position))

                for next_state, write_symbol, direction in self.tm.step():
                    if next_state:
                        new_tape = tape[:]
                        if 0 <= position < len(new_tape):
                            new_tape[position] = write_symbol
                        else:
                            new_tape.append(write_symbol)  # Manejar posición fuera de la cinta

                        new_position = position + (1 if direction == "R" else -1)

                        # Expandir la cinta si la cabeza se mueve más allá de los extremos
                        if new_position < 0:
                            new_tape.insert(0, "_")
                            new_position = 0
                        elif new_position >= len(new_tape):
                            new_tape.append("_")

                        configurations.append((next_state, new_position, new_tape))
        return "Rejected"
