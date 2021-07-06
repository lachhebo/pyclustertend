import numpy as np
import pytest
from sklearn import datasets
from pyclustertend import (
    assess_tendency_by_metric,
    assess_tendency_by_mean_metric_score,
)

from unittest.mock import patch, call


@pytest.mark.parametrize(
    "metric", ["silhouette", "calinski_harabasz", "davies_bouldin"]
)
def test_assess_tendency_by_metric_return_the_max_cluster_score_and_the_scores_of_each_value(
    metric,
):
    # given
    iris = datasets.load_iris()
    iris_dataset = iris.data

    # when
    best_cluster, silhouette_score_array = assess_tendency_by_metric(
        iris_dataset, metric=metric
    )

    # then
    if metric == "davies_bouldin":
        assert np.argmin(silhouette_score_array) + 2 == best_cluster
    else:
        assert np.argmax(silhouette_score_array) + 2 == best_cluster


@patch("pyclustertend.metric.assess_tendency_by_metric", return_value=(1, [0.4, 0.6]))
def test_assess_tendency_by_mean_metric_score_return_the_mean_value_of_best_cluster_for_each_methods(
    mock_assess_tendency_by_metric,
):
    # given
    iris = datasets.load_iris()
    iris_dataset = iris.data

    # when
    assess_tendency_by_mean_metric_score(iris_dataset)

    # then

    mock_assess_tendency_by_metric.assert_has_calls(
        [
            call(iris_dataset, n_cluster=10, metric="silhouette", random_state=None),
            call(
                iris_dataset,
                n_cluster=10,
                metric="calinski_harabasz",
                random_state=None,
            ),
            call(
                iris_dataset, n_cluster=10, metric="davies_bouldin", random_state=None
            ),
        ]
    )
