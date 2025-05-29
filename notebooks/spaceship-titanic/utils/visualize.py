import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
pd.set_option('display.max_columns', None)


def describe_custom(df):
    desc = df.describe(include='all').T  # Transpose for easier merging
    desc['null'] = df.isnull().sum()
    desc['null%'] = (df.isnull().sum() / len(df) * 100)
    desc['dtype'] = df.dtypes
    
    return desc

def visualize_overview(df, target_column):
    if target_column in df.columns:
        sns.countplot(x=target_column, data=df)
        plt.title("Target Distribution")
        plt.show()

def plot_numerics(df, numerics):
    df[numerics].hist(bins=20, figsize=(12, 8))
    plt.tight_layout()
    plt.show()

def plot_categoricals(df, categoricals, target):
    for col in categoricals:
        sns.countplot(x=col, hue=target, data=df)
        plt.title(f"{col} by {target}")
        plt.xticks(rotation=30)
        plt.show()

def split_and_append_column(df, column, separator, newcolumns):
    """
    Splits the specified column by `separator` and adds new columns to the dataframe.
    
    Args:
        df (pd.DataFrame): The input DataFrame
        column (str): The column to split (e.g., 'Cabin')
        separator (str): The character used to split the string (e.g., '/')
        newcolumns (List[str]): List of new column names to assign the split parts
    
    Returns:
        pd.DataFrame: Updated DataFrame with new columns
    """
    split_cols = df[column].str.split(separator, expand=True)
    for i, new_col in enumerate(newcolumns):
        df[new_col] = split_cols[i]
    return df


def sum_columns(df, column_list, sum_column_title):
    """
    Adds a new column to the DataFrame by summing the values across the specified columns.

    Args:
        df (pd.DataFrame): The input DataFrame.
        column_list (List[str]): The columns to sum across.
        sum_column_title (str): The name of the new column to create.

    Returns:
        pd.DataFrame: The updated DataFrame with the new column.
    """
    df[sum_column_title] = df[column_list].sum(axis=1)
    return df


def plot_violin(df, x_axis, y_axis, title):
    """
    Creates a violin plot using the specified x and y axes.

    Args:
        df (pd.DataFrame): The data to plot.
        x_axis (str): Column name for the x-axis (usually categorical).
        y_axis (str): Column name for the y-axis (usually numeric).
        title (str): Title of the plot.
    """
    sns.violinplot(data=df, x=x_axis, y=y_axis)
    plt.title(title)
    plt.show()

def plot_count(df, x_axis, hue=None, title=None):
    """
    Creates a countplot with optional hue and dynamic title.

    Args:
        df (pd.DataFrame): The data to plot.
        x_axis (str): Column name for the x-axis.
        hue (str, optional): Column name for hue (e.g., to color by category).
        title (str, optional): Title of the plot. Defaults to auto-generated.
    """
    sns.countplot(data=df, x=x_axis, hue=hue)
    plt.title(title if title else f"{x_axis} count plot")
    plt.xticks(rotation=30)
    plt.show()


