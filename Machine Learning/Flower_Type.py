import numpy as np
from matplotlib import pyplot as plt

# data set
#      len  wid  type
data = [[3, 1.5,  1],
        [2,  1,   0],
        [4, 1.5,  1],
        [3,  1,   0],
        [3.5, .5, 1],
        [2,  .5,  0],
        [5.5, 1,  1],
        [1,  1,   0]]

unknown_data = [4.5, 1]

# neural network

#       o       flower type (0 or 1)
#      / \          weights and bias value
#     o   o         length, width of data set

# initially taking random values
w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.randn()

print("w1 : ", w1)
print("w2 : ", w2)
print("b : ", b)

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x) * (1 - sigmoid(x))

"""
T = np.linspace(-5, 5, 100)
Y = sigmoid(T)
plt.plot(T, sigmoid(T), c='r')
plt.plot(T, sigmoid_der(T), c='b')
"""
# plt.show()

"""
# scatter data
plt.axis([0, 6, 0, 2])
plt.grid()
for i in range(len(data)):
    point = data[i]
    color = 'r'
    if point[2] == 0:
        color = 'b'
    plt.scatter(point[0], point[1], c=color)

# plt.show()
"""
learning_rate = 0.2
#cost_graph = []
cost_graph2 = []

for i in range(50000):
    ri = np.random.randint(len(data))
    point = data[ri]

    z = point[0] * w1 + point[1] * w2 + b
    prediction = sigmoid(z)

    target = point[2]
    cost = np.square(prediction - target)

    #cost_graph.append(cost)

    dcost_dpred = 2 * (prediction - target)
    dpred_dz = sigmoid_der(z)

    dz_dw1 = point[0]
    dz_dw2 = point[1]
    dz_db = 1

    dcost_dz = dcost_dpred * dpred_dz

    dcost_dw1 = dcost_dz * dz_dw1
    dcost_dw2 = dcost_dz * dpred_dz
    dcost_db = dcost_dz * dz_db

    w1 = w1 - learning_rate * dcost_dw1
    w2 = w2 - learning_rate * dcost_dw2
    b = b - learning_rate * dcost_db

    if i % 100 == 0:
        cost_sum = 0
        for j in range(len(data)):
            point2 = data[j]

            z2 = point2[0] * w1 + point2[1] * w2 + b
            pred = sigmoid(z2)

            tar = point2[2]
            cost_sum += np.square(pred - tar)

        cost_graph2.append(cost_sum/len(data))


plt.plot(cost_graph2)

for i in range(len(data)):
    point = data[i]
    print(point)
    z = point[0] * w1 + point[1] * w2 + b
    prediction = sigmoid(z)
    print("flower type : {}" .format(prediction))

while 1:
    print("Enter the length and width of flower - ")
    len = input("Len >> ")
    width = input("Width >> ")
    z = len * w1 + width * w2 + b
    pred = sigmoid(z)

    if pred <= 0.5:
        print("Red")
    else:
        print("Blue")


