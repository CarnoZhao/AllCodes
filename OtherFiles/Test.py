import random
import matplotlib.pyplot as plt
import seaborn as sns
from math import log10
# seaborn can make pyplot's figure more beautiful
# if you have not install seaborn package,
# you can delete that line

wild = 1 # the ancestor cell, and the number of wild type
mutant = 0 # the number of mutation
data = [] # to store 1000 data points
N = 10 ** 3 # number of maximum replications
M = 1 # number of trials
bin_num = 100
X = list(log10(x) for x in range(1, N, N // bin_num))
Y = [4 - 2 * x for x in X]
# I do not know what did you derive in class, so the log-log line
# of power law distribution is not correct. Do it youself !!
plt.plot(X, Y)
plt.show()