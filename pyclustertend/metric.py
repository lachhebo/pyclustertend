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
    >>> from sklearn.preprocessing import scale
    >>> X = scale(datasets.load_boston().data)
    >>> assess_tendency_silhouette(X,10)
    (2, array([0.36011769, 0.25740335, 0.28098046, 0.28781574, 0.26746932,
        0.26975514, 0.27155699, 0.28883395, 0.29028124]))

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
    >>> from pyclustertend import assess_tendency_calinski_harabaz
    >>> from sklearn.preprocessing import scale
    >>> X = scale(datasets.load_boston().data)
    >>> assess_tendency_calinski_harabaz(X,10)
    (2, array([286.08249447, 219.25073844, 187.90633666, 176.54408944,
        169.44923471, 163.29755259, 160.66682836, 158.65038162,
        151.76885495]))

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
    >>> from pyclustertend import assess_tendency_davies_bouldin
    >>> from sklearn.preprocessing import scale
    >>> X = scale(datasets.load_boston().data)
    >>> assess_tendency_davies_bouldin(X,10)
    (9, array([1.19025242, 1.31822679, 1.171196  , 1.24124198, 1.23071422,
        1.23071946, 1.24731647, 1.10070805, 1.16275418]))

    """
    result_kmeans = np.array([])

    for k_cluster in range(2, max_nb_cluster+1):

        labels = KMeans(n_clusters=k_cluster,
                        random_state=random_state).fit_predict(X)
        result_kmeans = np.append(
            result_kmeans, davies_bouldin_score(X, labels))

    return np.argmin(result_kmeans) + 2, result_kmeans

def assess_tendency_by_metrics(X, max_nb_cluster=10, random_state=None):
    """Assess the clusterability of a dataset using KMeans algorithm and the silhouette, calinski and davies bouldin score, the best cluster number is the mean of the result of the three methods. 

    Parameters
    ----------
    X : numpy array, DataFrame
        The input dataset
    max_nb_cluster : int
        The maxium number of cluster to consider
    random_state : int (default to None)

    Returns
    ---------------------
    n_clusters :  n_clusters is the mean of the best number of cluster score (with Kmeans algorithm)

    Examples
    --------
    >>> from sklearn import datasets
    >>> from pyclustertend import assess_tendency_by_metrics
    >>> from sklearn.preprocessing import scale
    >>> X = scale(datasets.load_boston().data)
    >>> assess_tendency_by_metrics(X,10)
    2.6666666666666665
    """


    silhouette_best, _ = assess_tendency_silhouette(X, max_nb_cluster= max_nb_cluster, random_state= random_state)
    calinski_best, _   = assess_tendency_calinski_harabaz(X, max_nb_cluster= max_nb_cluster, random_state= random_state)
    davies_best, _     = assess_tendency_davies_bouldin(X, max_nb_cluster= max_nb_cluster, random_state= random_state)

    return np.mean([silhouette_best, calinski_best, davies_best])

