# Moore Machine Implementation with detailed processing

# Moore states definition
moore_states = {
    'S1': {'output': 'A', '0': 'S1', '1': 'S2'},
    'S2': {'output': 'B', '0': 'S3', '1': 'S4'},
    'S3': {'output': 'A', '0': 'S5', '1': 'S2'},
    'S4': {'output': 'B', '0': 'S2', '1': 'S6'},
    'S5': {'output': 'C', '0': 'S2', '1': 'S6'},
    'S6': {'output': 'C', '0': 'S5', '1': 'S2'},
    'S7': {'output': 'C', '0': 'S5', '1': 'S7'}
}

def process_input_detailed(input_string):
    current_state = 'S1'
    print(f"Input: {input_string}")
    print("Step-by-step process:")
    print("Current State | Input | Next State | Output")
    print("-" * 45)
    
    # Initial state output
    print(f"{current_state:13} | {'Start':5} | {'':10} | {moore_states[current_state]['output']}")
    
    for char in input_string:
        next_state = moore_states[current_state][char]
        output = moore_states[next_state]['output']
        print(f"{current_state:13} | {char:5} | {next_state:10} | {output}")
        current_state = next_state
    
    final_output = moore_states[current_state]['output']
    print(f"\nFinal output: {final_output}")
    print("=" * 50)
    return final_output

# Test inputs
inputs = ["00110", "11001", "1010110", "101111"]

print("MOORE MACHINE PROCESSING")
print("=" * 50)

# Process each input with detailed steps
for input_str in inputs:
    process_input_detailed(input_str)