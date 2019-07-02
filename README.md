# pyclustertend [![Build Status](https://travis-ci.com/lachhebo/pyclustertend.svg?branch=master)](https://travis-ci.com/lachhebo/pyclustertend)  [![PyPi Status](https://img.shields.io/pypi/v/pyclustertend.svg?color=brightgreen)](https://pypi.org/project/pyclustertend/) [![Documentation Status](https://readthedocs.org/projects/pyclustertend/badge/?version=latest)](https://pyclustertend.readthedocs.io/en/latest/?badge=latest)



## Presentation : 

pyclustertend is a python package to do cluster tendency. Cluster tendency consist to assess if clustering algorithms are relevant for a dataset.

Two methods for assessing cluster tendency are currently implemented  :

- [x] Hopkins Statistics 
- [x] VAT

## Installation : 

```shell
    pip install pyclustertend
```

## Usage : 

### Example 1 : 

```python
    from sklearn import datasets
    from pyclustertend import hopkins

    X = datasets.load_iris().data
    hopkins(X,150)
```

### Example 2 :

```python
    from sklearn import datasets
    from pyclustertend import vat

    X = datasets.load_iris().data
    vat(X,150)
```
