#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:16:40 2019

@author: zhongjiulu
"""
# Import libraries

import pandas as pd
import numpy as np

# dummy_data
filename = "sample.csv"
n = 10

def moneyFlowIndex(filename, n):
    # read the input data into workplace
    df = pd.read_csv(filename)
    # generate typical price feature
    df["Typical Price"] = df[['High', 'Low', 'Close']].mean(axis=1)
    
    # create flag to define whether it is positive or negative flow
    df["pos_neg"] = df["Typical Price"].diff(periods=1)
    
    #df["pos_neg_bool"] = np.where(df["typical_price"].diff(periods=1) > 0, 1, -1)
    # create the positive money flow feature
    df["Positive Money Flow"] = df.loc[df.pos_neg > 0]["Typical Price"] * df["Volume"]
    # create the negative money flow feature
    df["Negative Money Flow"] = df.loc[df.pos_neg < 0]["Typical Price"] * df["Volume"]

    # using rolling windows caclulation to create postive money flow sum feature
    df['Positive Money Flow Sum']=df['Positive Money Flow'].rolling(window=n, min_periods=0).sum()
    # take the first 10 observations and replace them with missing values
    df.loc[: n-1,'Positive Money Flow Sum'] = np.nan
    
    # same applies to negative money flow sum feature
    df['Negative Money Flow Sum']=df['Negative Money Flow'].rolling(window=n, min_periods=0).sum()
    df.loc[: n-1,'Negative Money Flow Sum'] = np.nan

    # geenrate feature money ratio
    df['money_ratio'] = df['Positive Money Flow Sum'] / df['Negative Money Flow Sum']
    # calculate the money flow index
    df['Money Flow Index'] = 100 * (df['money_ratio']) / (1+df['money_ratio']) 
    
    # delete the needless features
    del_col = ["pos_neg", "money_ratio"]
    df.drop(del_col, axis = 1, inplace = True)
    
    # output the result in the right format
    output_filename = ('money_flow_index_' + str(n) + ".csv")
    # output dataframe into csv file
    df.to_csv(output_filename, index=False, header=True)


moneyFlowIndex(filename, n)
