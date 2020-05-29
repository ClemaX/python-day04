import pandas


class FileLoader():
    @staticmethod
    def load(path):
        df = pandas.read_csv(path)
        height = df.shape[0]
        width = df.shape[1]
        print(f"Loaded dataset of dimensions {height} x {width}")
        return df

    def display(df, n):
        if n > 0:
            print(df[:n])
        else:
            print(df[n:])


if __name__ == '__main__':
    data = FileLoader.load('../data/athlete_events.csv')
    FileLoader.display(data, -2)
