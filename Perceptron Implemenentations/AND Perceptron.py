import pandas as pd

# Set weight1, weight2, and bias
weight1 = 3.0
weight2 = 1.0
bias = -4.0

# Inputs and outputs
test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
correct_outputs = [False, False, False, True]
outputs = []

# Generate and check output
for test_input, correct_output in zip(test_inputs, correct_outputs):
    linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
    # Output - activation function is the biased heaviside function
    output = int(linear_combination >= 0)
    is_correct_string = 'Yes' if output == correct_output else 'No'
    outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

# Print output
num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
output_frame = pd.DataFrame(outputs, columns=['Input 1', '  Input 2', '  Linear Combination', '  Activation Output', '  Is Correct'])
if not num_wrong:
    print('AND Gate logic implemented correctly.\n')
else:
    print('One of the outputs were incorrect.\n')
print(output_frame.to_string(index=False))

# Return

/* Input 1    Input 2    Linear Combination    Activation Output   Is Correct
      0          0                  -4.0                    0          Yes
      0          1                  -3.0                    0          Yes
      1          0                  -1.0                    0          Yes
      1          1                   0.0                    1          Yes
*/
