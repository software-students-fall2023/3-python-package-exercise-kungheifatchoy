from .pyquadratic import *

def main():
    eq = "2x^2-4x+2"
    print("Original Equation: " + eq)
    eq = simplifyQuadratic(eq)
    print("Simplified Equation: " + eq)
    vertex_form = toVertexForm(eq)
    factored_form = toFactoredForm(eq)
    print("Vertex Form: " + vertex_form)
    print("Factored Form: " + factored_form)
    real_solution = realSolution(eq)
    print("Solution: x_1 = " + str(real_solution[0]) + "; x_2 = " + str(real_solution[1]))

if __name__ == '__main__':
    main()