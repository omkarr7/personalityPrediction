import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

columns = ['email','EXT1','EXT2','EXT3','EXT4','EXT5','EXT6','EXT7','EXT8','EXT9','EXT10','EST1','EST2','EST3',
'EST4','EST5','EST6','EST7','EST8','EST9','EST10','AGR1','AGR2','AGR3','AGR4','AGR5','AGR6','AGR7','AGR8','AGR9',
'AGR10','CSN1','CSN2','CSN3','CSN4','CSN5','CSN6','CSN7','CSN8','CSN9','CSN10',
'OPN1','OPN2','OPN3','OPN4','OPN5','OPN6','OPN7','OPN8','OPN9','OPN10']

with open('persona.pickle','rb') as f:
    k_fit = pickle.load(f)
    print('loaded succesfully')

def get_info(email):
    sheet_id = 'Your sheet id here'
    sheet_name = "Personality Prediction (Responses)"
    start_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    url = start_url.replace(" ","")

    df = pd.read_csv(url)

    df1 = df.copy()
    df2 = df1.fillna(method='bfill')
    df3 = df2.drop('Timestamp',axis='columns')
    df3.columns = columns

    df4 = df3.loc[df3['email'] == email]
    df5 = df4.drop('email',axis='columns')
    my_personality = k_fit.predict(df5)
    col_list = df5.values.tolist()
    ext = col_list[0][0:10]
    est = col_list[0][10:20]
    agr = col_list[0][20:30]
    csn = col_list[0][30:40]
    opn = col_list[0][40:50]

    Ext  = []
    Est  = []
    Agr  = []
    Csn  = []
    Opn  = []


    for i in ext:
      Ext.append(int(i))
    for i in est:
      Est.append(int(i))
    for i in agr:
      Agr.append(int(i))
    for i in csn:
      Csn.append(int(i))
    for i in opn:
      Opn.append(int(i))
    # ext = make_int(ext,Ext)
    my_sums = pd.DataFrame()
    my_sums['extroversion'] = [((sum(Ext)/10)/5)*100]
    my_sums['neurotic'] = [((sum(Est)/10)/5)*100]
    my_sums['agreeable'] = [((sum(Agr)/10)/5)*100]
    my_sums['conscientious'] = [((sum(Csn)/10)/5)*100]
    my_sums['open'] = [((sum(Opn)/10)/5)*100]
    my_sums['cluster'] = my_personality
    return my_sums

