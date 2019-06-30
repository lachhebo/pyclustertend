import numpy as np 
from sklearn.metrics import pairwise_distances
import matplotlib.pyplot as plt


def VAT(X, plot=True): 
    """VAT means Visual assesement of tendency. basically, it allow to asses cluster tendency
    through a map based on the dissimiliraty matrix. 


    Parameters
    ----------

    X : matrix
        numpy array

    plot : plot the map
        boolean (default to True)


    Return
    -------
    
    RSM : matrix
        the permuted dissimalarity matrix plotted.

    """

    I = []

    ## dissimilarity matrix : 
    R =  pairwise_distances(X) #- np.max(pairwise_distances(X)) )
        
    P = np.zeros(R.shape[0],dtype = "int")

    ## Step 1 : Validé ! 
    
    argmax = np.argmax(R) 

    j = argmax % R.shape[1]
    i = argmax // R.shape[1]

    P[0] = i
    I.append(i)

    K = np.linspace(0, R.shape[0] - 1 ,R.shape[0] , dtype = "int")
    
    J = np.delete(K, i)
    
    ## Step 2 : 

    for r in range(1,R.shape[0]) :

        p,q = (-1, -1)
        
        mini = np.max(R)
        
        for pp in I :
            for jj in J :
                if R[pp,jj] < mini :
                    p = pp
                    q = jj
                    mini = R[pp,jj]
                
                

        if p == -1 or q == -1 :
            raise("Error Step 2")

        P[r] = q
        I.append(q)

        ind_q = np.where(np.array(J) == q)[0][0]
        J = np.delete(J,ind_q)
    
    ## Step 3 

    RDM = np.zeros(R.shape)

    for i in range(RDM.shape[0]):
        for j in range(RDM.shape[1]):
            alpha = P[i]
            beta  = P[j]
            RDM[i,j] = R[alpha,beta]

    ## Step 4 : 

    if plot == True :
        plt.imshow(RDM, cmap='gray', vmin=0, vmax=np.max(RDM))
        plt.title("VAT")
        plt.show()
    
    return RDM
