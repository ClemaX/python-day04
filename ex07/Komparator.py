import pandas as pd
import matplotlib.pyplot as plt


class Komparator:
    def __init__(self, df):
        self.df = df

    def compare_box_plots(self, categorical_var, numerical_var):
        df.boxplot(numerical_var, categorical_var)
        plt.show()

    def density(self, categorical_var, numerical_var):
        df.groupby(categorical_var)[numerical_var].plot.kde(legend=True)
        plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        by_cat = df.pivot(columns=categorical_var)[numerical_var]
        by_cat.plot(kind='hist', alpha=0.5, stacked=True)
        plt.show()


if __name__ == '__main__':
    df = pd.read_csv('../data/athlete_events.csv')
    k = Komparator(df)
    k.compare_histograms('Sex', 'Height')
    k.compare_box_plots('Sex', 'Height')
    k.density('Sex', 'Height')
