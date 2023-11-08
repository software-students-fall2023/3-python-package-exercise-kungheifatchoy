# Pyquadratic

![Python build & test](https://github.com/software-students-fall2023/3-python-package-exercise-kungheifatchoy/actions/workflows/python-package.yml/badge.svg)


## Description

#### A python package designed to facilitate the solving and manipulation of quadratic equations.

### `simplifyQuadratic()`

Returns a simplified quadratic functions from the given input quadratic function.

#### Parameters

| Parameter | Type | Values            |
|-----------|------|-------------------|
| stdForm   | `str`  | "2x^2+8x+2"    | 

#### Return type
`str`

#### Errors

- If the `stdForm` value provided is not in the correct format a, `Value Error` exception is raised. 

### `realSolution()`

Returns the solutions for a quadratic equation entered in the format ax^2+bx+c

#### Parameters

| Parameter | Type | Values            |
|-----------|------|-------------------|
| stdForm  | `str`  |"2x^2+8x+2"  | 


#### Return type
`float[2]` or `int[2]`

#### Errors

- If the `stdForm` value provided is not in the correct format, a `Value Error` exception is raised. 
- If a real solution does not exist, a `Value Error` exception is raised. 

### `toFactoredForm()`

Returns the factored form of the corresponding standard form of quadratic equation

#### Parameters

| Parameter | Type | Values            |
|-----------|------|-------------------|
| stdForm  | `str`  |"2x^2+8x+2"  | 


#### Return type
`str`

#### Errors

- If the `stdForm` value provided is not in the correct format, a `Value Error` exception is raised. 
- If a real solution does not exist, a `Value Error` exception is raised. 

### `toVertexForm()`

Returns the vertex form of the corresponding standard form of quadratic equation

#### Parameters

| Parameter | Type | Values            |
|-----------|------|-------------------|
| stdForm  | `str`  |"2x^2+8x+2" | 


#### Return type
`str`

#### Errors

- If the `stdForm` value provided is not in the correct format, a `Value Error` exception is raised. 

### `pyquadratic._readString()` (<span style="color: red;">Private: for contributors only</span>)

Returns the coefficients for an ax^2+bx+c string of a quadratic equation

#### Parameters

| Parameter | Type | Values            |
|-----------|------|-------------------|
| stdForm  | str  |"2x^2+8x+2"  | 


#### Return type
`float[3]` or `int[3]`

#### Errors

- If the `stdForm` value provided is not in the correct format, a `Value Error` exception is raised. 

## Instructions

Use the standard form `ax^2+bx+c` to use pyquadratic functions (Always assume = 0)
### How to import:

Go to terminal and run:
`pip install pyquadratic`

In your python file, be sure to include: 

`from pyquadratic.pyquadratic import *`

Now you will be able to use the functions included in the pyquadratic package!

[Example Code](https://github.com/software-students-fall2023/3-python-package-exercise-kungheifatchoy/blob/main/example.py)

### How to Contribute to the Project:

#### How to Set Up the Virtual Environment

* Fork the Repository.

* Clone it to your local directory.

* Go to terminal, locate the project directory, and run:  `pip install pipenv`.

* Run `pipenv shell` to activate the virtual environment.

* Run `pipenv install` to install all the required dependencies for developemnt.

#### How to Build

* Before every build, make sure you delete `dist` and `pyquadratic.egg-info` 
directory.

* Update version number in `pyproject.toml` if approved.
* Go to terminal, locate the project directory, and run:  `python -m build` or `python3 -m build`.

#### How to Test

* Go to terminal, locate the project directory, and run:  `pytest`.

## Team Members

Nicolas Izurieta: https://github.com/ni2050

Patrick Zhao: https://github.com/PatrickZhao0

Brad Yin: https://github.com/BREADLuVER

Yucheng Xu: https://github.com/Yucheng-XPH


## Link to Package

https://pypi.org/project/pyquadratic/

