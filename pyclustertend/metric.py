from sklearn.metrics import silhouette_score, calinski_harabaz_score, davies_bouldin_score
from sklearn.cluster import KMeans, Birch

import numpy as np


def assess_tendency_silhouette(X, max_nb_cluster=10, random_state=None):
    """Assess the clusterability of a dataset using KMeans algorithm and the silhouette score, the best cluster number is the number that best scored with the silhouette score. 

    Parameters
    ----------
    X : numpy array, DataFrame
        The input dataset
    max_nb_cluster : int
        The maxium number of cluster to consider
    random_state : int (default to None)

    Returns
    ---------------------
    (n_clusters, value) :  n_clusters is the number of cluster that best scored on the silhouette score on Kmeans. As for value, it is the silhouette score for each number of cluster on KMeans.

    Examples
    --------
    >>> from sklearn import datasets
    >>> from pyclustertend import assess_tendency_silhouette
    >>> X = datasets.load_boston().data
    >>> assess_tendency_silhouette(X,10)
    (3, array([0.69140457, 0.72342825, 0.5682447 , 0.5707678 , 0.50128812,
        0.50793465, 0.46238188, 0.47375595, 0.46244695]))

    """

    result_kmeans = np.array([])

    for k_cluster in range(2, max_nb_cluster+1):

        labels = KMeans(n_clusters=k_cluster,
                        random_state=random_state).fit_predict(X)
        result_kmeans = np.append(result_kmeans, silhouette_score(X, labels))

    return np.argmax(result_kmeans) + 2, result_kmeans


def assess_tendency_calinski_harabaz(X, max_nb_cluster=10, random_state=None):
    """Assess the clusterability of a dataset using KMeans algorithm and the calinski_harabaz score, the best cluster number is the number that best scored with the calinski_harabaz score. 

    Parameters
    ----------
    X : numpy array, DataFrame
        The input dataset
    max_nb_cluster : int
        The maxium number of cluster to consider
    random_state : int (default to None)

    Returns
    ---------------------
    (n_clusters, value) :  n_clusters is the number of cluster that best scored on the calinski_harabaz score on Kmeans. As for value, it is the calinski_harabaz score for each number of cluster on KMeans.

    Examples
    --------
    >>> from sklearn import datasets
    >>> from pyclustertend import assess_tendency_silhouette
    >>> X = datasets.load_boston().data
    >>> assess_tendency_calinski_harabaz(X,10)
    (3, array([0.69140457, 0.72342825, 0.5682447 , 0.5707678 , 0.50128812,
        0.50793465, 0.46238188, 0.47375595, 0.46244695]))

    """
    result_kmeans = np.array([])

    for k_cluster in range(2, max_nb_cluster+1):

        labels = KMeans(n_clusters=k_cluster,
                        random_state=random_state).fit_predict(X)
        result_kmeans = np.append(
            result_kmeans, calinski_harabaz_score(X, labels))

    return np.argmax(result_kmeans) + 2, result_kmeans


def assess_tendency_davies_bouldin(X, max_nb_cluster=10, random_state=None):
    """Assess the clusterability of a dataset using KMeans algorithm and the davies_bouldin score, the best cluster number is the number that best scored with the davies_bouldin score. 

    Parameters
    ----------
    X : numpy array, DataFrame
        The input dataset
    max_nb_cluster : int
        The maxium number of cluster to consider
    random_state : int (default to None)

    Returns
    ---------------------
    (n_clusters, value) :  n_clusters is the number of cluster that best scored on the davies_bouldin score on Kmeans. As for value, it is the davies_bouldin score for each number of cluster on KMeans.

    Examples
    --------
    >>> from sklearn import datasets
    >>> from pyclustertend import assess_tendency_silhouette
    >>> X = datasets.load_boston().data
    >>> assess_tendency_davies_bouldin(X,10)
    (3, array([0.69140457, 0.72342825, 0.5682447 , 0.5707678 , 0.50128812,
        0.50793465, 0.46238188, 0.47375595, 0.46244695]))

    """
    result_kmeans = np.array([])

    for k_cluster in range(2, max_nb_cluster+1):

        labels = KMeans(n_clusters=k_cluster,
                        random_state=random_state).fit_predict(X)
        result_kmeans = np.append(
            result_kmeans, davies_bouldin_score(X, labels))

    return np.argmin(result_kmeans) + 2, result_kmeans



def assess_tendency_by_metrics(X, max_nb_cluster=10, random_state=None):


    silhouette_best, _ = assess_tendency_silhouette(X, max_nb_cluster= max_nb_cluster, random_state= random_state)
    calinski_best, _   = assess_tendency_calinski_harabaz(X, max_nb_cluster= max_nb_cluster, random_state= random_state)
    davies_best, _     = assess_tendency_davies_bouldin(X, max_nb_cluster= max_nb_cluster, random_state= random_state)

    return np.mean([silhouette_best, calinski_best, davies_best])

