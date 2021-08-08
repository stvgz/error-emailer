# How to Build this project and upload

## build with python build
python -m build

## (optional) test upload
twine upload --repository testpypi dist/*

## test install and uninstall if already installed

pip uninstall error-emailer-stevegao
pip install --index-url https://test.pypi.org/simple/ --no-deps error-emailer-stevegao

## test usage
import error_emailer_stevegao


# change name 
python -m build

# upload to pypi
twine upload dist/*
