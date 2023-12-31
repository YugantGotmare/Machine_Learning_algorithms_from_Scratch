import numpy as np


def Sigmoid(x):
    return 1/(1 + np.exp(-x))


class LogisticRegression():

    def __init__(self, lr= 0.001, n_iters=1000):
        self.lr = lr 
        self.n_iters = n_iters
        self.weights = None
        self.bais = None 

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bais = 0

        for _ in range(self.n_iters):
            linear_pred = np.dot(X, self.weights) + self.bais
            predictions = Sigmoid(linear_pred)

            dw = (1/n_samples) * np.dot(X.T, (predictions - y))
            db = (1/n_samples) * np.sum(predictions - y)

            self.weights = self.weights - self.lr * dw
            self.bais = self.bais - self.lr * db 

    
    def predict(self, X):
        linear_pred = np.dot(X, self.weights) + self.bais
        y_pred = Sigmoid(linear_pred)
        class_pred = [0 if y<=0.5 else 1 for y in y_pred]
        return class_pred

