import pandas as pd
df=pd.read_csv("data.csv")
df.head(10)

df.tail(5)

df.info()

df.columns

df.describe()

df.isnull().sum()

employee=['Department','Gender','Age']
df['Total']=df[employee].sum(axis=0)
df[['EmployeeName','Department','Gender','YearsExperience']].tail()

df['Average']=df[['Age','MonthlyIncome','JobSatisfaction','WorkLifeBalance']].mean(axis=1)
df[['EmployeeName','Average']].head(5)

def grade(avg):
  if avg>=29000:
    return'30000'
  elif avg>=49000:
    return'40000'
  elif avg>=68687:
    return'70000'
  elif avg>=11765:
    return'12000'
  else:
    return'140000'
df['Grade']=df['Average'].apply(grade)
df[['EmployeeName','Average','Grade']].head(7)

df['MonthlyIncome'].mean()

df['WorkLifeBalance'].max()

df['WorkLifeBalance'].min()

df[df['MonthlyIncome']>70000]

import matplotlib.pyplot as plt
MonthlyIncome_avg = df.groupby('EmployeeName')['MonthlyIncome'].mean()
plt.figure(figsize=(15,10))
colors=['pink','yellow','red','blue','gray','green']
MonthlyIncome_avg.head(6).plot(kind='bar',color=colors)
plt.title('Average MonthlyIncome by EmployeeName')
plt.xlabel('EmployeeName')
plt.ylabel('Average MonthlyIncome')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()