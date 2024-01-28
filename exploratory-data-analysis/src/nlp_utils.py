import re
import string
import pandas as pd
import matplotlib.pyplot as plt
from typing import Optional


def convert_to_lowercase(text: str) -> str:
    """
    Converts the input text to lowercase.
    Args:
        text (str): The input text.
    Returns:
        str: The converted text.
    """
    return text.lower()

def remove_leading_hashtags(text: str) -> str:
    """
    Removes the leading hashtag sign in front of the words from the input text.
    Args:
        text (str): The input text.
    Returns:
        str: The text without hashtags.
    """
    return re.sub('(#)(\S+)', r' \2', text)

def remove_punctuations(text: str) -> str:
    """
    Removes punctuations from the input text.
    Args:
        text (str): The input text.
    Returns:
        str: The text without punctuations.
    """
    return re.sub('[%s]' % re.escape(string.punctuation), '', text)

def remove_multiple_whitespaces(text: str) -> str:
    """
    Removes possible multiple whitespaces between the words of the given input text.
    Args:
        text (str): The input text.
    Returns:
        str: The text without multiple whitespaces.
    """
    return re.sub(' +', ' ', text)

def remove_surrounding_whitespaces(text: str) -> str:
    """
    Removes leading and trailing whitespaces from the input text.
    Args:
        text (str): The input text.
    Returns:
        str: The text without leading and trailing whitespaces.
    """
    return text.strip()

def trim_text(text: str) -> str:
    """
    Removes all extra whitespace from the input text.
    Args:
        text (str): The input text.
    Returns:
        str: The text without any extra whitespaces.
    """
    return remove_surrounding_whitespaces(remove_multiple_whitespaces(text))


def preprocess_text(text: str, options: Optional[list[str]] = None) -> str:
    """
    Applies text preprocessing to the input text data, based on the given options.
    Args:
        text (str): The input text.
        options (list, optional): The list of options to apply to the input text. Defaults to None.
            If None, the all available options will be applied. Available options:
                'trim_text': Removes all extra whitespace from the input text.
                'remove_hashtags': Removes hashtags from the input text.
                'remove_punctuations': Removes punctuations from the input text.
                'convert_to_lowercase': Converts the input text to lowercase.
    Returns:
        str: The preprocessed text.
    Raises:
        ValueError: If an unknown option is passed.
    """
    valid_options = {
        'remove_hashtags': remove_leading_hashtags,
        'remove_punctuations': remove_punctuations,
        'convert_to_lowercase': convert_to_lowercase,
        'trim_text': trim_text
    }
    if options is not None:
        for option in options:
            if option not in valid_options.keys():
                raise ValueError(f'Unknown option: {option}')

    action_list = valid_options.values() if options is None else [valid_options[option] for option in options]
    for action in action_list:
        text = action(text)

    return text


def plot_cloud(wordcloud, fig_dims: tuple = (12, 12)) -> None:
    """
    Plots the given wordcloud object.
    Args:
        wordcloud: The wordcloud object to plot.
        fig_dims (tuple, optional): The dimensions of the figure. Defaults to (12, 12).
    """
    plt.figure(figsize=fig_dims)
    plt.axis("off")
    plt.imshow(wordcloud)


def extract_all_words(dataframe: pd.DataFrame, text_column_name: str) -> str:
    """
    Extracts all the words in the given text column of the given dataframe.
    Args:
        dataframe (pd.DataFrame): The input dataframe.
        text_column_name (str): The name of the text column.
    Returns:
        list[str]: The list of all the words in the given text column of the given dataframe.
    """
    return ' '.join(dataframe[text_column_name].to_list())
