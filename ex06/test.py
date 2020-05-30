from MyPlotLib import MyPlotLib as plt
import pandas as pd


df = pd.read_csv('../data/athlete_events.csv')

plt.histogram(df, ['Height', 'Weight'])
plt.density(df, ['Height', 'Weight'])
plt.pair_plot(df, ['Height', 'Weight'])
plt.box_plot(df, ['Height', 'Weight'])
