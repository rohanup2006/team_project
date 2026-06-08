import pandas as pd 
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
def add(a, b):
    return a + b
print(add(df['a'], df['b']))