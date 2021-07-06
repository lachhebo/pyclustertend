import unittest

import numpy as np
from sklearn import datasets

from pyclustertend.hopkins import hopkins


class HopkinsTest(unittest.TestCase):
    def test_hopkins(self):
        """
        entry : a Dataframe D and a sampling_size
        return the hopkins statistics of the dataframe.
        """

        iris = datasets.load_iris()
        X = iris.data

        hopkins_scores = []
        for _ in range(0, 100):
            hopkins_scores.append(hopkins(X, 150))

        mean_hopkins = np.mean(hopkins_scores)

        self.assertTrue(mean_hopkins >= 0.15)
        self.assertTrue(mean_hopkins <= 0.20)


if __name__ == "__main__":
    unittest.main()
