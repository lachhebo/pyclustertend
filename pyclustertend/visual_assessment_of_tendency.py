from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import pairwise_distances
from numba import njit


def vat(data: np.ndarray, return_odm: bool = False, figure_size: Tuple = (10, 10)):
    """VAT means Visual assessment of tendency. basically, it allow to asses cluster tendency
    through a map based on the dissimilarity matrix.


    Parameters
    ----------

    data : matrix
        numpy array

    return_odm : return the Ordered dissimilarity Matrix
        boolean (default to False)

    figure_size : size of the VAT.
        tuple (default to (10,10))


    Return
    -------

    ODM : matrix
        the ordered dissimilarity matrix plotted.

    """

    ordered_dissimilarity_matrix = compute_ordered_dissimilarity_matrix(data)

    _, ax = plt.subplots(figsize=figure_size)
    ax.imshow(
        ordered_dissimilarity_matrix,
        cmap="gray",
        vmin=0,
        vmax=np.max(ordered_dissimilarity_matrix),
    )

    if return_odm is True:
        return ordered_dissimilarity_matrix


@njit(cache=True)
def compute_ordered_dis_njit(matrix_of_pairwise_distance: np.ndarray):  # pragma: no cover
    """
    The ordered dissimilarity matrix is used by visual assessment of tendency. It is a just a a reordering
    of the dissimilarity matrix.


    Parameter
    ----------

    x : matrix
        numpy array

    Return
    -------

    ODM : matrix
        the ordered dissimilarity matrix

    """

    # Step 1 :

    observation_path = np.zeros(matrix_of_pairwise_distance.shape[0], dtype="int")

    list_of_int = np.zeros(matrix_of_pairwise_distance.shape[0], dtype="int")

    index_of_maximum_value = np.argmax(matrix_of_pairwise_distance)

    column_index_of_maximum_value = (
        index_of_maximum_value // matrix_of_pairwise_distance.shape[1]
    )

    list_of_int[0] = column_index_of_maximum_value
    observation_path[0] = column_index_of_maximum_value

    K = np.linspace(
        0,
        matrix_of_pairwise_distance.shape[0] - 1,
        matrix_of_pairwise_distance.shape[0],
    ).astype(np.int32)

    J = np.delete(K, column_index_of_maximum_value)

    for r in range(1, matrix_of_pairwise_distance.shape[0]):

        p, q = (-1, -1)

        mini = np.max(matrix_of_pairwise_distance)

        for candidate_p in observation_path[0:r]:
            for candidate_j in J:
                if matrix_of_pairwise_distance[candidate_p, candidate_j] < mini:
                    p = candidate_p
                    q = candidate_j
                    mini = matrix_of_pairwise_distance[p, q]

        list_of_int[r] = q
        observation_path[r] = q
        ind_q = np.where(J == q)[0][0]
        J = np.delete(J, ind_q)

    # Step 3

    ordered_matrix = np.zeros(matrix_of_pairwise_distance.shape)

    for column_index_of_maximum_value in range(ordered_matrix.shape[0]):
        for j in range(ordered_matrix.shape[1]):
            ordered_matrix[
                column_index_of_maximum_value, j
            ] = matrix_of_pairwise_distance[
                list_of_int[column_index_of_maximum_value], list_of_int[j]
            ]

    # Step 4 :

    return ordered_matrix


def compute_ordered_dissimilarity_matrix(x: np.ndarray) -> np.ndarray:
    matrix_of_pairwise_distance = pairwise_distances(x)
    dis_matrix = compute_ordered_dis_njit(matrix_of_pairwise_distance)
    return dis_matrix


def ivat(data: np.ndarray, return_odm: bool = False, figure_size: Tuple = (10, 10)):
    """iVat return a visualisation based on the Vat but more reliable and easier to
    interpret.


    Parameters
    ----------

    data : matrix
        numpy array

    return_odm : return the Ordered dissimilarity Matrix
            boolean (default to False)

    figure_size : size of the VAT.
        tuple (default to (10,10))


    Return
    -------

    D_prim : matrix
        the ivat ordered dissimilarity matrix

    """

    ordered_matrix = compute_ivat_ordered_dissimilarity_matrix(data)

    _, ax = plt.subplots(figsize=figure_size)
    ax.imshow(ordered_matrix, cmap="gray", vmin=0, vmax=np.max(ordered_matrix))

    if return_odm is True:
        return ordered_matrix


def compute_ivat_ordered_dissimilarity_matrix(x: np.ndarray):
    """The ordered dissimilarity matrix is used by ivat. It is a just a a reordering
    of the dissimilarity matrix.


    Parameters
    ----------

    x : matrix
        numpy array

    Return
    -------

    D_prim : matrix
        the ordered dissimilarity matrix

    """

    ordered_matrix = compute_ordered_dissimilarity_matrix(x)
    re_ordered_matrix = np.zeros((ordered_matrix.shape[0], ordered_matrix.shape[0]))

    for r in range(1, ordered_matrix.shape[0]):
        # Step 1 : find j for which D[r,j] is minimum and j ipn [1:r-1]

        j = np.argmin(ordered_matrix[r, 0:r])

        # Step 2 :

        re_ordered_matrix[r, j] = ordered_matrix[r, j]
        re_ordered_matrix[j, r] = ordered_matrix[r, j]

        # Step 3 : for c : 1, r-1 with c !=j
        c_tab = np.array(range(0, r))
        c_tab = c_tab[c_tab != j]

        for c in c_tab:
            re_ordered_matrix[r, c] = max(ordered_matrix[r, j], re_ordered_matrix[j, c])
            re_ordered_matrix[c, r] = re_ordered_matrix[r, c]

    return re_ordered_matrix
