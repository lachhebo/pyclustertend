import unittest
import pandas as pd 
import numpy as np
from pyclustertend.hopkins import hopkins 
from sklearn import datasets


class HopkinsTest(unittest.TestCase):

    
    def test_hopkins(self): 
        '''
        entry : a Dataframe D and a sampling_size 
        return the hopkins statistics of the dataframe.
        '''

        iris = datasets.load_iris()
        X = iris.data

        l = []
        for _ in range (0,100):
            l.append(hopkins(X,150))
    
        
        mean_hopkins = np.mean(l)

        self.assertTrue(mean_hopkins >= 0.15)
        self.assertTrue(mean_hopkins <= 0.20)


if __name__ == '__main__':
    unittest.main()