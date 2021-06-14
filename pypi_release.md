# Release Instructions:

1. delete the dist/ folder if it exists
1. make sure your virtual environment is activated then run these commands:

Then:


```
pip install --upgrade -r requirements.txt
python -m build
```

Upload to PyPi test:

```
python -m twine upload --repository testpypi dist/*
```

Test by downloading the repository into a clean virtual environment
```
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps frolic-engine
```

If everything downloaded fine
upload to PyPi production:

```
python -m twine upload dist/*
```
