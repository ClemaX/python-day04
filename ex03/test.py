from FileLoader import FileLoader as loader
from HowManyMedals import howManyMedals

df = loader.load('../data/athlete_events.csv')
md = howManyMedals(df, 'Kjetil Andr Aamodt')
print(md)
