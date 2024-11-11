from collections import deque

class Simulator:
    def __init__(self, turing_machine):
        self.tm = turing_machine
        self.visited_states = set()

    def simulate(self, input_string, output_file="output.txt"):
        self.tm.reset(input_string)
        configurations = deque([(self.tm.current_state, self.tm.head_position, self.tm.tape[:])])
        steps = []

        while configurations:
            state, position, tape = configurations.popleft()
            self.tm.current_state, self.tm.head_position, self.tm.tape = state, position, tape

            # Guardar el estado actual en los pasos y en el archivo de salida
            current_configuration = f"State: {state}, Position: {position}, Tape: {''.join(tape)}"
            steps.append(current_configuration)
            print(current_configuration)

            if self.tm.is_accepting():
                self.save_output("Accepted", steps, output_file)
                return "Accepted"
            elif self.tm.is_rejecting():
                self.save_output("Rejected", steps, output_file)
                return "Rejected"
            elif (state, position) in self.visited_states:
                continue
            else:
                self.visited_states.add((state, position))
                for next_state, write_symbol, direction in self.tm.step():
                    if next_state:
                        new_tape = tape[:]
                        if 0 <= position < len(new_tape):
                            new_tape[position] = write_symbol
                        else:
                            new_tape.append(write_symbol)

                        new_position = position + (1 if direction == "R" else -1)
                        if new_position < 0:
                            new_tape.insert(0, "_")
                            new_position = 0
                        elif new_position >= len(new_tape):
                            new_tape.append("_")

                        configurations.append((next_state, new_position, new_tape))

        self.save_output("Rejected", steps, output_file)
        return "Rejected"

    def save_output(self, result, steps, output_file):
        with open(output_file, "w") as file:
            file.write("\n".join(steps))
            file.write(f"\nResult: {result}\n")
