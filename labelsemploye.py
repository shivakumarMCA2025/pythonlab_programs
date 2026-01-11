import pandas as pd

data={
    'name':["A","B","C"],
'salary':[50000,65000,45000]

}

df=pd.DataFrame(data)

#without inbuilt function (high=df[df['salary']>60000])

print("mean",df['salary'].mean())
print("avg",sum(df['salary'])/len(df['salary']))
#print("highest",high)