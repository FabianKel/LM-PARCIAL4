from collections import deque, defaultdict

class Simulator:
    def __init__(self, turing_machine):
        self.tm = turing_machine
        self.visited_states = defaultdict(int)  # Track each configuration's occurrence

    def simulate(self, input_string, output_file="output.txt"):
        self.tm.reset(input_string)
        configurations = deque([(self.tm.current_state, self.tm.head_position, tuple(self.tm.tape))])
        steps = []

        while configurations:
            state, position, tape = configurations.popleft()
            self.tm.current_state, self.tm.head_position, self.tm.tape = state, position, list(tape)

            current_configuration = f"State: {state}, Position: {position}, Tape: {''.join(tape)}"
            steps.append(current_configuration)
            print(current_configuration)

            if self.tm.is_accepting():
                self.save_output("Accepted", steps, output_file)
                return "Accepted"
            elif self.tm.is_rejecting():
                self.save_output("Rejected", steps, output_file)
                return "Rejected"
            elif self.visited_states[(state, position, tuple(tape))] >= 3:  # Loop detection
                self.save_output("Infinite Loop", steps, output_file)
                return "Infinite Loop"
            else:
                self.visited_states[(state, position, tuple(tape))] += 1
                for result in self.tm.step():
                    if result is not None:  # Ensure result is not None
                        next_state, write_symbol, direction = result
                        new_tape = list(tape)
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

                        configurations.append((next_state, new_position, tuple(new_tape)))

        self.save_output("Rejected", steps, output_file)
        return "Rejected"

    def save_output(self, result, steps, output_file):
        with open(output_file, "w") as file:
            file.write("\n".join(steps))
            file.write(f"\nResult: {result}\n")

