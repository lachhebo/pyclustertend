# pyclustertend

[![Build Status](https://travis-ci.com/lachhebo/pyclustertend.svg?branch=master)](https://travis-ci.com/lachhebo/pyclustertend)  [![PyPi Status](https://img.shields.io/pypi/v/pyclustertend.svg?color=brightgreen)](https://pypi.org/project/pyclustertend/) [![Documentation Status](https://readthedocs.org/projects/pyclustertend/badge/?version=master)](https://pyclustertend.readthedocs.io/en/master/) [![Downloads](https://pepy.tech/badge/pyclustertend)](https://pepy.tech/project/pyclustertend) [![codecov](https://codecov.io/gh/lachhebo/pyclustertend/branch/master/graph/badge.svg)](https://codecov.io/gh/lachhebo/pyclustertend)
[![DOI](https://zenodo.org/badge/187477036.svg)](https://zenodo.org/badge/latestdoi/187477036)

pyclustertend is a Python package specialized in cluster tendency. Cluster tendency consist to assess if clustering algorithms are relevant for a dataset.

Three methods for assessing cluster tendency are currently implemented and one additional method based on metrics obtained with a KMeans estimator:
- Hopkins Statistics [^1]
- VAT [^5]
- iVAT [^6]
- Metric based method (Silhouette [^2], Calinski-Harabasz [^3], Davies-Bouldin [^4])

## Installation
<!-- To install the Python 3.14 compatible version of `pyclustertend`, you can use `pip` to install directly from the GitHub repository. Run the following command in your terminal:
```shell
pip install git+https://github.com/Alessi0X/pyclustertend-fork.git@upgrade-python-3.14
```
or, for the Python 3.13 compatible version:
```shell
pip install git+https://github.com/Alessi0X/pyclustertend-fork.git@upgrade-python-3.13
```
For info about the branches, please refer to the [Acknowledgments](#acknowledgments) section below. -->
The package is available on PyPi and can be installed using `pip`:
```shell
pip install pyclustertend
```

## Usage

### Example Hopkins

```python
    >>> from sklearn import datasets
    >>> from pyclustertend import hopkins
    >>> from sklearn.preprocessing import scale
    >>> X = scale(datasets.load_iris().data)
    >>> hopkins(X,150)
    0.18950453452838564
```

### Example VAT

```python
    >>> from sklearn import datasets
    >>> from pyclustertend import vat
    >>> from sklearn.preprocessing import scale
    >>> X = scale(datasets.load_iris().data)
    >>> vat(X)
```

<img height="350" src="https://raw.githubusercontent.com/lachhebo/pyclustertend/screenshots/vat.png" />

### Example iVat

```python
    >>> from sklearn import datasets
    >>> from pyclustertend import ivat
    >>> from sklearn.preprocessing import scale
    >>> X = scale(datasets.load_iris().data)
    >>> ivat(X)
```

<img height="350" src="https://raw.githubusercontent.com/lachhebo/pyclustertend/screenshots/ivat.png" />

## Notes

It's preferable to scale the data before using hopkins or vat algorithm as they use distance between observations. Moreover, vat and ivat algorithms
do not really fit to massive databases. A first solution is to sample the data before using those algorithms. 

<!-- ## Acknowledgments

This is a fork of the original [pyclustertend](https://github.com/lachhebo/pyclustertend) library by [Ismaïl Lachheb](https://github.com/lachhebo). The original library got somehow abandoned, and I decided to fork it and continue its development, especially in terms of compatibility with the latest versions of Python. This fork is structured as follows:
- The original codebase is preserved in the `master` branch
- The `upgrade-python-3.13` branch features updates to ensure compatibility with Python 3.13
- The `upgrade-python-3.14` branch includes further updates for compatibility with Python 3.14

Shout-out to Ismaïl Lachheb for creating the original `pyclustertend` library! -->


[^1]: Hopkins, Brian; Skellam, J.G. (1954). "A new method for determining the type of distribution of plant individuals". _Annals of Botany_. **18** (2). Annals Botany Co: 213–227. doi:10.1093/oxfordjournals.aob.a083391

[^2]: Rousseeuw, Peter J. (1987). "Silhouettes: a Graphical Aid to the Interpretation and Validation of Cluster Analysis". _Computational and Applied Mathematics_. **20**: 53–65. doi:10.1016/0377-0427(87)90125-7.

[^3]: Caliński, Tadeusz; Harabasz, Jerzy (1974). "A dendrite method for cluster analysis". _Communications in Statistics_. **3** (1): 1–27. doi:10.1080/03610927408827101

[^4]: Davies, David L.; Bouldin, Donald W. (1979). "A Cluster Separation Measure". _IEEE Transactions on Pattern Analysis and Machine Intelligence_. PAMI-1 (2): 224–227. doi:10.1109/TPAMI.1979.4766909

[^5]: Bezdek, James C.; Hathaway, Richard J. (2002). "VAT: A Tool for Visual Assessment of (Cluster) Tendency". _Proceedings of the 2002 International Joint Conference on Neural Networks_. IJCNN '02. IEEE Computer Society. pp. 2225–2230. doi:10.1109/IJCNN.2002.1007487.

[^6]: Wang, L., Nguyen, U. T., Bezdek, J. C., Leckie, C. A., Ramamohanarao, K. (2010). "iVAT and aVAT: enhanced visual analysis for cluster tendency assessment". In _Advances in Knowledge Discovery and Data Mining. PAKDD 2010_ (pp. 16-27). Berlin, Heidelberg: Springer Berlin Heidelberg. doi:10.1007/978-3-642-13657-3_5.