import pandas as pd

data={
    "name":["shivu","charlie","ashi"],
    "marks":[20,30,40]

}

df=pd.DataFrame(data)

print("avg",df['marks'].mean())
print("mininum",df['marks'].min())
print("maximum",df['marks'].max())