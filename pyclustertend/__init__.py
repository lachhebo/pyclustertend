# -*- coding: utf-8 -*-
name = "pyclustertend"

from .hopkins import hopkins
from .VAT import vat, ordered_dissimilarity_matrix
from .metric import assess_tendency_silhouette, assess_tendency_calinski_harabaz, assess_tendency_davies_bouldin, assess_tendency_by_metrics


# TODO: add version information here
#from . import metrics
#__all__ = ['metrics']
