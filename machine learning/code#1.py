import matplotlib.pyplot as plt
import numpy as np

x = range(0, 10)
y = [1.8 * F + 32 for F in x]

print(x)
print(y)

plt.plot(x, y, '-*r')
plt.show()