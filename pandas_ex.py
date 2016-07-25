import numpy as np
import pandas as pd

def main():
    do_exercise()

def do_exercise():
    # 1
    appl_bars = pd.read_csv("./AAPL.csv")
    # 2
    date_index = appl_bars.pop('Date')
    appl_bars.index = pd.to_datetime(date_index)
    # 3
    ts1 = appl_bars.Open.values
    ts2 = appl_bars.Close.values
    ts3 = appl_bars.Volume.values
    appl_dic = {'Open' : ts1, 'Close' : ts2, 'Volume' : ts3}
    df = pd.DataFrame(appl_dic)
    # 4
    df.index = pd.to_datetime(date_index)
    df = df[:]['1989':'2003-04']
    print(df)
    return df

if __name__ == "__main__":
    main()