#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import os
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
datapath = "."
trainfile = os.path.join(datapath ,"train_sample.csv")
output = "output"
df = pd.read_csv(trainfile,dtype={"C15":str,"C16":str})
'''
result = df[["C14","C15","C16","C17","C18","C19","C20","C21"]].describe()

with open("train_sample_describe.csv","w") as f:
    pd.SparseDataFrame(result).to_csv(f)
'''
def getweekday(x):
    '''
    :param date: YYMMDD
    :return: weekday
    '''
    sdt = str(x)
    year = int(sdt[0:2])
    month = int(sdt[2:4])
    day = int(sdt[4:6])
    dt = datetime.date(year, month, day)
    weekday = dt.weekday()
    return weekday
df.info()
'''

print(df["click"].mean())
print("################")
print(df["C1"].value_counts())
print("################")
print(df["banner_pos"].value_counts())
print("################")
print(df["site_id"].value_counts())
print("################")
print(df["site_domain"].value_counts())
print("################")
print(df["site_category"].value_counts())
print("################")
print(df["app_id"].value_counts())
print("################")
print(df["app_domain"].value_counts())
print("################")
print(df["app_category"].value_counts())
print("################")
print(df["device_ip"].value_counts())
print("################")
print(df["device_model"].value_counts())
print("################")
print(df["device_type"].value_counts())
print("#########group by column #######")
group = df["click"].groupby(df["device_type"])
print(group.mean())
print("################")
print(df["device_conn_type"].value_counts())
print("################")
print(df["C15"].value_counts())
print(df["C16"].value_counts())
print(df["C17"].value_counts())
print(df["C18"].value_counts())
print(df["C19"].value_counts())
print(df["C20"].value_counts())
print(df["C21"].value_counts())
print("################")
'''
#建立新的特征列

df["size"] = df["C15"].str.cat(df["C16"],sep="_")
#将hour列拆分为
df["hour1"] = df["hour"].map(lambda x:str(x)[6:8])
df["day"] = df["hour"].map(lambda x:str(x)[4:6])
df["weekday"] = df["hour"].map(lambda x:getweekday(x))

df = df.drop(["id","site_id","app_id","hour","C15","C16"],axis=1)
#生成新的数据集
train_new =os.path.join(output, "train_new.csv")
print(train_new)
with open(train_new,"w") as newtrain:
    df.to_csv(newtrain,index=False,header=True)
