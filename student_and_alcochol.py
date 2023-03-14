# import wykorzystywanych bibliotek
from sklearn.model_selection import train_test_split
from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import pickle
#import seaborn as sns
#import klas
from analyze_statistics_data import analyze_statistics_data
from del_not_using_data import del_not_using_data
from variable_map import variable_map
from plt_show import plt_show
from correlations import correlations
from data_and_labels import data_and_labels
from model import model

#importowanie csv do ramki danych
students = pd.read_csv('student-mat.csv')
students.head(50)

analyze_statistics_data.analyze(students)
del_not_using_data.del_columns(students)
variable_map.map(students)
plt_show.show(students)
correlations.show(students)
X = data_and_labels.gen_data(students)
y = data_and_labels.gen_label(students)



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12345) 

#model.linear_regression(X_train, y_train, X_test)
#model.random_forest_regressor(X_train, y_train, X_test)
#model.compare_models(model.accuracy_compare)
def train_model(classifier, feature_vector_train, label, feature_vector_valid):
    # trenuj model
    classifier.fit(feature_vector_train, label)
    
    with open('titanic_classifier.pickle', 'wb') as handle:
        pickle.dump(classifier, handle)
    
    # wygeneruj przewidywania modelu dla zbioru testowego
    predictions = classifier.predict(feature_vector_valid)
    
    # dokonaj ewaluacji modelu na podstawie danych testowych
    score_vals = [
        metrics.mean_squared_error(predictions, y_test),
        metrics.mean_absolute_error(predictions, y_test)
    ]
    return score_vals

# MODEL 1 - regresja liniowa
accuracy = train_model(linear_model.LinearRegression(), X_train, y_train, X_test)
accuracy_compare = {'LR': accuracy}
print ("LR: ", accuracy)

# MODEL 2 - RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)
accuracy = train_model(regressor, X_train, y_train, X_test)
accuracy_compare['random forrest tree'] = accuracy
print ('random forrest tree' , accuracy)

df_compare = pd.DataFrame(accuracy_compare, index = ['mse', 'mae'])
df_compare.plot(kind='bar')

regressor.predict([[18,2,2,0,1,0,0,0,1,1,0,0,3,4,1,1,3,6, 19, 19]]) #prawidłowa wartość 15

# działania korygujące - hiperparametry

# MODEL 3 - RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 200, random_state = 0)
accuracy = train_model(regressor, X_train, y_train, X_test)
accuracy_compare['random forrest tree'] = accuracy
print ('random forrest tree' , accuracy)

df_compare = pd.DataFrame(accuracy_compare, index = ['mse', 'mae'])
df_compare.plot(kind='bar')

regressor.predict([[18,2,2,0,1,0,0,0,1,1,0,0,3,4,1,1,3,6, 15, 16]]) #prawidłowa wartość 15

import pickle
s = pickle.dumps(regressor)
clf = pickle.loads(s)
clf.predict(X[0:1])

with open('alcholic_regressor_model.pickle', 'wb') as handle:
    pickle.dump(clf, handle)