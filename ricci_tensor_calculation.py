import sympy as sp
from sympy import pprint, symbols, diff, Matrix
from sympy.parsing.latex import parse_latex 
# parse-latex takes a string written in LaTeX-style math and converts it into a SymPy expression


def texfy(expr): #let's define a function that takes a LaTeX string and returns a SymPy expression
    try:
        return parse_latex(expr)
    except Exception as exc:
        raise ValueError("Please enter a valid LaTeX expression.") from exc
    

# DIMENSION OF THE SPACETIME
while True:
    try:
        d = int(input("Enter the number of dimensions of your spacetime (integer) : d = "))

        if d>0:
            break
        else:
            print("d must be a positive integer greter than 0")
    
    except ValueError:
        print("Please, enter an integer")

# COORDINATES
x_mu = sp.Matrix.zeros(d,1)

print("Now, let's define your coordinates. Please enter them one by one in LaTeX format (e.g., t, r, \\theta, \\phi).")
for i in range(d):
    x_mu[i] = texfy((input(f'x**{i} = ')))
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
            g[mu, nu] = texfy(input(f"g[{mu},{nu}] = "))
            g[nu, mu] = g[mu, nu]  # Imposing symmetry of the metric tensor
        else:
          print("mu and nu must be integers between 0 and", d)

    except ValueError:
        print("")
        print("g_{mu nu} = ")
        print("")
        pprint(g)
        break


