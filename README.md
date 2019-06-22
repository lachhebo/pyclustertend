# pyclustertend [![Build Status](https://travis-ci.com/lachhebo/pyclustertend.svg?branch=master)](https://travis-ci.com/lachhebo/pyclustertend)

## Presentation : 

pyclustertend is a python package to do cluster tendency evaluation. Clustertendency consist to check if clusters exist in the data.

One method for assessing cluster tendency is currently implemented  :

- [x] Hopkins Statistics 

## Usage : 

```python
    from sklearn import datasets
    from pyclustertend import hopkins

    X = datasets.load_iris().data
    hopkins(X,150)
```
