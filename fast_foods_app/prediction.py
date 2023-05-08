import pandas
import numpy as np
from sklearn.linear_model import LinearRegression

def train():
    dataframe = pandas.read_csv("./fastfood.csv")

    dataframe.head()
    dataframe.info()
    dataframe.describe()

    data = dataframe
    train_set = data[:int(len(data)*0.7)]
    train_x = train_set[['calories']]
    train_y = train_set[['cholesterol']]
    test_set = data[int(len(data)*0.7):]
    test_x = test_set[['calories']]
    test_y = test_set[['cholesterol']]

    model = LinearRegression()
    model.fit(train_x.values, train_y.values)

    #predicted_list = model.predict(test_x.values)
    #print(predicted_list)

    squared_error = 0
    for sample_x,sample_y in zip(test_x['calories'], test_y['cholesterol']):
        predicted_value = model.predict(np.array([[sample_x]]))
        print("predicted: {}, expected: {}".format(predicted_value, sample_y))
        error = predicted_value[0][0] - sample_y
        squared = error * error
        squared_error += squared
    mean_squared_error = squared_error / len(test_y)
    print(mean_squared_error)
    return model, mean_squared_error

if __name__ == '__main__':
    train()
