# pyclustertend [![Build Status](https://travis-ci.com/lachhebo/pyclustertend.svg?branch=master)](https://travis-ci.com/lachhebo/pyclustertend)

## Presentation : 

pyclustertend is a python package to do cluster tendency. Cluster tendency consist to assess if clustering algorithm are relevant for a dataset.

One method for assessing cluster tendency is currently implemented  :

- [x] Hopkins Statistics 

## Installation : 

```shell
    pip install pyclustertend
```

## Usage : 

```python
    from sklearn import datasets
    from pyclustertend import hopkins

    X = datasets.load_iris().data
    hopkins(X,150)
```
