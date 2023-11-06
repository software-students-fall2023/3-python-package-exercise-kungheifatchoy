import pytest
from vertex_form_function import toVertexForm

def test_to_vertex_form_handling_spaces():
    test_cases = [
        ("  x^2 + 6x + 9  ", "(x + 3.0)^2", "extra spaces with simple quadratic"),
        ("  1x^2   + 2x   + 1  ", "(x + 1.0)^2", "irregular spaces between coefficients")
    ]

    for expression, expected, msg in test_cases:
        actual = toVertexForm(expression)
        assert actual == expected, f"Input: '{expression}'; Expected: '{expected}', got: '{actual}' for case: {msg}"

def test_to_vertex_form_various_coefficients():
    test_cases = [
        ("1x^2 + 0x + 4", "x^2 + 4", "no x term and zero linear coefficient"),
        ("-x^2 - 6x - 9", "-(x + 3.0)^2", "negative coefficients"),
        ("0.5x^2 + 1.5x + 0.25", "0.5(x + 1.5)^2 - 0.88", "fractional coefficients"),
        ("x^2 + x + 1", "(x + 0.5)^2 + 0.75", "unitary quadratic coefficient"),
        ("x^2 + x", "(x + 0.5)^2 - 0.25", "no constant term"),
        ("1000x^2 + 2000x + 1000", "1000.0(x + 1.0)^2", "large coefficients"),
        ("x^2 - 4", "x^2 - 4", "no x term"),
        ("3x^2 + 3x + 1", "3.0(x + 0.5)^2 + 0.25", "positive coefficients")
    ]

    for expression, expected, msg in test_cases:
        actual = toVertexForm(expression)
        assert actual == expected, f"Input: '{expression}'; Expected: '{expected}', got: '{actual}' for case: {msg}"

def test_vertex_form_invalid_inputs():
    with pytest.raises(ValueError):
        toVertexForm("0x^2 + 2x + 3")

    with pytest.raises(ValueError):
        toVertexForm("b^2-4ac")

    with pytest.raises(ValueError):
        toVertexForm("0x^2 + 0x + 5")

    with pytest.raises(ValueError):
        toVertexForm("0x^2 + 0x + 0")

    with pytest.raises(ValueError):
        toVertexForm("2x^4 + 2x + 1")
