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
    D = pd.read_csv('Concrete_Data_Yeh.csv')
    from pyclustertend import Hopkins
    hop = Hopkins(D,200)
    score = hop.fit()
    print(score)
```
