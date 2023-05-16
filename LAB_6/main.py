import time
import numpy as np
from matplotlib import pyplot as plt
from prettytable import PrettyTable
from decimal import *


def bbpPi(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    pi = 0
    for k in range(n + 1):
        pi += (1 / pow(16, k)) * (
                4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))
    return int(pi * pow(10, n) % 10)


def legendrePi(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    getcontext().prec = n + 1
    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(1) / Decimal(4)
    p = Decimal(1)
    for _ in range(n):
        atmp = (a + b) / Decimal(2)
        b = (a * b).sqrt()
        t -= p * (a - atmp) ** Decimal(2)
        a = atmp
        p *= Decimal(2)
    pi = (a + b) ** Decimal(2) / (Decimal(4) * t)
    return int(str(pi)[n])


def spigotPi(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    pi = 0
    d = 1
    for i in range(n):
        pi += 4 * d
        d = (d * 10 - int(d * 10 / 10) * 10)
    return int(pi / pow(10, n - 1)) % 10


def bar(alg):
    colors = ['lightblue', 'lightgreen', 'lightpink', 'lavender', 'lightcyan']
    x = range(1, len(alg) + 1)
    width = 0.9
    for i, value in enumerate(alg):
        plt.bar(x[i], value, width, color=colors[i])


if __name__ == "__main__":
    n = [10, 50, 100, 200, 300]
    bbpTime = []
    legendreTime = []
    spigotTime = []
    xAxis = []
    for i in n:
        xAxis.append(str(i))

    arr = [i for i in range(len(n))]
    x = np.arange(1, len(arr) + 1)

    for nr in n:
        startTime = time.perf_counter()
        bbpPi(nr)
        endTime = time.perf_counter()
        bbpTime.append(endTime - startTime)
        print(f"BBP Time: {endTime - startTime}")

        startTime = time.perf_counter()
        legendrePi(nr)
        endTime = time.perf_counter()
        legendreTime.append(endTime - startTime)
        print(f"Legendre Time: {endTime - startTime}")

        startTime = time.perf_counter()
        spigotPi(nr)
        endTime = time.perf_counter()
        spigotTime.append(endTime - startTime)
        print(f"Spigot Time: {endTime - startTime}")

    pastel_colors = ['#FFB6C1', '#87CEFA', '#90EE90', '#FFDAB9', '#B0C4DE']  # List of pastel colors
    bar(bbpTime)
    plt.xticks(x, xAxis)
    plt.xlabel('N-th digit')
    plt.ylabel('Time, s')
    plt.title('BBP Algorithm', fontsize=16)
    plt.grid(True)  # Add grid
    plt.show()

    bar(legendreTime)
    plt.xticks(x, xAxis)
    plt.xlabel('N-th digit')
    plt.ylabel('Time, s')
    plt.title('Legendre Algorithm', fontsize=16)
    plt.grid(True)  # Add grid
    plt.show()

    bar(spigotTime)
    plt.xticks(x, xAxis)
    plt.xlabel('N-th digit')
    plt.ylabel('Time, s')
    plt.title('Spigot Algorithm', fontsize=16)
    plt.grid(True)  # Add grid
    plt.show()

    plt.plot(n, bbpTime, linewidth=5, label='BBP', color=pastel_colors[0])
    plt.plot(n, legendreTime, linewidth=5, label='Legendre', color=pastel_colors[1])
    plt.plot(n, spigotTime, linewidth=5, label='Spigot', color=pastel_colors[2])
    plt.xlabel('N-th digit')
    plt.ylabel('Time, s')
    plt.title('Algorithms Comparison', fontsize=16)
    plt.legend()
    plt.grid(True)  # Add grid
    plt.show()

    Yellow = '\033[93m'
    END = '\033[0m'

    myTable = PrettyTable(["Algorithm-Nth digit", *n])
    myTable.add_row(["BBP", *bbpTime])
    myTable.add_row(["Spigot", *spigotTime])
    myTable.add_row(["Legendre", *legendreTime])
    print(Yellow + str(myTable) + END)
