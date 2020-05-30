def howManyMedals(df, name):
    subset = df.loc[df['Name'] == name]
    year_medals = subset[['Year', 'Medal']]
    by_year = year_medals.groupby(['Year'])
    result = {}
    for k, v in by_year:
        gold = v[v['Medal'] == 'Gold'].shape[0]
        silver = v[v['Medal'] == 'Silver'].shape[0]
        bronze = v[v['Medal'] == 'Bronze'].shape[0]
        result[k] = {'G': gold, 'S': silver, 'B': bronze}
    return result
