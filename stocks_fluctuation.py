import os
import pandas as pd
import numpy as np
import sklearn.decomposition
import sklearn.preprocessing
import sklearn.cluster
import scipy.spatial.distance

def main():
    # 1
    stocks_df, code_to_name = load_data()

    stocks_df = calculate_fluctuations(stocks_df)
    #print(list(stocks_df['000020'].values)[0:10])
    print(stocks_df)

def calculate_fluctuations(stocks_df):
    # 2
    code_list = stocks_df.columns
    for code in code_list:
        if stocks_df[code].count() < 1400:
            stocks_df.drop(code, 1, inplace = True)
    new_code_list = stocks_df.columns
    for code in new_code_list:
        fluctuation = []
        before = 0
        for price in stocks_df[code].values:
            if before == 0 or np.isnan(float(before)) or np.isnan(float(price)):
                fluctuation.append(0)
            else:
                fluctuation.append((price - before)/before)
            before = price
        stocks_df[code] = fluctuation
    
    
    # 3
    return stocks_df

def load_data():
    stocks_df = pd.read_csv("./stocks.csv")
    stocks_df = stocks_df.set_index('index')
    krx_listed_companies = pd.read_csv("./krx_listed_companies.csv")

    code_to_name = {}
    for code, name in zip(krx_listed_companies['Code'].values, krx_listed_companies['Name'].values):
        z_code = '0' * (6 - len(str(code))) + str(code)
        code_to_name[z_code] = name

    return stocks_df, code_to_name

if __name__ == "__main__":
    main()