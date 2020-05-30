class SpatioTemporalData:
    def __init__(self, df):
        self.df = df

    def where(self, year):
        """Get locations from given year"""
        games = self.df.loc[self.df['Year'] == year]
        cities = games['City'].drop_duplicates()
        return cities.tolist()

    def when(self, location):
        """Get years from given location"""
        games = self.df.loc[self.df['City'] == location]
        years = games['Year'].drop_duplicates()
        return years.tolist()
