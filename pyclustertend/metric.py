from sklearn.metrics import (
    silhouette_score,
    calinski_harabasz_score,
    davies_bouldin_score,
)
from sklearn.cluster import KMeans
import numpy as np


def assess_tendency_by_metric(
    dataset, metric="silhouette", n_cluster=10, random_state=None
):
    """Assess the clusterability of a dataset using KMeans algorithm and a metric score, the best cluster number
    is the number that best scored with the silhouette score.

    Parameters
    ----------
    dataset : numpy array, DataFrame
        The input dataset
    metric : string
         The method to assess cluster quality ('silhouette', 'calinski_harabasz', 'davies_bouldin'), default to
         'silhouette'
    n_cluster : int
        The maxium number of cluster to consider
    random_state : int (default to None)

    Returns
    ---------------------
    (n_clusters, value) :  n_clusters is the number of cluster that best scored on the silhouette score on Kmeans.
    As for value, it is the silhouette score for each number of cluster on KMeans.

    Examples
    --------
    >>> from sklearn import datasets
    >>> from pyclustertend import assess_tendency_by_metric
    >>> from sklearn.preprocessing import scale
    >>> X = scale(datasets.load_boston().data)
    >>> assess_tendency_by_metric(X, n_cluster=10)
    (2, array([0.36011769, 0.25740335, 0.28098046, 0.28781574, 0.26746932,
        0.26975514, 0.27155699, 0.28883395, 0.29028124]))

    """
    result_kmeans = np.array([])

    for k_cluster in range(2, n_cluster + 1):
        labels = KMeans(n_clusters=k_cluster, random_state=random_state).fit_predict(
            dataset
        )
        if metric == "silhouette":
            result_kmeans = np.append(result_kmeans, silhouette_score(dataset, labels))
        elif metric == "calinski_harabasz":
            result_kmeans = np.append(
                result_kmeans, calinski_harabasz_score(dataset, labels)
            )
        elif metric == "davies_bouldin":
            result_kmeans = np.append(
                result_kmeans, davies_bouldin_score(dataset, labels)
            )

    if metric == "davies_bouldin":
        return np.argmin(result_kmeans) + 2, result_kmeans
    else:
        return np.argmax(result_kmeans) + 2, result_kmeans


def assess_tendency_by_mean_metric_score(dataset, n_cluster=10, random_state=None):
    """Assess the clusterability of a dataset using KMeans algorithm and the silhouette, calinski and davies bouldin
    score, the best cluster number is the mean of the result of the three methods.

    Parameters
    ----------
    dataset : numpy array, DataFrame
        The input dataset
    n_cluster : int
        The maxium number of cluster to consider
    random_state : int (default to None)

    Returns
    ---------------------
    n_clusters :  n_clusters is the mean of the best number of cluster score (with Kmeans algorithm)

    Examples
    --------
    >>> from sklearn import datasets
    >>> from pyclustertend import assess_tendency_by_mean_metric_score
    >>> from sklearn.preprocessing import scale
    >>> X = scale(datasets.load_boston().data)
    >>> assess_tendency_by_mean_metric_score(X,10)
    2.6666666666666665
    """

    silhouette_best, _ = assess_tendency_by_metric(
        dataset, metric="silhouette", n_cluster=n_cluster, random_state=random_state
    )

    calinski_best, _ = assess_tendency_by_metric(
        dataset,
        metric="calinski_harabasz",
        n_cluster=n_cluster,
        random_state=random_state,
    )

    davies_best, _ = assess_tendency_by_metric(
        dataset, metric="davies_bouldin", n_cluster=n_cluster, random_state=random_state
    )

    return np.mean([silhouette_best, calinski_best, davies_best])
