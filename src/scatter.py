import sys

import matplotlib.pyplot as plt


plt.switch_backend("Agg")

data_file = sys.argv[1]
out_file = sys.argv[2]
title = sys.argv[3]
x_label = sys.argv[4]
y_label = sys.argv[5]

x_values = []
y_values = []

for line in open(data_file):
    fields = line.rstrip().split()
    x_values.append(float(fields[0]))
    y_values.append(float(fields[1]))

fig, ax = plt.subplots()
ax.scatter(x_values, y_values)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.set_title(title)

plt.savefig(out_file, bbox_inches="tight")
