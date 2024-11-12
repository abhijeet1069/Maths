import numpy as np

def function(x):
    return 160-9.8*x  # Example function: f(x) = x^2

def riemann_sums(func, a, b, n):
    x = np.linspace(a, b, n+1)
    dx = (b - a) / n
    print(f"No of subinterval: {n} ")
    print(f"Subinterval length: {dx} ")
    upper_sum = np.sum(func(x[1:]) * dx) # all elements except first one
    lower_sum = np.sum(func(x[:-1]) * dx) # all elements except last one
    middle_sum = np.sum(func((x[:-1] + x[1:]) / 2) * dx)
    
    return upper_sum, middle_sum, lower_sum

# Parameters
a = 0  # Start of interval
b = 3  # End of interval
n = 192  # Number of subintervals

# Calculate Riemann sums
upper_sum, middle_sum, lower_sum = riemann_sums(function, a, b, n)

print(f"Upper sum: {upper_sum}")
print(f"Middle sum: {middle_sum}")
print(f"Lower sum: {lower_sum}")
