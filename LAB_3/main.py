import time
import math
import matplotlib.pyplot as plt

# ANSI color codes for pretty printing
Red = '\033[91m'
Green = '\033[92m'
White = '\033[97m'


def algorithm_1(n):
    # Create a list of n+1 True values to represent the numbers from 1 to n
    c = [True] * (n + 1)

    # Mark 1 as not prime
    c[1] = False

    # Initialize the loop variable
    i = 2

    # Loop through all the numbers from 2 to n
    while i <= n:
        # If i is prime, mark all multiples of i as not prime
        if c[i]:
            j = 2 * i
            while j <= n:
                c[j] = False
                j = j + i

        # Move to the next number
        i = i + 1

    # Return the list of True/False values representing whether each number is prime or not
    return c


def algorithm_2(n):
    c = [True] * (n + 1)  # Initialize all values of c to True
    c[1] = False  # Set c[1] to False
    i = 2

    while i <= n:
        j = 2 * i  # Start with j = 2i and mark all multiples of i as composite
        while j <= n:
            c[j] = False
            j = j + i
        i = i + 1  # Move to the next number in the list

    return c


def algorithm_3(n):
    # Initialize all values of c to True
    c = [True] * (n + 1)

    # Set c[1] to False, since 1 is not a prime number
    c[0] = c[1] = False

    # Initialize the loop counter
    i = 2

    while i <= n:
        if c[i]:
            # Start j at i + 1, since we already know i is prime
            j = i + 1
            while j <= n:
                # If j is divisible by i, it's not a prime number
                if j % i == 0:
                    c[j] = False
                j = j + 1
        i = i + 1

    return c


def algorithm_4(n):
    c = [True] * (n + 1)  # Initialize all values of c to True
    c[1] = False  # Set c[1] to False
    i = 2

    while i <= n:
        j = 2
        is_prime = True
        while j < i:
            if i % j == 0:
                is_prime = False  # If i is divisible by any number less than itself, it is not prime
                break
            j = j + 1
        if not is_prime:
            c[i] = False  # Set the corresponding value in c to False if i is not prime
        i = i + 1

    return c


def algorithm_5(n):
    c = [True] * (n + 1)  # Create a list of n+1 elements and set all of them to True initially
    c[0] = c[1] = False  # Set the first two elements (0 and 1) to False as they are not prime numbers
    i = 2  # Start with i=2, the first prime number
    while (i <= n):  # Continue until the given upper bound n
        j = 2  # Start with j=2
        while (j <= math.sqrt(i)):  # Check if j is a divisor of i up to the square root of i
            if (i % j == 0):  # If j divides i, then i is not prime
                c[i] = False  # Mark c[i] as False
            j += 1  # Increment j
        i += 1  # Increment i
    return c  # Return the list of prime numbers


def exec_time(function, n):
    start_time = time.time()
    function(n)
    end_time = time.time()
    return end_time - start_time


n = 5000

first = exec_time(algorithm_1, n)
second = exec_time(algorithm_2, n)
third = exec_time(algorithm_3, n)
fourth = exec_time(algorithm_4, n)
fifth = exec_time(algorithm_5, n)

print(Green + "Algorithm 1 - " + White, first, "s")
print(Green + "Algorithm 2 - " + White, second, "s")
print(Green + "Algorithm 3 - " + White, third, "s")
print(Green + "Algorithm 4 - " + White, fourth, "s")
print(Green + "Algorithm 5 - " + White, fifth, "s")

# Create a bar chart with execution times
labels = ['Algorithm 1', 'Algorithm 2', 'Algorithm 3', 'Algorithm 4', 'Algorithm 5']
times = [first, second, third, fourth, fifth]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
plt.bar(labels, times, color=colors)
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time Comparison')
plt.grid()

for i, v in enumerate(times):
    plt.text(i, v, f"{v:.4f}", ha='center', va='bottom')

plt.text(0.05, 0.95, f"n={n}", transform=plt.gca().transAxes, ha='left', fontweight='bold',
         bbox=dict(facecolor='white', edgecolor='black', boxstyle='square'))

plt.show()

Algorithms = [
    {
        "name": "Algorithm 1",
        "alg": lambda n: algorithm_1(n)
    },
    {
        "name": "Algorithm 2",
        "alg": lambda n: algorithm_2(n)
    },
    {
        "name": "Algorithm 3",
        "alg": lambda n: algorithm_3(n)
    },
    {
        "name": "Algorithm 4",
        "alg": lambda n: algorithm_4(n)
    },
    {
        "name": "Algorithm 5",
        "alg": lambda n: algorithm_5(n)
    }
]

times = []

for alg in Algorithms:
    exec_times = []
    for i in range(1, 6):
        exec_t = exec_time(alg["alg"], i * 1000)
        exec_times.append(exec_t)
        print(Red + alg["name"] + White, " - ", i * 1000, "elements - ", exec_t, "s")
    times.append(exec_times)

x_axis = [i * 1000 for i in range(1, 6)]

plt.title('Execution Time Comparison')
plt.plot(x_axis, times[0], label=Algorithms[0]["name"])
plt.plot(x_axis, times[1], label=Algorithms[1]["name"])
plt.plot(x_axis, times[2], label=Algorithms[2]["name"])
plt.plot(x_axis, times[3], label=Algorithms[3]["name"])
plt.plot(x_axis, times[4], label=Algorithms[4]["name"])

plt.xlabel('Input = n')
plt.ylabel('Time ')

plt.grid()
plt.legend()
plt.show()
