import re

def toVertexForm(stdForm):
    # Remove whitespace and tokenize the input
    tokens = re.findall(r'([-+]?[^-+]+)', stdForm.replace(" ", ""))
    a = b = c = 0

    # check if quadratic
    x2_present = any('x^2' in token for token in tokens)
    if not x2_present:
        raise ValueError("Error: Invalid Input for x^2, Try Again")

    # Regular expressions to match coefficients
    square_term = r'([-+]?\d*\.?\d*)x\^2'
    linear_term = r'([-+]?\d*\.?\d*)x(?!\^)'
    constant_term = r'([-+]?\d*\.?\d*)$'

    # Extract coefficients
    for token in tokens:
        if 'x^2' in token:
            if token.strip() in ['-x^2', '+x^2', 'x^2']:
                a = 1 if token.strip() in ['+x^2', 'x^2'] else -1
            else:
                a = float(re.search(square_term, token).group(1))
        elif 'x' in token:
            if token.strip() in ['-x', '+x', 'x']:
                b = 1 if token.strip() in ['+x', 'x'] else -1
            else:
                b = float(re.search(linear_term, token).group(1))
        else:
            match = re.search(constant_term, token)
            if match:
                c = float(match.group(1))

    # if a = 0 invalid quadratic
    if a == 0:
        raise ValueError("x^2 == 0, No Real Solution, Try Again")

    # Convert to vertex form
    h = -b / (2 * a)
    k = c - (b ** 2) / (4 * a)

    a_str = '' if a == 1 else '-' if a == -1 else str(a)

    h = round(h, 2) if h % 1 else float(h)
    h_str = '' if h == 0 else str(abs(h))
    h_sign = '+' if h < 0 else '-'
    h_term = f"(x {h_sign} {h_str})" if h_str else "x"

    k = round(k, 2) if k % 1 else int(k)
    k_str = '' if k == 0 else f" + {k}" if k > 0 else f" - {-k}"

    vertex_form = f"{a_str}{h_term}^2{k_str}"

    return vertex_form

# Examples
std_form = "3x^2 + 2x + 1"
print(toVertexForm(std_form)) 
std_form = "x^2 - 4"
print(toVertexForm(std_form))  
std_form = "0.5x^2 + 1.5x + 0.25"
print(toVertexForm(std_form))