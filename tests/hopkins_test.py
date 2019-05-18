import unittest


class HopkinsTest(unittest.TestCase):


    def test_do_sampling(self,D,sampling_size): 
        '''
        Entry : D, sampling size
        Return a sample of D of size sampling_size
        '''
        pass


    def test_do_neirest_neigbbors(self,P,D):
        '''
        entry : DataFrame P and D
        return an array of double containing the distance of the NN of P in D
        '''
        pass


    def test_do_simulate_points(self,sampling_size):
        '''
        entry sampling_size and Dataframe D
        return an simulated (uniform) Dataframe with sampling_size column and the same variation as D
        '''
        pass

    def test_evaluate_hopkins(self,X,Y):
        '''
        entry : two dataframe X and Y
        return the sum(X)/(sum(X)+sum(Y))
        '''
        pass

    def test_eval(self,D,sampling_size): 
        '''
        entry : a Dataframe D and a sampling_size 
        return the hopkins statistics of the dataframe.
        '''
        pass

if __name__ == '__main__':
    unittest.main()