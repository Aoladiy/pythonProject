import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv('https://raw.githubusercontent.com/koroteevmv/ML_course/main/ML1.1_sgd/data/x.csv', index_col=0)['0']
y = pd.read_csv('https://raw.githubusercontent.com/koroteevmv/ML_course/main/ML1.1_sgd/data/y.csv', index_col=0)['0']


class Model:
    """Модель парной линейной регрессии"""

    def __init__(self):
        self.b0 = 0
        self.b1 = 0
        self.steps = []
        self.errors = []

    def third_task(self, x, y):
        if isinstance(x, pd.DataFrame):
            x = pd.Series(x.iloc[:, 0])
        if isinstance(y, pd.DataFrame):
            y = pd.Series(y.iloc[:, 0])
        return x, y

    def plot(self, x, y):
        x, y = self.third_task(x, y)
        Y_pred = self.predict(x)
        plt.scatter(x, y)
        plt.plot(x, Y_pred, color='red')
        plt.show()

    def plot_learning_curves(self):
        plt.plot(self.steps, self.errors, color='green')
        plt.show()

    def predict(self, x):
        x, _ = self.third_task(x, None)
        Y = self.b0 + self.b1 * x
        return Y

    def error(self, x, y):
        x, y = self.third_task(x, y)
        return sum((self.predict(x) - y) ** 2) / (2 * len(x))

    def fit(self, x, y, alpha=1, accuracy=0.01, max_steps=10000, decrease=2):
        x, y = self.third_task(x, y)

        step = 0
        prev_error = 0
        increase_count = 0
        while True:
            new_err = hyp.error(x, y)
            if abs(prev_error - new_err) < accuracy:
                print(f"Reached desired accuracy after {len(self.steps)} steps")
                break
            prev_error = new_err

            dJ0 = sum(self.predict(x) - y) / len(x)
            dJ1 = sum((self.predict(x) - y) * x) / len(x)
            self.b0 -= alpha * dJ0
            self.b1 -= alpha * dJ1

            step += 1
            self.steps.append(step)
            self.errors.append(new_err)
            # if len(self.steps) == 1 and new_err > prev_error:
            #     increase_count += 1
            # elif increase_count == 1 and new_err > prev_error:
            #     alpha /= decrease
            #     self.b0 = 0
            #     self.b1 = 0
            #     self.steps = []
            #     prev_error = 0
            #     increase_count = 0
            # else:
            #     increase_count = 0  # сброс счетчика, если ошибка не увеличивается

            if len(self.steps) == max_steps:
                print("Reached maximum number of steps")
                break
        return self.steps, self.errors


hyp = Model()
hyp.fit(x, y)
J = hyp.error(x, y)
print("error after gradient descent:", J)
hyp.plot(x, y)
hyp.plot_learning_curves()

