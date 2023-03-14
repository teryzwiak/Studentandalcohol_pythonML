from sklearn.model_selection import train_test_split
from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics
import numpy as np
import pandas as pd

class model:
    def model_division(X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12345) 
        return X_train, X_test, y_train, y_test
        #return train_test_list
    
    def train_model(classifier, feature_vector_train, label, feature_vector_valid):
        # trenuj model
        classifier.fit(feature_vector_train, label)
        
        with open('titanic_classifier.pickle', 'wb') as handle:
            pickle.dump(classifier, handle)
        
        # wygeneruj przewidywania modelu dla zbioru testowego
        predictions = classifier.predict(feature_vector_valid)
        
        # dokonaj ewaluacji modelu na podstawie danych testowych
        score_vals = [
            metrics.mean_squared_error(predictions, model.y_test),
            metrics.mean_absolute_error(predictions, model.y_test)
        ]
        return score_vals

    def linear_regression(X_train, y_train, X_test):
        accuracy = model.train_model(linear_model.LinearRegression(), X_train, y_train, X_test)
        accuracy_compare = {'LR': accuracy}

        print ("LR: ", accuracy)

        return accuracy, accuracy_compare

    def random_forest_regressor(X_train, y_train, X_test):
        from sklearn.ensemble import RandomForestRegressor
        regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)
        accuracy = model.train_model(regressor, X_train, y_train, X_test)
        model.accuracy_compare['random forrest tree'] = accuracy

        print ('random forrest tree' , accuracy)

        return accuracy

    def correcting(X_train, y_train, X_test):
        from sklearn.ensemble import RandomForestRegressor
        regressor = RandomForestRegressor(n_estimators = 200, random_state = 0)
        accuracy = model.train_model(regressor, X_train, y_train, X_test)
        model.accuracy_compare['random forrest tree'] = accuracy
        print ('random forrest tree' , accuracy)

    def compare_models(accuracy_compare):
        df_compare = pd.DataFrame(accuracy_compare, index = ['mse', 'mae'])
        df_compare.plot(kind='bar')

