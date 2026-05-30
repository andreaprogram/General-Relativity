import sympy as sp
from sympy import pprint, symbols, diff, Matrix

# DIMENSION OF THE SPACETIME
while True:
    try:
        d = int(input("Enter the number of dimensions of your spacetime (integer) : d = "))

        if d>0:
            break
        else:
            print("d must be a positive integer greter than 0")
    
    except ValueError:
        print(" Please, enter an integer")

# COORDINATES
x_mu = sp.Matrix.zeros(d,1)

print("Now, let's define your coordinates. Please enter them one by one in LaTeX format (e.g., t, r, \\theta, \\phi).")
for i in range(d):
    x_mu[i] = sp.symbols(input(f'x**{i} = '))
#print(x_mu)

# METRIC TENSOR 
g = sp.Matrix.zeros(d,d)


print("Please enter the non-zero components of your metric one by one" \
" if you are done, enter any other character for mu and nu")

while True:
    try:
        mu = int(input("mu = "))
        nu = int(input("nu = "))

        if 0 <= mu < d and 0 <= nu < d:
            g[mu, nu] = sp.sympify(input(f"g[{mu},{nu}] = "))
            g[nu, mu] = g[mu, nu]  # Imposing symmetry of the metric tensor
        else:
          print("mu and nu must be integers between 0 and", d)

    except ValueError:
        print("")
        print("g_{mu nu} = ")
        print("")
        pprint(g)
        break


