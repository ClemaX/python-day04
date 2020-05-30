def proportionBySport(df, year, sport, gender):
    subset = df.loc[(df['Year'] == year) & (df['Sex'] == gender)]
    sport = subset.loc[subset['Sport'] == sport].drop_duplicates(subset='Name')
    all_sports = subset.drop_duplicates(subset='Name')
    return sport.shape[0] / all_sports.shape[0]
