# -*- coding: utf-8 -*-
name = "pyclustertend"

from .hopkins import hopkins
from .visual_assessment_of_tendency import vat, compute_ordered_dissimilarity_matrix, ivat, \
    compute_ivat_ordered_dissimilarity_matrix
from .metric import assess_tendency_by_mean_metric_score, assess_tendency_by_metric
