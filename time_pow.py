
import timeit
import csv 
from test_pow import pow1, pow2, pow3
import pandas as pd

f = open("results.csv", "w")
writer = csv.DictWriter(f, fieldnames=['i','Pow1', 'Pow2', 'Pow3'])
writer.writeheader()
f.close()
with open('results.csv', 'a+', newline='') as f:
  f = csv.writer(f)
  for num in range(1, 6):
    f.writerow([num])
    for i in [1, 10, 100, 1000, 10000]:
      p1 = timeit.Timer(lambda: pow1(num, i))
      p2 = timeit.Timer(lambda: pow2(num, i))
      p3 = timeit.Timer(lambda: pow3(num, i))
      line = [i, p1.timeit(number=1), p2.timeit(number=1), p3.timeit(number=1)]
      f.writerow(line)


