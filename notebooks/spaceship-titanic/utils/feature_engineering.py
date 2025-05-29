import pandas as pd
from utils.visualize import split_and_append_column, sum_columns

def prepare_features(df):
    # Handle Cabin → CabinDeck, CabinNum, CabinSide
    df = split_and_append_column(df, 'Cabin', '/', ['CabinDeck', 'CabinNum', 'CabinSide'])

    # TotalSpend = sum of amenities
    spend_cols = ['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']
    df = sum_columns(df, spend_cols, 'TotalSpend')
    df['TotalSpend'] = df['TotalSpend'].fillna(0)

    # Impute CryoSleep: If spent money, assume not in cryo sleep
    df.loc[df['CryoSleep'].isnull() & (df['TotalSpend'] > 0), 'CryoSleep'] = False
    df.loc[df['CryoSleep'].isnull() & (df['TotalSpend'] == 0), 'CryoSleep'] = True

    # Impute VIP: Assume False if spent nothing and not VIP, else mode
    df['VIP'] = df['VIP'].fillna(False)

    # Age → fill with median
    df['Age'] = df['Age'].fillna(df['Age'].median())

    # Fill mode for HomePlanet, Destination, CabinDeck, CabinSide
    for col in ['HomePlanet', 'Destination', 'CabinDeck', 'CabinSide']:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Convert boolean columns to numeric
    df['CryoSleep'] = df['CryoSleep'].astype(int)
    df['VIP'] = df['VIP'].astype(int)

    # Encode 'Sex' as 0 (female) and 1 (male)
    df['Sex'] = df['Sex'].map({'male': 1, 'female': 0})

    return df
