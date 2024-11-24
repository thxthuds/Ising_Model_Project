import numpy as np

lattice = np.array([
    [1, 1, 1],
    [-1, -1, -1],
    [-1, -1, -1]
])

prob = np.array([
    [0.5, 0.5, 0.5],
    [0.5, 0.5, 0.5],
    [0.8, 0.8, 0.8]
])

X_prob_c = np.exp(- lattice)
print(X_prob_c)

# new = lattice.copy()
# new[(lattice < 0) & (prob < 0.6)] = 0


# print(lattice)
# print(new)

# add = lattice + prob
# print(add)

# print()
# print()

# row = lattice[0]
# probrow = prob[0]
# newrow = row.copy()
# newrow[probrow < 0.6] = 0
# print(row)
# print(newrow)


# np.random.seed(0)
# size = (3, 3)

# # X_lattice = np.random.choice([-1, 1], size=size)
# X_lattice = np.array([
#     [1, 1, 1],
#     [-1, -1, -1],
#     [-1, -1, -1]
# ])
# # X_result = X_lattice.copy()
# X_deltaE = - X_lattice
# # If deltaE < 0 (spin is currently down), flip up.
# X_lattice[X_deltaE < 0] = 1

# # If deltaE > 0 (spin is currently up), flip down with probability
# # given by Boltzmann factor.
# X_prob = np.random.rand(*X_lattice.shape)
# X_lattice[(X_deltaE > 0) & (X_prob < 0.6)] = -1

# print(X_lattice)
# print("energy")
# print(X_deltaE)
# print()
# print("prob")
# print(X_prob)
# print()
# print(X_lattice)