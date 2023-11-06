import pytest
from vertex_form_function import toVertexForm
def test_zero_linear_coefficient():
    assert toVertexForm("1x^2 + 0x + 4") == "x^2 + 4"

def test_missing_x_squared_term():
    with pytest.raises(ValueError):
        toVertexForm("0x^2 + 2x + 3")
    with pytest.raises(ValueError):
        toVertexForm("b^2-4ac")

def test_negative_coefficients():
    assert toVertexForm("-x^2 - 6x - 9") == "-(x + 3.0)^2"

def test_fractional_coefficients():
    assert toVertexForm("0.5x^2 + 1.5x + 0.25") == "0.5(x + 1.5)^2 - 0.88"

def test_coefficients_equal_one():
    assert toVertexForm("x^2 + x + 1") == "(x + 0.5)^2 + 0.75"

def test_no_constant_term():
    assert toVertexForm("x^2 + x") == "(x + 0.5)^2 - 0.25"

def test_all_zero_coefficients():
    with pytest.raises(ValueError):
        toVertexForm("0x^2 + 0x + 0")

def test_coefficients_with_spaces():
    assert toVertexForm("  1x^2   + 2x   + 1  ") == "(x + 1.0)^2"

def test_large_coefficients():
    assert toVertexForm("1000x^2 + 2000x + 1000") == "1000.0(x + 1.0)^2"

def test_only_constant_term_nonzero():
    with pytest.raises(ValueError):
        toVertexForm("0x^2 + 0x + 5")

def test_no_x_term():
    assert toVertexForm("x^2 - 4") == "x^2 - 4"

def test_positive_coefficients():
    assert toVertexForm("3x^2 + 3x + 1") == "3.0(x + 0.5)^2 + 0.25"

def test_to_vertex_form_invalid_input():
    with pytest.raises(ValueError):
        toVertexForm("2x^4 + 2x + 1")

# You can also add tests to ensure that it handles spaces properly
def test_to_vertex_form_with_spaces():
    assert toVertexForm("x^2 + 6x + 9") == "(x + 3.0)^2"
    assert toVertexForm("  x^2 + 2x + 1 ") == "(x + 1.0)^2"