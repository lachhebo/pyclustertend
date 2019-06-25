from sklearn.neighbors import BallTree
import numpy as np
from random import sample
from numpy.random import uniform 
import pandas as pd


def hopkins(X, sampling_size):
    """Assess the clusterability of a dataset.

    Parameters
    ----------
    X : numpy array, DataFrame
        The input dataset 

    sampling_size : int 
        The sampling size which is used to evaluate the number of DataFrame.

    Returns
    -------
    hopkins score : float or raise errors
        The hopkins score of the dataset (between 0 and 1)

    """

    if type(X) == np.ndarray:
        X = pd.DataFrame(X)
    X = X 


    sampling_size = sampling_size
    return  fit(X, sampling_size)[0]

def do_sampling(D,sample_size): 
    '''
    return n sample from D 
    '''
    if sample_size > D.shape[0]:
        raise Exception('The number of sample of sample is superieur than the shape of D')

    P = D.sample(n= sample_size)

    return P

def do_neirest_neigbbors(P,D,first):
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

def do_simulate_points(D,sample_size):
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

def evaluate_hopkins(X,Y):
    '''
    return the Hopkins score
    '''

    x = sum(X)
    y = sum(Y)

    if (x+y == 0):
        raise Exception('The denominator of the hopkins statistics is null')

    return x/(x+y)


def fit(D, sampling_size):

    P = do_sampling(D, sampling_size)
    X = do_neirest_neigbbors(P,D,2)
    Q = do_simulate_points(D,sampling_size)
    Y = do_neirest_neigbbors(Q,D,1)

    return evaluate_hopkins(X,Y)



