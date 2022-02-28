import pandas as pd
from sklearn import datasets

def data():
    data = datasets.load_iris()
    return data;

#create a DataFrame
def dataframe(data):
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    df.head()
    return df