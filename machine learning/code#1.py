import matplotlib.pyplot as plt
import numpy as np
from sklearn import model_selection
from sklearn import linear_model

x = range(0, 10)
y = [1.8 * F + 32 for F in x]

print(x)
print(y)

plt.plot(x, y, '-*g')
plt.show()

x = np.array(x).reshape(-1, 1)
y = np.array(y).reshape(-1, 1)

xTrain, xTest, yTrain, yTest = model_selection.train_test_split(x, y, test_size=0.2)


model = linear_model.LinearRegression()  
model.fit(xTrain, yTrain)
print (model.coef_)
print (model.intercept_)
accuracy = model.score(xTrain, yTrain)
print(accuracy * 100)
