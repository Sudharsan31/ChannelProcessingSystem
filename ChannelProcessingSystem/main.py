import numpy as np

# Define the functions

# Y = m*X + C
def array_Y(m, c, X):
    Y = m * np.array(X) + c
    return Y

# B = A + Y
def array_B(A, Y):
    B = A + Y
    return B

# b = mean(B)
def metric_b(B):
    b = np.mean(B)
    return b

# A = 1/X
def array_A(X):
    A = 1 / np.array(X)
    return A

# C = X + b
def array_C(X, b):
    C = np.array(X) + b
    return C

# Test function (to test easy extensiblity)
# G = m*g*h
def metric_G(m,g,h):
    G = m*g*h
    return G

parameters = {}

# Read values from parameters.txt
with open("parameters.txt", "r") as parameter_file:
    for line in parameter_file:
        # reads the corresponding values from parameters.txt
        # when extra inputs are added, it reads that too (easily extensible)
        key, value = line.strip().split(", ")
        parameters[key] = float(value)

# Read values from channels.txt
with open("channels.txt", "r") as channel_file:
    for line in channel_file:
        data = line.strip().split(", ")
        # converts the numbers to float, ignoring the letter X from channels.txt,
        # as string can't be converted to float
        a = [float(x) for x in data[1:]]

# Defining the values before calculating the functions
X = a
m = parameters["m"]
c = parameters["c"]

# extensibilty test inputs
g = parameters["g"]
h = parameters["h"]

# Defines the functions to each letter as required
Y = array_Y(m, c, X)
A = array_A(X)
B = array_B(A, Y)
b = metric_b(B)
C = array_C(X,b)

# extensibilty test function
G = metric_G(m,g,h)

# prints the calculated value of metric_b
print(f"The value of metric b is : {b}")

# prints the calculated value of metric_G (extensiblity test)
print(f"the value of metric G is : {G}")

# prints the calculated value of all the other functions (OPTIONAL)
#print(f"The value of array A is : {A}")
#print(f"The value of array B is : {B}")
#print(f"The value of array C is : {C}")
#print(f"The value of array Y is : {Y}")