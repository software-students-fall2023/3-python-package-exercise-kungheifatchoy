from .pyquadratic import *

def main():
    eq = "2x^2-4x+2"
    print("Original Equation: " + eq)
    eq = simplifyQuadratic(eq)
    print("Simplified Equation: " + eq)
    vertex_form = toVertexForm(eq)
    factored_form = toFactoredForm(eq)
    print("Input: 6x^2-17x+12")
    print("Vertex Form: " + vertex_form)
    print("Factored Form: " + factored_form)
    real_solution = realSolution(eq)
    print("Solution: x_1 = " + real_solution[0] + "; x_2 = " + real_solution[1])

if __name__ == '__main__':
    main()