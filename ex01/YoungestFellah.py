def youngestFellah(df, year):
    year_data = df.loc[df['Year'] == year]
    subset = year_data[['Sex', 'Age']]

    females = subset.loc[df['Sex'] == 'F'][['Age']]
    males = subset.loc[df['Sex'] == 'M'][['Age']]
    return {'f': float(females.min()), 'm': float(males.min())}
