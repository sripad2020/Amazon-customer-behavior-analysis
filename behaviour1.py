import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
data=pd.read_csv('Amazon Customer Behavior Survey.csv')
print(data.columns)
print(data.info())
print(data.isna().sum())
print(data.describe())
'''for i in data.columns.values:
    if len(data[i].value_counts())<=5:
        sn.countplot(data[i])
        plt.show()'''''

male=data[data['Gender']=='Male']
female=data[data['Gender']=='Female']
trans=data[data['Gender']=='Others']
nogen=data[data['Gender']=='Prefer not to say']


'''for i in male.columns.values:
    index=male[i].value_counts().index.values
    val=male[i].value_counts().values
    if (len(index) and len(val)) <=10:
        plt.pie(val,labels=index,autopct='%1.1f%%')
        plt.title('the values and their counts ')
        plt.legend()
        plt.show()'''


'''lab=LabelEncoder()
for i in male.select_dtypes(include='object').columns.values:
    male[i]=lab.fit_transform(male[i])

for i in female.select_dtypes(include='object').columns.values:
    female[i]=lab.fit_transform(female[i])

for i in trans.select_dtypes(include='object').columns.values:
    trans[i]=lab.fit_transform(trans[i])

for i in nogen.select_dtypes(include='object').columns.values:
    nogen[i]=lab.fit_transform(nogen[i])'''



print(male['Personalized_Recommendation_Frequency '].value_counts())
print(male.columns)
print(male['Purchase_Categories'].value_counts())
print('-----------------------------------------')
print(male['Improvement_Areas'].value_counts())
print('------------------------------------------')
print(male['age'].value_counts().index.values)

btw5_25=data[(data['age']>=0)&(data['age']<=27)]

btw25_35=data[(data['age']>=28)&(data['age']<=35)]

btw35_47=data[(data['age']>=36)&(data['age']<=47)]

btw47_57=data[(data['age']>=48)&(data['age']<=60)]

for i in btw5_25.select_dtypes(include='number').columns.values:
    for j in btw5_25.select_dtypes(include='number').columns.values:
        sn.histplot(btw5_25[i], label=f"{i}", color='red')
        sn.histplot(btw5_25[j], label=f"{j}", color="blue")
        plt.title(f" {i} vs {j} in between age group of 5 and 25 category")
        plt.legend()
        plt.show()


'''plt.figure(figsize=(17, 6))
corr = male.corr(method='spearman')
my_m = np.triu(corr)
sn.heatmap(corr, mask=my_m, annot=True, cmap="Set2")
plt.show()


sn.pairplot(male)
plt.show()

for i in male.select_dtypes(include='number').columns.values:
    for j in male.select_dtypes(include='number').columns.values:
        sn.histplot(male[i], label=f"{i}", color='red')
        sn.histplot(male[j], label=f"{j}", color="blue")
        plt.title(f" {i} vs {j} in male category")
        plt.legend()
        plt.show()

for i in male.select_dtypes(include='number').columns.values:
    for j in male.select_dtypes(include='number').columns.values:
        sn.distplot(male[i], label=f"{i}", color='red')
        sn.distplot(male[j], label=f"{j}", color="blue")
        plt.title(f"{i} vs {j} in male category")
        plt.legend()
        plt.show()'''