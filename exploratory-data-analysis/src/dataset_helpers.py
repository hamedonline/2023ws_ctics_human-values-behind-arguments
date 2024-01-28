import pandas as pd


def create_simplified_data(df: pd.DataFrame, label_columns: list[str]) -> pd.DataFrame:
    """
    Creates a simplified version of the given dataframe, based on the given label columns.
    Args:
        df (pd.DataFrame): The input dataframe.
        label_columns (list[str]): The list of label columns to use for simplification.
    Returns:
        pd.DataFrame: The simplified dataframe.
    """
    return pd.DataFrame(
        {
            'argument_id': df['Argument ID'],
            'stance': df['Stance'],
            'conclusion': df['Conclusion'],
            'premise': df['Premise'],
            'labels': df[label_columns].apply(lambda row: row.index[row == 1].tolist(), axis=1)
        }
    )


def find_duplicate_rows(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Finds duplicate rows in the given dataframe of dataset, based on the given column name.
    Args:
        df (pd.DataFrame): The input dataframe.
        column_name (str): The name of the column to use for finding duplicates.
    Returns:
        pd.DataFrame: The dataframe containing the duplicate rows.
    """
    # sorting by values of the specified column_name is applied to ensure duplicates are grouped together
    return df[df[column_name].duplicated(keep=False)].sort_values(column_name)


def build_duplicate_details(df: pd.DataFrame, column_name: str) -> dict:
    """
    Builds a dictionary containing details of duplicate values in a given DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to analyze.
        column_name (str): The name of the column to check for duplicates.

    Returns:
        dict: A dictionary with the following structure:
            - Keys: Tuples containing indices of duplicate rows.
            - Values: Dictionaries containing duplicate row values in a column_name:value format.
    """
    duplicates = find_duplicate_rows(df, column_name)
    if duplicates.empty:
        return {}

    details_dict = {}
    prev_value = None
    duplicate_indices = []
    value_dicts = {}

    for index, row in duplicates.iterrows():
        current_value = row[column_name]

        if current_value == prev_value:
            duplicate_indices.append(index)
            # value_dicts.append(row.to_dict())
            value_dicts[index] = row.to_dict()
        else:
            if duplicate_indices:
                details_dict[tuple(duplicate_indices)] = value_dicts
            duplicate_indices = [index]
            # value_dicts = [row.to_dict()]
            value_dicts = {index: row.to_dict()}

        prev_value = current_value

    # add the last group of duplicates, if any
    if duplicate_indices:
        details_dict[tuple(duplicate_indices)] = value_dicts

    return details_dict


def remove_redundant_pairs(reference_pairs: list) -> list:
    pair_set = set()
    for pair_tuple in reference_pairs:
        # sort the pair and convert it back to a tuple
        sorted_pair = tuple(sorted(pair_tuple))
        # add the sorted pair to the set (which will remove duplicates if any)
        pair_set.add(sorted_pair)

    return sorted(list(pair_set))


def extract_intersection_keys(dict1: dict, dict2: dict) -> list:
    """
    Extracts the keys that are common in two dictionaries.

    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.

    Returns:
        list: The list of common keys (in ascending order).
    """
    intersection_key_pairs = list(set(dict1.keys()) & set(dict2.keys()))
    # remove possible redundant pairs
    intersection_key_pairs = remove_redundant_pairs(intersection_key_pairs)
    return intersection_key_pairs


def extract_union_keys(dict1: dict, dict2: dict) -> list:
    """
    Extracts the keys that are present in either of two dictionaries.

    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.

    Returns:
        list: The unique sorted list of all keys in both dictionaries (in ascending order).
    """
    union_key_pairs = list(set(dict1.keys()) | set(dict2.keys()))
    # remove possible redundant pairs: (a, b) and (b, a) are the same
    union_key_pairs = remove_redundant_pairs(union_key_pairs)
    return union_key_pairs


def find_difference_in_duplicates(duplicates_dict: dict, column_to_compare: str, reference_df: pd.DataFrame):
    differ_dict = {}
    for key_pair in duplicates_dict.keys():
        if reference_df.loc[key_pair[0], column_to_compare] != reference_df.loc[key_pair[1], column_to_compare]:
            differ_dict[key_pair] = duplicates_dict[key_pair]
    return differ_dict
