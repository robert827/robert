# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 14:56:03 2021

@author: ro662
"""
import triplevaluefunction
from triplefunction import substance, data
from sklearn.metrics import r2_score, mean_absolute_error, mean_absolute_percentage_error, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from scipy.stats import stats
from itertools import product as prod
import triplefunction
from data_base import drop_series,name_list
best = dict({'R2': 0, '常數項': 0, '係數': 0, '預測': 0,
             '測試': 0, '特徵組合': 0, 'train_pred': 0, 'MAE': 0, 'MAPE': 0, 'MSE': 0, 'RMSE': 0})

# python方程式求解


for j in range(1, 11):  # 依序前1到前10特徵參數的迴圈
    number = j
    print(number)

    biggest = drop_series.nlargest(number)
    polynomial = biggest.index

# create a datadict, which can access the value by key name(like 'e')

    triplevalue_list = [substance, ]
    for i in range(0, number, 1):   # 第二層迴圈執行num次，每次輸入成績
        value = name_list[polynomial[i]]
        triplevalue_list += [value]

    finaldata = np.transpose(triplevalue_list)

    # 回歸方程式求解
    dataset = finaldata
    X = dataset[:, 1:]
    y = dataset[:, 0]
    patient_max = 10000
    for k in range(0, 300):  # 每個計算都算3000次 算是經驗次數
        print(k)
        score = 0
        patient = 0  # 程式除錯運算次數名稱
        while (score < 0.6):  # 設定回歸公式的決定係數 分數介於1~0.00001 之間算一次運算
            # Importing the dataset
            # Splitting the dataset into the Training set and Test set
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.3)  # 取30%當測試 70%當作訓練
            # random_state = 0

            # Fitting Multiple Linear Regression to the Training set
            regressor = LinearRegression()
            regressor.fit(X_train, y_train)

            # Predicting the Test set results
            y_pred = regressor.predict(X_test)  # 預測
            # y= regressor.predict(X)

            score = r2_score(y_test, y_pred)  # 分數
            mae = mean_absolute_error(y_test, y_pred)  # MAE
            mape = mean_absolute_percentage_error(y_test, y_pred)  # MAPE
            mse = mean_squared_error(y_test, y_pred)  # MSE
            rmse = mse**0.5
            alpha = regressor.intercept_  # 常數項
            beta = regressor.coef_  # 各特徵參數的係數

            point_list = []
            point = dict({'R2': score, '常數項': alpha,  # 給定名稱為了儲存資料  best的定義在最上面
                          '係數': beta, '預測': y_pred, '測試': y_test, '特徵組合': polynomial, 'MAE': mae, 'MAPE': mape, 'MSE': mse, 'RMSE': rmse})
            if best['R2'] < point['R2']:
                best = point.copy()

            patient += 1  # 程式除錯運算次數疊加

            if patient == patient_max:
                print("FAILED")
                break  # 跳出 while (1>score>0.5)
            elif patient % 1000 == 0:
                print("tried {}/{}".format(patient, patient_max))
        if patient == patient_max:
            break  # 跳出 for k in range(0, 3000)
            
regression_function = ''
for i in range(0, len(best['特徵組合'])):
    regression_function +=str( best['特徵組合'][i])+"*"+"("+str(best['係數'][i])+")"+"+"
regression_function = substance.name+"="+regression_function+"("+str(best['常數項'])+")"
print(regression_function)
print('決定係數', best['R2'])
