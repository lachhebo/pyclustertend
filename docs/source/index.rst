.. pyclustertend documentation master file, created by
   sphinx-quickstart on Mon Jun 24 22:17:12 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyclustertend's documentation!
=========================================



**Deployment & Documentation & Stats**


.. image:: https://img.shields.io/pypi/v/pyclustertend.svg?color=brightgreen
   :target: https://pypi.org/project/pyclustertend/
   :alt: PyPI version

.. image:: https://readthedocs.org/projects/pyclustertend/badge/?version=latest
   :target: https://pyclustertend.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

image:: https://img.shields.io/github/stars/lachhebo/pyclustertend.svg
   :target: https://github.com/lachhebo/pyclustertend/stargazers
   :alt: GitHub stars

.. image:: https://img.shields.io/github/forks/lachhebo/pyclustertend.svg?color=blue
   :target: https://github.com/lachhebo/pyclustertend/network
   :alt: GitHub forks

**Build Status & Coverage & Maintainability & License**

.. image:: https://travis-ci.com/lachhebo/pyclustertend.svg?branch=master
   :target: https://travis-ci.com/lachhebo/pyclustertend
   :alt: Build Status



pyclustertend is a **Python toolkit** for **assessing cluster tendency**. Cluster tendency is 
about discovering the existence of cluster's in multivariate data. (link to wikipedia)



**Note on Python 2.7**\ :


The python package is not available in python 2 and only tested on Linux for the moments.



**API Demo**\ :


.. code-block:: python

    from sklearn import datasets
    from pyclustertend import hopkins

    X = datasets.load_iris().data
    hopkins(X,150)



**Key Links and Resources**\ :

* `View the latest codes on Github <https://github.com/lachhebo/pyclustertend>`_




.. toctree::
   :maxdepth: 2
   :caption: Contents:


.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Documentation

   pyclustertend




.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Additional Information

   about


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
