
import timeit
import csv 
from test_pow import pow1, pow2, pow3

f = open("results.csv", "w")
writer = csv.DictWriter(f, fieldnames=['i','Pow1', 'Pow2', 'Pow3'])
writer.writeheader()
f.close()
num = 
for i in [1, 10, 100, 1000, 10000]:
  p1 = timeit.Timer(lambda: pow1(num, i))
  p2 = timeit.Timer(lambda: pow2(num, i))
  p3 = timeit.Timer(lambda: pow3(num, i))

  line = [i, p1.timeit(number=1), p2.timeit(number=1), p3.timeit(number=1)]
  with open('results.csv', 'a+', newline='') as f:
          csv_writer = csv.writer(f)
          csv_writer.writerow(line)
f.close()
import matplotlib.pyplot as plt
import pandas as pd
table = pd.read_csv("results.csv")
t = table['i']
a = table['Pow1']
b = table['Pow2']
c = table['Pow3']

plt.plot(t, a, 'r') # plotting t, a separately 
plt.plot(t, b, 'b') # plotting t, b separately 
plt.plot(t, c, 'g') # plotting t, c separately 
plt.legend(["Pow 1", "Pow 2", "Pow 3"])
plt.show()



