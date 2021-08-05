import numpy as np
from sklearn import datasets

from pyclustertend.hopkins import hopkins

def test_hopkins_give_coherent_results_for_iris_dataset(self):
    iris = datasets.load_iris()
    X = iris.data

    hopkins_scores = []
    for _ in range(0, 100):
        hopkins_scores.append(hopkins(X, 150))

    mean_hopkins = np.mean(hopkins_scores)

    assert mean_hopkins >= 0.15)
    assert mean_hopkins <= 0.20)


