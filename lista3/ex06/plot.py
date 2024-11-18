import numpy as np
import matplotlib.pyplot as plt
from functions import f

x = np.linspace(-1, 2, 100)
y = f(x)

plt.plot(x, y)
plt.show()
