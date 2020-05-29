from FileLoader import FileLoader as loader
from YoungestFellah import youngestFellah


data = loader.load('../data/athlete_events.csv')
print(youngestFellah(data, 2004))
