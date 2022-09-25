import pandas as pd
def degprofane(ele):
#     for ele in raw['tweet']:
    count=0
    s=[x for x in ele.split()]
    for i in range(len(s)):
        if s[i] in parse:
            count=count+1
#             print("profane word"+s[i])
            s[i]="x"*len(s[i])
    return count
def profane(ele):
    count=0
    s=[x for x in ele.split()]
    for i in range(len(s)):
        if s[i] in parse:
            s[i]="x"*len(s[i])
    return " ".join(str(x) for x in s)


raw=pd.read_csv("labeled_data.csv")
print(raw.head())
print(raw.columns)
print(raw.info())
print(raw.describe())
raw=raw.drop(['Unnamed: 0', 'count', 'hate_speech', 'offensive_language', 'neither','class'],axis=1)
print(raw.columns)
print(raw.head())
import json
f=open('words.json',encoding="utf8")
parse=json.load(f)
raw['degree of profanity']=raw['tweet'].apply(degprofane)
raw['retweets']=raw['tweet'].apply(profane)
raw.to_csv('censored tweets.csv')