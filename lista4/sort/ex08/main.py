import numpy as np
import matplotlib.pyplot as plt
import time

from progress.bar import Bar

from bubble import bubble_sort
from quick import quick_sort
from selection import selection_sort

N = [100, 200, 400, 800, 1600, 3200]
tempos = np.zeros((3, len(N)))

def mede_tempo(func, arr):
    t0 = time.time()
    func(arr)
    t1 = time.time()
    return t1 - t0

bar = Bar("Sorting...", max=sum(N))
for i, n in enumerate(N):
    arr = np.random.randint(0, n, n)
    tempos[0][i] = mede_tempo(bubble_sort, arr)
    tempos[1][i] = mede_tempo(quick_sort, arr)
    tempos[2][i] = mede_tempo(selection_sort, arr)
    bar.next(n)
bar.finish()

plt.loglog(N, tempos[0], label='Bubble Sort')
plt.loglog(N, tempos[1], label='Quick Sort')
plt.loglog(N, tempos[2], label='Selection Sort')

plt.legend()
plt.xlabel('N')
plt.ylabel('Tempo (s)')
plt.show()
