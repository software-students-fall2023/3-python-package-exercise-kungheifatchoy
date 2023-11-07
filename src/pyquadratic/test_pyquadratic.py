from .pyquadratic import *
from . import pyquadratic
import pytest

#CASE 0 - 13
def test__readString_parsing_success():
    actual = pyquadratic._readString("1x^2 + 1x + 1")
    expected = [1,1,1]
    assert actual == expected, f"CASE 0: Expected Return: {expected}; Actual Return: {actual}"  

    actual = pyquadratic._readString("x^2 + x + 1")
    expected = [1,1,1]
    assert actual == expected, f"CASE 1: Expected Return: {expected}; Actual Return: {actual}"  

    actual = pyquadratic._readString("x + 1")
    expected = [0,1,1]
    assert actual == expected, f"CASE 2: Expected Return: {expected}; Actual Return: {actual}"  

    actual = pyquadratic._readString("x^2 + x")
    expected = [1,1,0]
    assert actual == expected, f"CASE 3: Expected Return: {expected}; Actual Return: {actual}"  

    actual = pyquadratic._readString("x^2 + 1")
    expected = [1,0,1]
    assert actual == expected, f"CASE 4: Expected Return: {expected}; Actual Return: {actual}" 

    actual = pyquadratic._readString("1")
    expected = [0,0,1]
    assert actual == expected, f"CASE 5: Expected Return: {expected}; Actual Return: {actual}" 

    actual = pyquadratic._readString("x")
    expected = [0,1,0]
    assert actual == expected, f"CASE 6: Expected Return: {expected}; Actual Return: {actual}" 

    actual = pyquadratic._readString("x^2")
    expected = [1,0,0]
    assert actual == expected, f"CASE 7: Expected Return: {expected}; Actual Return: {actual}" 

    actual = pyquadratic._readString("x^2 + 1")
    expected = [1,0,1]
    assert actual == expected, f"CASE 8: Expected Return: {expected}; Actual Return: {actual}" 

    actual = pyquadratic._readString("1.1x^2 + 1.1x + 1.1")
    expected = [1.1,1.1,1.1]
    assert actual == expected, f"CASE 9: Expected Return: {expected}; Actual Return: {actual}" 

    actual = pyquadratic._readString("1.1x^2 + 1x + 1.1")
    expected = [1.1,1,1.1]
    assert actual == expected, f"CASE 10: Expected Return: {expected}; Actual Return: {actual}" 

    actual = pyquadratic._readString("1x^2+1x+1")
    expected = [1.1,1,1.1]
    assert actual == expected, f"CASE 11: Expected Return: {expected}; Actual Return: {actual}" 

    actual = pyquadratic._readString("1x^2+1x+ 1")
    expected = [1.1,1,1.1]
    assert actual == expected, f"CASE 12: Expected Return: {expected}; Actual Return: {actual}" 

    actual = pyquadratic._readString("1x^2 + 1x+1")
    expected = [1.1,1,1.1]
    assert actual == expected, f"CASE 13: Expected Return: {expected}; Actual Return: {actual}" 

    actual = pyquadratic._readString("-x^2 - x - 1")
    expected = [-1,-1,-1]
    assert actual == expected, f"CASE 1: Expected Return: {expected}; Actual Return: {actual}"  
    
    actual = pyquadratic._readString("-1x^2 - 1x - 1")
    expected = [-1,-1,-1]
    assert actual == expected, f"CASE 1: Expected Return: {expected}; Actual Return: {actual}"  

#CASE 11 - 
def test__readString_parsing_fail():
    with pytest.raises(ValueError) as msg:
        pyquadratic._readString("x^^2 + x")
    error_msg = str(msg.value)
    assert "Error: Invalid Input, Try Again" == error_msg, f"Expected Msg: Error: No Invalid Input; Actual Msg: {error_msg}"

    with pytest.raises(ValueError) as msg:
        pyquadratic._readString("x**2")
    error_msg = str(msg.value)
    assert "Error: Invalid Input, Try Again" == error_msg, f"Expected Msg: Error: No Invalid Input; Actual Msg: {error_msg}"
    
    with pytest.raises(ValueError) as msg:
        pyquadratic._readString("ax^2 + bx + c")
    error_msg = str(msg.value)
    assert "Error: Invalid Input, Try Again" == error_msg, f"Expected Msg: Error: No Invalid Input; Actual Msg: {error_msg}"

    with pytest.raises(ValueError) as msg:
        pyquadratic._readString("x+x")
    error_msg = str(msg.value)
    assert "Error: Invalid Input, Try Again" == error_msg, f"Expected Msg: Error: No Invalid Input; Actual Msg: {error_msg}"
    
def test_realSolution_real(monkeypatch):
    monkeypatch.setattr(pyquadratic, "_readString", lambda string: [1, -2, -3])
    actual = realSolution("x^2 -2x -3")
    expected = [3, -1]
    expected2 = [-1 ,3]
    assert (actual == expected or actual == expected2), f"Expected Return: {expected} or {expected2}; Actual Return {actual}"

    monkeypatch.setattr(pyquadratic, "_readString", lambda string: [1, 0, 0])
    actual = realSolution("x^2")
    expected = [0, 0]
    expected2 = [0 ,0]
    assert (actual == expected or actual == expected2), f"Expected Return: {expected} or {expected2}; Actual Return {actual}"

def test_realSolution_imaginary(monkeypatch):
    monkeypatch.setattr(pyquadratic, "_readString", lambda string: [2, 4, 5])
    with pytest.raises(ValueError) as msg:
        realSolution("2x^2 + 4x + 5")
    error_msg = str(msg.value)
    assert "Error: No Real Solution, Try Again" == error_msg, f"Expected Msg: Error: No Real Solution, Try Again; Actual Msg: {error_msg}"

def test_toFactoredForm(monkeypatch):
    monkeypatch.setattr(pyquadratic, "_readString", lambda string: [1, -5, 6])
    monkeypatch.setattr(pyquadratic, "realSolution", lambda string: [2, 3])
    actual = toFactoredForm("x^2 -5x +6")
    expected = "(x-2)(x-3)"
    assert actual == expected, f"Expected Return: {expected}; Actual Return: {actual}"

    monkeypatch.setattr(pyquadratic, "_readString", lambda string: [1, 6, 8])
    monkeypatch.setattr(pyquadratic, "realSolution", lambda string: [-2, -4])
    actual = toFactoredForm("x^2 +6x +8")
    expected = "(x+2)(x+4)"
    assert actual == expected, f"CASE 1: Expected Return: {expected}; Actual Return: {actual}"

    monkeypatch.setattr(pyquadratic, "_readString", lambda string: [2, 8, 6])
    monkeypatch.setattr(pyquadratic, "realSolution", lambda string: [-1, -3])
    actual = toFactoredForm("2x^2 +8x +6")
    expected = "2(x+1)(x+3)"
    assert actual == expected, f"CASE 1: Expected Return: {expected}; Actual Return: {actual}"
