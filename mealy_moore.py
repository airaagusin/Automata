# =====================================================
# FINITE AUTOMATA WITH OUTPUT
# MEALY MACHINE and MOORE MACHINE IMPLEMENTATION
# Task: Print "a" whenever the sequence "01" is encountered
# =====================================================

# ----------------------------
# MEALY MACHINE IMPLEMENTATION
# ----------------------------

def mealy_machine(input_str):
    """
    Mealy Machine that prints 'a' whenever '01' sequence is found.
    Output depends on transition (state + input).
    """
    state = 'A'
    output = []

    for symbol in input_str:
        if state == 'A':
            if symbol == '0':
                state = 'B'
                output.append('b')
            else:  # symbol == '1'
                state = 'A'
                output.append('b')

        elif state == 'B':
            if symbol == '0':
                state = 'B'
                output.append('b')
            else:  # symbol == '1'
                state = 'C'
                output.append('a')

        elif state == 'C':
            if symbol == '0':
                state = 'B'
                output.append('b')
            else:  # symbol == '1'
                state = 'A'
                output.append('b')

    return ''.join(output)


# ----------------------------
# MOORE MACHINE IMPLEMENTATION
# ----------------------------

def moore_machine(input_str):
    """
    Moore Machine that prints 'a' whenever '01' sequence is found.
    Output depends on the current state only.
    """
    # Define state outputs
    outputs = {
        'A': 'b',
        'B': 'b',
        'C': 'a'
    }

    state = 'A'
    output = [outputs[state]]

    for symbol in input_str:
        if state == 'A':
            if symbol == '0':
                state = 'B'
            else:
                state = 'A'
        elif state == 'B':
            if symbol == '0':
                state = 'B'
            else:
                state = 'C'
        elif state == 'C':
            if symbol == '0':
                state = 'B'
            else:
                state = 'A'

        output.append(outputs[state])

    return ''.join(output)


# ----------------------------
# MAIN PROGRAM
# ----------------------------
if __name__ == "__main__":
    print("FINITE AUTOMATA WITH OUTPUT")
    print("===========================")
    user_input = input("Enter a binary input (0s and 1s only): ")

    # Run Mealy Machine
    mealy_output = mealy_machine(user_input)
    print("\n--- MEALY MACHINE ---")
    print("Input:  ", user_input)
    print("Output: ", mealy_output)

    # Run Moore Machine
    moore_output = moore_machine(user_input)
    print("\n--- MOORE MACHINE ---")
    print("Input:  ", user_input)
    print("Output: ", moore_output)
