from FileLoader import FileLoader as loader
from HowManyMedalsByCountry import howManyMedalsByCountry

df = loader.load('../data/athlete_events.csv')
print(howManyMedalsByCountry(df, 'France'))
