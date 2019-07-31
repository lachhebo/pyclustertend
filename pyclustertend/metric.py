from sklearn.metrics import silhouette_score, calinski_harabaz_score, davies_bouldin_score
from sklearn.cluster import KMeans, Birch

import numpy as np


def assess_tendency_silhouette(X, max_nb_cluster=10, random_state=None):
    """Assess the clusterability of a dataset using the number of cluster that best scored with the silhouette score using algorithm Birch and Kmeans

    Parameters
    ----------
    X : numpy array, DataFrame
        The input dataset
    max_nb_cluster : int
        The number of cluster maximum to consider
    random_state : int (default to None)

    Returns
    ---------------------
    (n_clusters, value) :  n_clusters is the number of cluster that allowed the best silhouette score on Kmeans or Birch. As for value, it is the maximum silhouette score for each number of cluster on KMeans and Birch.

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

    result_birch = np.array([])

    brc = Birch(n_clusters=None)
    brc.partial_fit(X)

    for k_cluster in range(2, max_nb_cluster+1):

        brc.set_params(n_clusters=k_cluster)
        labels = brc.fit_predict(X)
        result_birch = np.append(result_birch, silhouette_score(X, labels))

    result_final = np.zeros(len(result_birch))

    for i in range(len(result_birch)):
        if result_birch[i] < result_kmeans[i]:
            result_final[i] = result_kmeans[i]
        else:
            result_final[i] = result_birch[i]

    return np.argmax(result_final) + 2, result_final


def assess_tendency_calinski_harabaz(X, max_nb_cluster=10, random_state=None):
    """Assess the clusterability of a dataset using the number of cluster that best scored with the calinski_harabaz score using algorithm Birch and Kmeans

    Parameters
    ----------
    X : numpy array, DataFrame
        The input dataset
    max_nb_cluster : int
        The number of cluster maximum to consider
    random_state : int (default to None)

    Returns
    ---------------------
    (n_clusters, value) :  n_clusters is the number of cluster that allowed the best calinski_harabaz score on Kmeans or Birch. As for value, it is the maximum calinski_harabaz score for each number of cluster on KMeans and Birch.

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

    result_birch = np.array([])

    brc = Birch(n_clusters=None)
    brc.partial_fit(X)

    for k_cluster in range(2, max_nb_cluster+1):

        brc.set_params(n_clusters=k_cluster)
        labels = brc.fit_predict(X)
        result_birch = np.append(
            result_birch, calinski_harabaz_score(X, labels))

    result_final = np.zeros(len(result_birch))

    for i in range(len(result_birch)):
        if result_birch[i] < result_kmeans[i]:
            result_final[i] = result_kmeans[i]
        else:
            result_final[i] = result_birch[i]

    return np.argmax(result_final) + 2, result_final


def assess_tendency_davies_bouldin(X, max_nb_cluster=10, random_state=None):
    """Assess the clusterability of a dataset using the number of cluster that best scored with the davies_bouldin score using algorithm Birch and Kmeans
assess_tendency_silhouette
    Parameters
    ----------
    X : numpy array, DataFrame
        The input dataset
    max_nb_cluster : int
        The number of cluster maximum to consider
    random_state : int (default to None)

    Returns
    ---------------------
    (n_clusters, value) :  n_clusters is the number of cluster that allowed the best davies_bouldin score on Kmeans or Birch. As for value, it is the minimum davies_bouldin score for each number of cluster on KMeans and Birch.

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

    result_birch = np.array([])

    brc = Birch(n_clusters=None)
    brc.partial_fit(X)

    for k_cluster in range(2, max_nb_cluster+1):

        brc.set_params(n_clusters=k_cluster)
        labels = brc.fit_predict(X)
        result_birch = np.append(
            result_birch, davies_bouldin_score(X, labels))

    result_final = np.zeros(len(result_birch))

    for i in range(len(result_birch)):
        if result_birch[i] > result_kmeans[i]:
            result_final[i] = result_kmeans[i]
        else:
            result_final[i] = result_birch[i]

    print(result_birch)
    print(result_kmeans)

    return np.argmin(result_final) + 2, result_final
