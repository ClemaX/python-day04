from FileLoader import FileLoader as fl
from ProportionBySport import proportionBySport


df = fl.load('../data/athlete_events.csv')
p = proportionBySport(df, 2004, 'Tennis', 'F')
print(p)
