import unittest
import pandas as pd 
import numpy as np
from pyclustertend import hopkins 

class HopkinsTest(unittest.TestCase):


    def test_do_sampling(self): 
        '''
        Entry : D, sampling size
        Return a sample of D of size sampling_size
        '''

        ## Arrange
        D = pd.read_csv('data/Concrete_Data_Yeh.csv')
        size = 10
        hop = hopkins.Hopkins(D,size)

        ## Act 
        P = hop.do_sampling(D, size)

        ## Assert 

        self.assertEqual(len(P),size)

    def test_do_neirest_neigbbors(self):
        '''
        entry : DataFrame P and D
        return an array of double containing the distance of the NN of P in D
        '''
        
        ## Arrange
        P = pd.read_csv('data/Concrete_Data_Yeh.csv')
        #D = pd.read_csv('data/faithful.csv')
        size = 10
        hop = hopkins.Hopkins(P,size)

        ## Act 

        NN = hop.do_neirest_neigbbors(P, P, first = 2)

        ## Assert 

        self.assertEqual(len(NN),len(P))


    def test_do_simulate_points(self):
        '''
        entry sampling_size and Dataframe D
        return an simulated (uniform) Dataframe with sampling_size column and the same variation as D
        '''
        
        ## Arrange
        D = pd.read_csv('data/Concrete_Data_Yeh.csv')
        size = 20
        hop = hopkins.Hopkins(D,size)

        ## Act 

        D_ = hop.do_simulate_points(D, size)

        ## Assert 

        self.assertEqual(len(D_),size)

        max_D = D.max()
        max_D_ = D_.max()
        min_D = D.min()
        min_D_ = D_.min()

        for i in range(0,len(D.columns)):
            self.assertTrue(max_D[i] >= max_D_[i])
            self.assertTrue(min_D[i] <= min_D_[i])


    def test_evaluate_hopkins(self):
        '''
        entry : two array X and Y
        return the sum(X)/(sum(X)+sum(Y))
        '''
        pass

    def test_eval(self): 
        '''
        entry : a Dataframe D and a sampling_size 
        return the hopkins statistics of the dataframe.
        '''
        D = pd.read_csv('data/Concrete_Data_Yeh.csv')

        hop = hopkins.Hopkins(D,200)

        l = []
        for i in range (0,20):
            l.append(hop.evalue())
    
        
        mean_hopkins = np.mean(l)
        
        self.assertTrue(mean_hopkins >= 0.08)
        self.assertTrue(mean_hopkins <= 0.09)


if __name__ == '__main__':
    unittest.main()