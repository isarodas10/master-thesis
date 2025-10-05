"""
Clustering Analysis Module
Contains functions for K-modes, DBSCAN, and cluster evaluation.
"""

import numpy as np
import pandas as pd
from kmodes.kmodes import KModes
from sklearn.cluster import DBSCAN
import gower


def fit_kmodes(data, n_clusters, init='Cao', n_init=1, verbose=1, random_state=None):
    """
    Fit K-modes clustering algorithm.
    
    Parameters
    ----------
    data : pd.DataFrame or np.ndarray
        Categorical data to cluster
    n_clusters : int
        Number of clusters
    init : str, default='Cao'
        Initialization method ('Cao' or 'Huang')
    n_init : int, default=1
        Number of initializations
    verbose : int, default=1
        Verbosity level
    random_state : int, optional
        Random seed
    
    Returns
    -------
    KModes
        Fitted K-modes model
    np.ndarray
        Cluster predictions
    """
    km = KModes(n_clusters=n_clusters, init=init, n_init=n_init, 
                verbose=verbose, random_state=random_state)
    clusters = km.fit_predict(data)
    return km, clusters


def evaluate_kmodes_range(data, cluster_range, init='Cao', n_init=1, verbose=1):
    """
    Evaluate K-modes for a range of cluster numbers.
    
    Parameters
    ----------
    data : pd.DataFrame or np.ndarray
        Data to cluster
    cluster_range : range or list
        Range of cluster numbers to try
    init : str, default='Cao'
        Initialization method
    n_init : int, default=1
        Number of initializations
    verbose : int, default=1
        Verbosity level
    
    Returns
    -------
    list
        Costs for each number of clusters
    """
    costs = []
    for num_clusters in cluster_range:
        kmode = KModes(n_clusters=num_clusters, init=init, n_init=n_init, verbose=verbose)
        kmode.fit_predict(data)
        costs.append(kmode.cost_)
    return costs


def get_cluster_centroids(model, column_names):
    """
    Extract cluster centroids as a DataFrame.
    
    Parameters
    ----------
    model : KModes
        Fitted K-modes model
    column_names : list
        Column names for the centroids
    
    Returns
    -------
    pd.DataFrame
        Cluster centroids
    """
    centroids_df = pd.DataFrame(model.cluster_centroids_)
    centroids_df.columns = column_names
    return centroids_df


def compute_gower_distance(data):
    """
    Compute Gower distance matrix for mixed data types.
    
    Parameters
    ----------
    data : pd.DataFrame
        Data with mixed types (categorical and numeric)
    
    Returns
    -------
    np.ndarray
        Distance matrix
    """
    return gower.gower_matrix(data)


def fit_dbscan_gower(data, eps=0.3, min_samples=2):
    """
    Fit DBSCAN using Gower distance for mixed data.
    
    Parameters
    ----------
    data : pd.DataFrame
        Data to cluster
    eps : float, default=0.3
        Maximum distance between samples
    min_samples : int, default=2
        Minimum samples in a neighborhood
    
    Returns
    -------
    np.ndarray
        Cluster labels (-1 for noise)
    """
    distance_matrix = compute_gower_distance(data)
    dbscan = DBSCAN(eps=eps, min_samples=min_samples, metric="precomputed")
    dbscan.fit(distance_matrix)
    return dbscan.labels_


def merge_cluster_assignments(original_data, cluster_labels, cluster_name='cluster'):
    """
    Merge cluster assignments back to original data.
    
    Parameters
    ----------
    original_data : pd.DataFrame
        Original dataset
    cluster_labels : np.ndarray or pd.Series
        Cluster assignments
    cluster_name : str, default='cluster'
        Name for cluster column
    
    Returns
    -------
    pd.DataFrame
        Data with cluster assignments
    """
    data_copy = original_data.copy()
    data_copy[cluster_name] = cluster_labels
    return data_copy


def get_cluster_summary(data, cluster_col='cluster', agg_func='mode'):
    """
    Summarize cluster characteristics.
    
    Parameters
    ----------
    data : pd.DataFrame
        Data with cluster assignments
    cluster_col : str, default='cluster'
        Name of cluster column
    agg_func : str or callable, default='mode'
        Aggregation function (mode, mean, median, etc.)
    
    Returns
    -------
    pd.DataFrame
        Cluster summaries
    """
    if agg_func == 'mode':
        return data.groupby(cluster_col).agg(pd.Series.mode)
    else:
        return data.groupby(cluster_col).agg(agg_func)


def get_cluster_sizes(data, cluster_col='cluster'):
    """
    Get size of each cluster.
    
    Parameters
    ----------
    data : pd.DataFrame
        Data with cluster assignments
    cluster_col : str, default='cluster'
        Name of cluster column
    
    Returns
    -------
    pd.Series
        Cluster sizes
    """
    return data.groupby(cluster_col).size()
