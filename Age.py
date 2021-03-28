import pandas as pd
df = pd.read_csv("Age W2.csv",header=2)
n=3
df.drop(df.tail(n).index, inplace = True)
a=df["Age"]=="18 - 24"
b=df.loc[a]
sconv=b["Conversions"].sum()
scos=b["Cost"].sum()
sCPA=scos/sconv

c=df["Age"]=="25 - 34"
d=df.loc[c]
mconv=d["Conversions"].sum()
mcos=d["Cost"].sum()
mCPA=mcos/mconv

e=df["Age"]=="35 - 44"
f=df.loc[e]
tconv=f["Conversions"].sum()
tcos=f["Cost"].sum()
tCPA=tcos/tconv

g=df["Age"]=="45 - 54"
h=df.loc[g]
wconv=h["Conversions"].sum()
wcos=h["Cost"].sum()
wCPA=wcos/wconv

i=df["Age"]=="55 - 64"
j=df.loc[i]
thconv=j["Conversions"].sum()
thcos=j["Cost"].sum()
thCPA=thcos/thconv

k=df["Age"]=="65+"
l=df.loc[k]
fconv=l["Conversions"].sum()
fcos=l["Cost"].sum()
fCPA=fcos/fconv

y=df["Age"]=="Unknown"
z=df.loc[y]
saconv=z["Conversions"].sum()
sacos=z["Cost"].sum()
saCPA=sacos/saconv

print("18-24 Conversion:", sconv)
print("25-34 Conversion:", mconv)
print("35-44 Conversion:", tconv)
print("45-54 Conversion:", wconv)
print("55-65 Conversion:", thconv)
print("65+ Conversion:", fconv)
print("Unknown Conversion:", saconv)
print('')
print('CPA')
print('')
print("18-24 CPA $:", sCPA)
print("25-34 CPA $:", mCPA)
print("35-44 CPA $:", tCPA)
print("45-54 CPA $:", wCPA)
print("55-65 CPA:", thCPA)
print("65+ CPA $:", fCPA)
print("Unknown CPA $:", saCPA)
print('')
print('Margin: 0.7')
print('')
print("18-24 CPA $:", sCPA/0.7)
print("25-34 CPA $:", mCPA/0.7)
print("35-44 CPA $:", tCPA/0.7)
print("45-54 CPA $:", wCPA/0.7)
print("55-65 CPA:", thCPA/0.7)
print("65+ CPA $:", fCPA/0.7)
print("Unknown CPA $:", saCPA/0.7)