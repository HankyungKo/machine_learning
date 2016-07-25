import sklearn.decomposition
import numpy as np
import pandas as pd
import elice_utils2

def main():
    count = int(input())
    X = []
    Y = []
    for each in range(count):
        (a, b) = input().strip().split(' ')
        X.append(float(a))
        Y.append(float(b))
    df = input_data(X, Y)

    # 2
    pca, pca_array = run_PCA(df, 1)

    # 4
    print(elice_utils.draw_toy_example(df, pca, pca_array))

def input_data(X, Y):
    # 1
    df = pd.DataFrame({'x': X, 'y': Y})
    return df

def run_PCA(dataframe, num_components):
    # 2
    pca = sklearn.decomposition.PCA(n_components=1)
    pca.fit(dataframe)
    pca_array = pca.transform(dataframe)
    return pca, pca_array

if __name__ == '__main__':
    main()