import random
from pathlib import Path
from unittest.mock import patch

import numpy as np
from sklearn import datasets
from sklearn.preprocessing import scale

from pyclustertend.visual_assessment_of_tendency import (
    vat,
    ivat,
    compute_ordered_dissimilarity_matrix,
    compute_ivat_ordered_dissimilarity_matrix,
)

TEST_DIR = Path(__file__).resolve().parent


def test_compute_ordered_dissimilarity_matrix():
    # given
    random.seed(42)
    np.random.seed(42)
    iris = datasets.load_iris()
    iris_dataset = iris.data
    expected_ordered_matrix = np.load(TEST_DIR / "data/iris_vat.npy")

    # when
    ordered_matrix = compute_ordered_dissimilarity_matrix(iris_dataset)

    # then
    np.testing.assert_allclose(ordered_matrix, expected_ordered_matrix, atol=0.3)


@patch(
    "pyclustertend.visual_assessment_of_tendency.compute_ivat_ordered_dissimilarity_matrix"
)
def test_ivat_call_compute_ivat_ordered_dissimilarity_matrix_to_obtain_the_ordered_matrix(
    mock_compute_ivat,
):
    # given
    random.seed(42)
    iris = datasets.load_iris()
    iris_dataset = iris.data
    np.random.seed(42)
    mock_compute_ivat.return_value = np.ones((3, 3))

    # when
    ivat(iris_dataset)

    # then
    mock_compute_ivat.assert_called_once_with(iris_dataset)


@patch(
    "pyclustertend.visual_assessment_of_tendency.compute_ordered_dissimilarity_matrix"
)
def test_vat_call_compute_ivat_ordered_dissimilarity_matrix_to_obtain_the_ordered_matrix(
    mock_compute_vat,
):
    # given
    random.seed(42)
    np.random.seed(42)
    iris = datasets.load_iris()
    iris_dataset = iris.data
    mock_compute_vat.return_value = np.ones((3, 3))

    # when
    ivat(iris_dataset)

    # then
    mock_compute_vat.assert_called_once_with(iris_dataset)


@patch(
    "pyclustertend.visual_assessment_of_tendency.compute_ivat_ordered_dissimilarity_matrix"
)
def test_ivat_does_not_return_the_matrix_by_default(mock_compute_ivat):
    # given
    random.seed(42)
    np.random.seed(42)
    iris = datasets.load_iris()
    iris_dataset = iris.data
    mock_compute_ivat.return_value = np.ones((3, 3))

    # when
    output_result = ivat(iris_dataset)

    # then
    assert output_result is None


@patch(
    "pyclustertend.visual_assessment_of_tendency.compute_ordered_dissimilarity_matrix"
)
def test_vat_does_not_return_the_matrix_by_default(mock_compute_vat):
    # given
    random.seed(42)
    np.random.seed(42)
    iris = datasets.load_iris()
    iris_dataset = iris.data
    mock_compute_vat.return_value = np.ones((3, 3))

    # when
    output_result = vat(iris_dataset)

    # then
    assert output_result is None


def test_compute_ivat_ordered_dissimilarity_matrix__return_symetric_matrix():
    # given
    random.seed(42)
    np.random.seed(42)
    x = scale(datasets.load_iris().data)

    # when
    result = compute_ivat_ordered_dissimilarity_matrix(x)

    # then
    np.testing.assert_allclose(result, result.T, atol=0.01)
