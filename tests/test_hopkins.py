import unittest
import numpy as np
from pyclustertend.hopkins import hopkins
from sklearn import datasets


class HopkinsTest(unittest.TestCase):

    def test_hopkins(self):
        iris = datasets.load_iris()
        iris_dataset = iris.data

        hopkins_scores = []
        for _ in range(0, 100):
            hopkins_scores.append(hopkins(iris_dataset, 150))

        mean_hopkins = np.mean(hopkins_scores)

        self.assertTrue(mean_hopkins >= 0.15)
        self.assertTrue(mean_hopkins <= 0.20)


if __name__ == '__main__':
    unittest.main()
