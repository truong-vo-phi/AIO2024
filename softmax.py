import torch

# Initialize the tensor data
data = torch.Tensor([1, 2, 3])

# Define the softmax function
def Softmax(data):
    result = []
    sum_torch = 0
    for j in data: 
        sum_torch += torch.exp(j)
    for i in data:
        result.append(torch.exp(i) / sum_torch)
    return result

def softmax_stable(data):
    c = max(data)
    result = []
    sum_torch = 0
    for j in data: 
        sum_torch += torch.exp(j-c)
    for i in data:
        result.append(torch.exp(i-c) / sum_torch)
    return result
# Compute the softmax
softmax = softmax_stable(data)

# Print the output
print(softmax)
