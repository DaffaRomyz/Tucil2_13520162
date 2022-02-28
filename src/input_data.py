import pandas as pd
from sklearn import datasets

def data(select):
    if select == 1:
        print("Data = iris")
        data = datasets.load_iris()
    elif select == 2:
        print("Data = wine")
        data = datasets.load_wine()
    elif select == 3:
        print("Data = breast_cancer")
        data = datasets.load_breast_cancer()
    else:
        print("Data = iris")
        data = datasets.load_iris()
    return data

#create a DataFrame
def dataframe(data):
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    df.head()
    return df