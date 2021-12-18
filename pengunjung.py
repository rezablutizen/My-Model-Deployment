import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def pengunjung_prediction(hrs):

    df = pd.read_csv("disparbud-od_15367_jml_pengunjung_ke_objek_wisata__jenis_wisatawan_data.csv")
    X = df[['tahun']]
    y = df[['jumlah_pengunjung']]

    X = X.values
    y = y.values

    model = LinearRegression()
    model.fit(X,y)

    X_test = np.array(hrs)
    X_test = X_test.reshape((1,-1))

    return model.predict(X_test)


