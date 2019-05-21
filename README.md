# pyclustertend [![Build Status](https://travis-ci.com/lachhebo/pyclustertend.svg?branch=master)](https://travis-ci.com/lachhebo/pyclustertend)

## Presentation : 

pyclustertend is a python package to do cluster tendency evaluation. Clustertendency consist to check if clusters exist in the data.

One method for assessing cluster tendency is currently implemented  :

- [x] Hopkins Statistics 

## Usage : 

```python
    D = pd.read_csv('Concrete_Data_Yeh.csv')
    from pyclustertend import Hopkins
    hop = Hopkins(D,200)
```
