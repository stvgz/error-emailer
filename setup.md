# How to Build this project and upload

Introduce how to build this project and upload to pypi as a package

---

## Project structure

Refer to this project 

or 

[Learn how to package your Python code for PyPI.](https://packaging.python.org/tutorials/packaging-projects/)

## build with python build

requires anaconda env with setuptools 

Run

>python -m build

under project directory


---


## (optional) Test upload to testpypi
twine upload --repository testpypi dist/*

## test install and uninstall if already installed

pip uninstall error-emailer-stevegao
pip install --index-url https://test.pypi.org/simple/ --no-deps error-emailer-stevegao


## Test usage in python

>import error_emailer_stevegao


---

## Upload to official pypi 


> python -m build

## upload to official pypi with twine
> twine upload dist/*
