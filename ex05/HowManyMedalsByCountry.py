def howManyMedalsByCountry(df, country):
    subset = df.loc[df['Team'] == country].dropna(subset=['Medal'])
    year_medals = subset[['Year', 'Event', 'Medal']]
    unique = year_medals.drop_duplicates(subset=['Event', 'Medal'])
    by_year = unique.groupby(['Year'])
    result = {}
    for k, v in by_year:
        gold = v[v['Medal'] == 'Gold'].shape[0]
        silver = v[v['Medal'] == 'Silver'].shape[0]
        bronze = v[v['Medal'] == 'Bronze'].shape[0]
        result[k] = {'G': gold, 'S': silver, 'B': bronze}
    return result
