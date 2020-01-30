import numpy as np 

input_data = np.array([2,3])

weights = {
          'node_0':np.array([1,1]),
          'node_1':np.array([-1,1]), 
          'output':np.array([2,-1])
          }
node_0_input = (input_data * weights['node_0']).sum()

node_0_output = np.tahn(node_0_input) 

node_1_input = (input_data * weights['node_1']).sum()

node_1_output = np.tanh(node_1_input)

hidden_layer_values = np.array([node_0_value, node_1_value]) 

print(hidden_layer_values)

output = (hidden_layer_values * weights['output']).sum()

print(output)
