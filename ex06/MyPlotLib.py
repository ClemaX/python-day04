from matplotlib import pyplot as plt
import pandas as pd


class MyPlotLib:
    @staticmethod
    def histogram(df, features):
        df[features].hist(edgecolor='black')
        plt.show()

    @staticmethod
    def density(df, features):
        df[features].plot.kde()
        plt.legend(loc="upper right")
        plt.show()

    @staticmethod
    def pair_plot(df, features):
        pd.plotting.scatter_matrix(df[features])
        plt.show()

    @staticmethod
    def box_plot(df, features):
        df[features].boxplot()
        plt.show()
