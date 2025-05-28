import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def describe_with_missing(df):
    desc = df.describe(include='all').T  # Transpose for easier merging
    desc['null'] = df.isnull().sum()
    desc['null%'] = (df.isnull().sum() / len(df) * 100)
    desc['dtype'] = df.dtypes

    # Reorder columns
    cols = list(desc.columns)
    reordered = ['dtype', 'count', 'null', 'null%'] + [col for col in cols if col not in ['dtype', 'count', 'null', 'null%']]
    desc = desc[reordered]

    # Round numeric values
    numeric_cols = desc.select_dtypes(include='number').columns
    desc[numeric_cols] = desc[numeric_cols].round(2)
    
    return desc.style.format(precision=2)

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
