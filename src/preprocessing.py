"""
Data Preprocessing Module
Contains functions for data cleaning, missing data handling, and transformation.
"""

import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer


def replace_na_smart(base, column, value, fill_value, is_na):
    """
    Smart missing data replacement based on conditional logic.
    
    Parameters
    ----------
    base : pd.DataFrame
        The dataframe to modify
    column : str
        Column name to check for conditions
    value : list
        List of values to match (when is_na=False)
    fill_value : int/float
        Value to fill missing data with
    is_na : bool
        If True, fill where column is null; if False, fill where column matches values
    
    Returns
    -------
    pd.DataFrame
        Modified dataframe
    """
    if is_na:
        base.loc[base[column].isnull(), column:] = base.loc[base[column].isnull(), column:].fillna(fill_value)
    else:
        base.loc[base[column].isin(value), column:] = base.loc[base[column].isin(value), column:].fillna(fill_value)
    return base


def iterative_impute(data, cols_to_impute=None, max_iter=10, random_state=0):
    """
    Perform iterative imputation on missing data.
    
    Parameters
    ----------
    data : pd.DataFrame
        Dataframe with missing values
    cols_to_impute : list, optional
        Column names to impute. If None, imputes all numeric columns
    max_iter : int, default=10
        Maximum number of imputation iterations
    random_state : int, default=0
        Random seed for reproducibility
    
    Returns
    -------
    pd.DataFrame
        Dataframe with imputed values
    """
    imp = IterativeImputer(max_iter=max_iter, random_state=random_state)
    
    if cols_to_impute is None:
        cols_to_impute = data.select_dtypes(include=[np.number]).columns
    
    # Fit on complete cases
    complete_cases = data[~data[cols_to_impute].isnull().any(axis=1)]
    imp.fit(complete_cases[cols_to_impute])
    
    # Transform incomplete cases
    incomplete_cases = data[data[cols_to_impute].isnull().any(axis=1)]
    if len(incomplete_cases) > 0:
        imputed_data = np.round(imp.transform(incomplete_cases[cols_to_impute]))
        data.loc[incomplete_cases.index, cols_to_impute] = imputed_data
    
    return data


def decode_survey_responses(data, codebook, question_id):
    """
    Replace coded survey responses with text labels.
    
    Parameters
    ----------
    data : pd.DataFrame
        Survey data with coded responses
    codebook : pd.DataFrame
        Codebook with columns ['ID_Pregunta', 'Pregunta_text', 'Respuestas_text', 'Number']
    question_id : str
        Question ID to decode
    
    Returns
    -------
    pd.Series
        Decoded responses
    """
    mini = codebook[codebook.ID_Pregunta == question_id][['Number', 'Respuestas_text']]
    mini['Number'] = mini.Number.astype(float)
    mini = mini.set_index('Number').T.to_dict('records')
    return data[question_id].replace(mini[0])


def categorize_responses(data, column, categories):
    """
    Categorize numeric responses into broader groups.
    
    Parameters
    ----------
    data : pd.DataFrame
        Dataset to modify
    column : str
        Column name to categorize
    categories : dict
        Dictionary mapping category_value: (min_val, max_val) or list of values
    
    Returns
    -------
    pd.DataFrame
        Modified dataframe
    """
    for category_val, condition in categories.items():
        if isinstance(condition, tuple):
            min_val, max_val = condition
            mask = (data[column] >= min_val) & (data[column] <= max_val)
        elif isinstance(condition, list):
            mask = data[column].isin(condition)
        data.loc[mask, column] = category_val
    
    return data


def map_age_codes(data, age_column='Age'):
    """
    Map age codes to actual ages.
    
    Parameters
    ----------
    data : pd.DataFrame
        Dataset with age codes
    age_column : str, default='Age'
        Name of age column
    
    Returns
    -------
    pd.DataFrame
        Dataset with mapped ages
    """
    age_mapping = {1.0: 13, 2.0: 14, 3.0: 15, 4.0: 16, 5.0: 17}
    data[age_column] = data[age_column].replace(age_mapping)
    return data


def standardize_column_names(data, column_mapping):
    """
    Rename columns to more readable names.
    
    Parameters
    ----------
    data : pd.DataFrame
        Dataset to rename
    column_mapping : dict or list
        Dictionary of {old_name: new_name} or list of new names
    
    Returns
    -------
    pd.DataFrame
        Dataset with renamed columns
    """
    if isinstance(column_mapping, dict):
        data = data.rename(columns=column_mapping)
    elif isinstance(column_mapping, list):
        data.columns = column_mapping
    return data
