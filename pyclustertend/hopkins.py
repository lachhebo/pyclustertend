from sklearn.neighbors import BallTree
import numpy as np
from random import sample
from numpy.random import uniform 
import pandas as pd


class Hopkins: 

    def __init__(self, f, s):
        self.D = f 
        self.sampling_size = s 
    
    def do_sampling(self,D,sample_size): 
        '''
        return n sample from D 
        '''
        if sample_size > D.shape[0]:
            raise Exception('The number of sample of sample is superieur than the shape of D')

        P = D.sample(n= sample_size)

        return P

    def do_neirest_neigbbors(self,P,D,first):
        '''
        return an array X containing the distance between P points and their
        neirest neigbors in D
        '''
        
        tree = BallTree(D,leaf_size=2)

        dist, _ = tree.query(P, k=first)

        if first == 2 : 
            return dist[:,1]
        else :
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

        x = sum(X)
        y = sum(Y)

        if (x+y == 0):
            raise Exception('The denominator of the hopkins statistics is null')

        return x/(x+y)


    def evalue(self):

        P = self.do_sampling(self.D, self.sampling_size)
        X = self.do_neirest_neigbbors(P,self.D,2)
        Q = self.do_simulate_points(self.D,self.sampling_size)
        Y = self.do_neirest_neigbbors(Q,self.D,1)

        return self.evaluate_hopkins(X,Y)



