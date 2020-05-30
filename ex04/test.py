from FileLoader import FileLoader as loader
from SpatioTemporalData import SpatioTemporalData

df = loader.load('../data/athlete_events.csv')
sp = SpatioTemporalData(df)

print('1896:   ', sp.where(1896))
print('2016:   ', sp.where(2016))

print('Athina: ', sp.when('Athina'))
print('Paris:  ', sp.when('Paris'))
