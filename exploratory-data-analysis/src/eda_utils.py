import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


def extract_frequent_words(
        dataframe: pd.DataFrame, 
        name_of_column_containing_text: str,
        name_of_column_containing_labels: str,
        target_labels: list[str]) -> dict:
    filtered_dataframe = dataframe[dataframe[name_of_column_containing_labels].apply(
        lambda labels: any(label in labels for label in target_labels))]
    frequent_words = pd.Series(' '.join(filtered_dataframe[name_of_column_containing_text]).lower().split()).value_counts()
    frequent_words_dict = frequent_words.to_dict()
    frequent_words_without_stopwords = {word:frequency for word, frequency in frequent_words_dict.items() if word not in ENGLISH_STOP_WORDS}
    return frequent_words_without_stopwords


def plot_frequent_words(frequent_words: dict, size_limit: int = 50, fig_dims: tuple = (16, 12), title: str = None) -> None:
    if len(frequent_words) < size_limit: 
        size_limit = len(frequent_words)
    fig, ax = plt.subplots(figsize=fig_dims)
    sns.barplot(x=list(frequent_words.values())[:size_limit],
                y=list(frequent_words.keys())[:size_limit],
                ax=ax)
    
    plot_title = 'Most Frequent Words' if title is None else f'Most Frequent Words in "{title}" Category'
    ax.set_title(plot_title)
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Word')
    plt.show()
