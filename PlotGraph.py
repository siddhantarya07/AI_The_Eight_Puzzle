from cProfile import label
import matplotlib.pyplot as plt

x_ucs = [2,4,8,12,16,20]
y_ucs = [14,60,500,3607,20293,71780]

x_misplaced = [2,4,8,12,16,20]
y_misplaced= [5,12,34,203,1065,4974]

x_manhattan = [2,4,8,12,16,20]
y_manhattan= [5,10,24,64,388,786]

plt.plot(x_ucs, y_ucs, label="Uniform Cost Search")
plt.plot(x_misplaced, y_misplaced, label="A* with Misplaced Tile")
plt.plot(x_manhattan, y_manhattan, label="A* with Manhattan Distance")
plt.xlabel("Solution Depth")
plt.ylabel("Number of Nodes Expanded")
plt.legend(loc='upper right')
plt.show()



# y_ucs_time = [0.00105834,0.00099658,0.03923344,0.35713315,9.72216749,266.45185589]

# y_misplaced_time= [0.0,0.0,0.00100827,0.00199007,0.05316710,0.70125699]

# y_manhattan_time= [0.0009975,0.00223922,0.00297236,0.02707028,0.06337380,0.12660217]

# plt.plot(x_ucs, y_ucs_time, label="Uniform Cost Search")
# plt.plot(x_misplaced, y_misplaced_time, label="A* with Misplaced Tile")
# plt.plot(x_manhattan, y_manhattan_time, label="A* with Manhattan Distance")
# plt.xlabel("Solution Depth")
# plt.ylabel("Time in Seconds")
# plt.legend(loc='upper right')
# plt.show()