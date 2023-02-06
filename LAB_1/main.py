import numpy as np
import timeit
import matplotlib.pyplot as plt

Blue = '\033[94m'
Red = '\033[91m'
Yellow = '\033[93m'
END = '\033[0m'


# decorator exec_time which calculates and outputs the execution time
# of a decorated function.
# The execution time is calculated in microseconds
# and the results can also be stored
# in the running_time dictionary for later use (e.g. for graphing).
# The decorated function is passed as an argument to exec_time,
# and the returned value from exec_time (which is a nested function real_decorator)
# is used to further decorate the function.


def exec_time(name):
    def real_decorator(func):
        result = None

        def wrapper(n):
            t_start = timeit.default_timer()
            result = func(n)
            t_end = timeit.default_timer()

            # * 10 ** 6 scales the elapsed time to microseconds,
            # #as 10 ** 6 is equivalent to 10 raised to the power of 6,
            # which equals 1 million.

            elapsed_time = round((t_end - t_start) * 10 ** 6, 4)
            print(
                f'Result for the input  {Red}{result}{END}: '
                f'{Red}{elapsed_time}{END} microseconds.')

            # saving the  results for graphs
            if name in running_time.keys():
                running_time[name].append(elapsed_time)
            else:
                running_time[name] = list()
                running_time[name].append(elapsed_time)

            return result

        return wrapper

    return real_decorator


running_time = dict()
values = [1, 10, 20, 30, 40, 50, 60, 70, 80]
# values = [180,190,200]


def exec_time_recursive(func, name, *args):
    t_start = timeit.default_timer()
    t_end = timeit.default_timer()
    func(args[0])

    elapsed_time = round((t_end - t_start) * 10 ** 6, 4)
    print(f'Result for the  input {args[0]}{END}: {Red}{elapsed_time}{END} microseconds.')

    # save results for graphing
    if name in running_time.keys():
        running_time[name].append(elapsed_time)
    else:
        running_time[name] = list()
        running_time[name].append(elapsed_time)


def plot_result():
    names = np.array(list(running_time.keys()))
    times = np.array(list(running_time.values()))
    algorithm_num = 0

    plt.title('RUNNING TIME ', fontsize=15, color='blue', fontweight='bold')
    plt.xlabel('Values', fontsize=15, color='blue')
    plt.ylabel("Time (microseconds)", fontsize=13, color='blue')

    for history in times:
        x_axis = np.array(values)
        y_axis = times[algorithm_num]

        plt.plot(x_axis, y_axis, label=names[algorithm_num])

        algorithm_num += 1

    plt.legend()
    plt.grid()
    plt.show()


# First Method = Iterative Method
@exec_time('ITERATIVE_METHOD')
def iterative_fib(n: int) -> int:
    i, j = 0, 0

    for k in range(n):
        j = i + j
        i = j - i

    return j


# Second Method = Iterative Memoization
@exec_time('ITERATIVE MEMOIZATION')
def iterative_fib_with_memoization(n: int) -> int:
    fib = [0, 1]

    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[n]


# Third Method = Dynamic
@exec_time('DYNAMIC_METHOD')
def fibonacci_dynamic(num):
    fibonacci = [0, 1]
    for i in range(2, num + 1):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return fibonacci[num]


# Fourth Method = Eigen
@exec_time('EIGEN_METHOD')
def eigen_fib(n: int) -> int:
    f1 = np.array(([1, 1], [1, 0]))
    eigenvalues, eigenvectors = np.linalg.eig(f1)
    fn = eigenvectors @ np.diag(eigenvalues ** n) @ eigenvectors.T

    return int(np.rint(fn[0, 1]))


# Fifth Method = Eigen Optimized
@exec_time('EIGEN_OPTIMIZED')
def eigen_fib_optimized(n: int) -> int:
    multiply = lambda a, b, x, y: (x * (a + b) + a * y, a * x + b * y)
    square = lambda a, b: ((a * a) + ((a * b) << 1), a * a + b * b)

    def power(a, b, m):
        n = 2

        if m == 0:
            return (0, 1)
        elif m == 1:
            return (a, b)
        else:
            x, y = a, b

            while n <= m:
                x, y = square(x, y)
                n = n * 2

            a, b = power(a, b, m - n // 2)

            return multiply(x, y, a, b)

    res, _ = power(1, 0, n)

    return res


# Sixth Method = Golden Ratio
@exec_time('GOLDEN_RATIO_METHOD')
def golden_ratio_fib(n: int) -> int:
    sqrt_of_five = 2.23606797749979
    phi = (1 + sqrt_of_five) / 2
    inv_phi = (1 - sqrt_of_five) / 2

    return int((phi ** n - inv_phi ** n) / sqrt_of_five)


print('\n1. Dynamic Method:')
for value in values:
    fibonacci_dynamic(value)

print('\n2. Iterative:')
for value in values:
    iterative_fib(value)

print('\n3. Iterative with memoization:')
for value in values:
    iterative_fib_with_memoization(value)

print('\n4. Eigenvectors:')
for value in values:
    eigen_fib(value)

print('\n5. Eigenvectors (optimized):')
for value in values:
    eigen_fib_optimized(value)

print('\n6. Golden Ratio:')
for value in values:
    golden_ratio_fib(value)

# find the fastest method
mean_times = running_time.copy()

for key in mean_times.keys():
    mean_times[key] = np.mean(np.array(mean_times[key]))

mean_times = {k: v for k, v in sorted(mean_times.items(), key=lambda item: item[1])}

print(f'\n {Red} Algorithms ranking (for 1-80 values): {END}')
for i, key in enumerate(mean_times.keys()):
    print(f'{i + 1}: {Blue}{key}{END} = {Yellow}{mean_times[key]}{END} microseconds.')

plot_result()
del running_time['EIGEN_METHOD']
plot_result()
del running_time['DYNAMIC_METHOD']
plot_result()
del running_time['EIGEN_OPTIMIZED']
plot_result()
