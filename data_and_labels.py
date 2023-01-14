class data_and_labels:
    def gen_data(students):
        X = students.drop(['G3'], axis=1).to_numpy()
        #X
        return X

    def gen_label(students):
        y = students.loc[:, 'G3'].to_numpy()
        return y