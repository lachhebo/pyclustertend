import numpy as np
from sklearn import datasets
from pyclustertend import assess_tendency_silhouette, assess_tendency_calinski_harabaz, assess_tendency_davies_bouldin, \
    assess_tendency_by_metrics
from unittest.mock import patch


def test_assess_tendency_silhouette_return_the_max_cluster_score_and_the_scores_of_each_value():
    # given
    iris = datasets.load_iris()
    iris_dataset = iris.data

    # when
    best_cluster, silhouette_score_array = assess_tendency_silhouette(iris_dataset)

    # then
    assert np.argmax(silhouette_score_array) + 2 == best_cluster


def test_assess_tendency_calinski_harabaz_return_the_maximum_index_and_the_scores_of_each_value():
    # given
    iris = datasets.load_iris()
    iris_dataset = iris.data

    # when
    best_cluster, silhouette_score_array = assess_tendency_calinski_harabaz(iris_dataset)

    # then
    assert np.argmax(silhouette_score_array) + 2 == best_cluster


def test_assess_tendency_davies_bouldin_return_the_maximum_index_and_the_scores_of_each_value():
    # given
    iris = datasets.load_iris()
    iris_dataset = iris.data

    # when
    best_cluster, silhouette_score_array = assess_tendency_davies_bouldin(iris_dataset)

    # then
    assert np.argmin(silhouette_score_array) + 2 == best_cluster


@patch('pyclustertend.metric.assess_tendency_silhouette', return_value=(1, [0.4, 0.6]))
@patch('pyclustertend.metric.assess_tendency_calinski_harabaz', return_value=(1, [0.4, 0.6]))
@patch('pyclustertend.metric.assess_tendency_davies_bouldin', return_value=(1, [0.4, 0.6]))
def test_assess_tendency_by_metrics_return_the_mean_of_the_value_of_best_cluster_for_each_methods(mock_davies,
                                                                                                  mock_calinski,
                                                                                                  mock_silhouette):
    # given
    iris = datasets.load_iris()
    iris_dataset = iris.data

    # when
    assess_tendency_by_metrics(iris_dataset)

    # then
    mock_calinski.assert_called_once_with(iris_dataset, max_nb_cluster=10, random_state=None)
    mock_davies.assert_called_once_with(iris_dataset, max_nb_cluster=10, random_state=None)
    mock_silhouette.assert_called_once_with(iris_dataset, max_nb_cluster=10, random_state=None)
