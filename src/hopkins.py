from scikit-learn import BallTree



class Hopkins(): 


    self.sampling_size = None

    def __init__():
        pass

    
    def do_sampling(D,sample_size): 
        '''
        return n sample from D : 
        '''
        pass
    

    def do_neirest_neigbbors(P):
        '''
        return an array X containing the distance between P points and their
        neirest neigbors in D
        '''
        pass

    def do_simulate_points(sample_size):
        '''
        return n sample from a simulate dataset
        '''
        pass

    def do_neirest_neigbbors(Q):
        '''
        return an array Y containing the distance between q points and their
        neirest neigbors in D
        '''
        pass

    def evaluate_hopkins(X,Y):
        '''
        return the Hopkins score
        '''

        numerator = sum(Y)
        denominator = sum(X) + sum(Y)

        return numerator/denominator


    def __main__(D,sampling_size):

        P = do_sampling(D,sampling_size)
        X = do_neirest_neigbbors(P)
        Q = do_simulate_points(sampling_size)
        Y = do_neirest_neigbbors(Q)


        return evaluate_hopkins(X,Y)



    
