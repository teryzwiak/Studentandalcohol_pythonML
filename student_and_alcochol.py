# import wykorzystywanych bibliotek
#from sklearn.model_selection import train_test_split
#from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics
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


train_test_list = np.array(model.model_division(X, y))
print(train_test_list)
model.linear_regression(train_test_list[0], train_test_list[2], train_test_list[1])
#model.linear_regression(model.X_train, model.y_train, model.X_test)
model.random_forest_regressor(model.X_train, model.y_train, model.X_test)
model.compare_models(model.accuracy_compare)