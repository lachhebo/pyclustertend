from sklearn.neighbors import BallTree
import numpy as np
from random import sample
from numpy.random import uniform 
import pandas as pd


class Hopkins(): 

    def __init__(self, size):
        print("méthode initialisé")
        self.size = size

    
    def do_sampling(self,D,sample_size): 
        '''
        return n sample from D 
        '''
        if sample_size > D.shape()[0]:
            raise Exception('The number of sample of sample is superieur than the shape of D')

        P = D.sample(n= sample_size)

        return P

    def do_neirest_neigbbors(self,P,D):
        '''
        return an array X containing the distance between P points and their
        neirest neigbors in D
        '''

        _tree = BallTree(D)
        dist , = _tree.query(P, k=1)
        

        return dist

    def do_simulate_points(self,D,sample_size):
        '''
        return n sample from a simulate dataset with the same variation as D
        '''
        
        max_D = D.max()
        min_D = D.min()

        matrix = np.column_stack((np.random.uniform(min_D[0],max_D[0], sample_size),np.random.uniform(min_D[1],max_D[1], sample_size)))
        if len(max_D)>=2:
            for i in range(2,len(max_D)):
                matrix = np.column_stack((matrix,np.random.uniform(min_D[i],max_D[i],sample_size)))

        df = pd.DataFrame(matrix)

        return df

    def evaluate_hopkins(self,X,Y):
        '''
        return the Hopkins score
        '''

        numerator = sum(Y)
        denominator = sum(X) + sum(Y)

        if (denominator == 0):
            raise Exception('The denominator of the hopkins statistics is null')

        return numerator/denominator


    def eval(self, D,sampling_size):

        P = self.do_sampling(D,sampling_size)
        X = self.do_neirest_neigbbors(P,D)
        Q = self.do_simulate_points(D,sampling_size)
        Y = self.do_neirest_neigbbors(Q,D)

        return self.evaluate_hopkins(X,Y)



