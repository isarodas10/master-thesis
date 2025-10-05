"""
Visualization Module
Functions for creating plots and visualizations for the analysis.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def plot_missing_data_matrix(data, figsize=(20, 10), fontsize=8):
    """
    Plot missing data matrix using missingno.
    
    Parameters
    ----------
    data : pd.DataFrame
        Dataset to visualize
    figsize : tuple, default=(20, 10)
        Figure size
    fontsize : int, default=8
        Font size for labels
    
    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    import missingno as msno
    return msno.matrix(data, figsize=figsize, fontsize=fontsize, sparkline=False)


def plot_correlation_heatmap(data, method='spearman', figsize=(8, 6), cmap='RdBu', 
                             vmin=-1, vmax=1, annot=True):
    """
    Plot correlation heatmap for ordinal/categorical variables.
    
    Parameters
    ----------
    data : pd.DataFrame
        Data to correlate
    method : str, default='spearman'
        Correlation method ('pearson', 'spearman', 'kendall')
    figsize : tuple, default=(8, 6)
        Figure size
    cmap : str, default='RdBu'
        Color map
    vmin, vmax : float
        Color scale limits
    annot : bool, default=True
        Show correlation values
    
    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    corr_matrix = data.corr(method=method)
    
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(corr_matrix, cmap=cmap, annot=annot, fmt='.2f',
                vmin=vmin, vmax=vmax, ax=ax)
    plt.title(f"Correlations ({method.capitalize()})")
    plt.tight_layout()
    return ax


def plot_correlation_clustermap(data, method='spearman', figsize=(14, 12)):
    """
    Plot hierarchical clustered correlation heatmap.
    
    Parameters
    ----------
    data : pd.DataFrame
        Data to correlate
    method : str, default='spearman'
        Correlation method
    figsize : tuple, default=(14, 12)
        Figure size
    
    Returns
    -------
    seaborn.matrix.ClusterGrid
        The clustermap object
    """
    corr_matrix = data.corr(method=method).fillna(0)
    g = sns.clustermap(corr_matrix, method='ward', cmap='RdBu', annot=True,
                       vmin=-1, vmax=1, figsize=figsize)
    plt.title("Hierarchical Clustering of Correlations")
    return g


def plot_grouped_counts(data, group_by, figsize=(10, 10), cmap='rocket'):
    """
    Plot grouped counts as horizontal bar chart.
    
    Parameters
    ----------
    data : pd.DataFrame
        Dataset to plot
    group_by : str
        Column to group by
    figsize : tuple, default=(10, 10)
        Figure size
    cmap : str, default='rocket'
        Color palette
    
    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    grouped = data.groupby(group_by).agg('count')
    ax = grouped.sort_index(ascending=False).plot(
        kind='barh',
        figsize=figsize,
        cmap=cmap,
        edgecolor='black',
        fontsize=14,
        title=f'Counts by {group_by}'
    )
    ax.yaxis.label.set_visible(False)
    return ax


def plot_cluster_characteristics(data, question_col, group_col, group_value, 
                                 order=None, palette='Spectral', ax=None):
    """
    Plot response distribution for a specific group/cluster.
    
    Parameters
    ----------
    data : pd.DataFrame
        Dataset with responses
    question_col : str
        Column with responses to plot
    group_col : str
        Column to filter by (e.g., 'Sex', 'cluster')
    group_value : str or int
        Value of group_col to plot
    order : list, optional
        Order of categories on y-axis
    palette : str, default='Spectral'
        Color palette
    ax : matplotlib.axes.Axes, optional
        Axes to plot on
    
    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    reduced_df = data[[question_col, group_col]]
    data_to_plot = reduced_df[reduced_df[group_col] == group_value][question_col].value_counts(normalize=True)
    
    ax = sns.barplot(
        y=data_to_plot.index,
        x=data_to_plot.values,
        ax=ax,
        order=order,
        palette=palette,
        edgecolor='black'
    )
    ax.set_title(f'{group_col} {group_value}: {question_col}')
    ax.yaxis.label.set_visible(False)
    
    return ax


def plot_elbow_curve(x_values, y_values, xlabel='Number of Clusters', 
                    ylabel='Cost', title='Elbow Method'):
    """
    Plot elbow curve for cluster optimization.
    
    Parameters
    ----------
    x_values : array-like
        X-axis values (e.g., number of clusters)
    y_values : array-like
        Y-axis values (e.g., cost, inertia)
    xlabel : str
        X-axis label
    ylabel : str
        Y-axis label
    title : str
        Plot title
    
    Returns
    -------
    matplotlib.axes.Axes
        The plot axes
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x_values, y_values, marker='o', linestyle='-', linewidth=2, markersize=8)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title, fontsize=14)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    return ax


def plot_cluster_distributions(data, variables, cluster_col='cluster', 
                               figsize=(15, 5), palette='viridis'):
    """
    Plot count distributions across clusters for multiple variables.
    
    Parameters
    ----------
    data : pd.DataFrame
        Dataset with cluster assignments
    variables : list
        List of variable names to plot
    cluster_col : str, default='cluster'
        Name of cluster column
    figsize : tuple, default=(15, 5)
        Figure size per plot
    palette : str, default='viridis'
        Color palette
    
    Returns
    -------
    None
        Displays plots
    """
    for var in variables:
        plt.figure(figsize=figsize)
        chart = sns.countplot(
            x=data[var],
            order=data[var].value_counts().index,
            hue=data[cluster_col],
            palette=palette
        )
        chart.set_xticklabels(chart.get_xticklabels(), rotation=45, ha='right')
        plt.title(f'{var} by {cluster_col}')
        plt.tight_layout()
        plt.show()
