# -*- coding: utf-8 -*-
"""
    Programmer: Mpumelelo Ntobi
    Date: Thu Feb 16 17:23:12 2023
    
    Writing code makes me happy.
"""

# Import library
import matplotlib.pyplot as plt

import sys


def main():
    # Toy data 
    raw_data = { 
        "predictor": [5, 7, 8, 7, 2, 9, 4, 11, 12, 9, 6],
        "response": [99, 86, 87, 88, 111, 87, 94, 78, 77, 85, 86]
    }

    data = raw_data.copy()

    # Sort the data
    temp_data = list(zip(data["predictor"], data["response"]))
    temp_data = sorted(temp_data, key=lambda element: element[0])
    
    data["predictor"], data["response"] = [list(_) for _ in list(zip(*temp_data))]
    
    ulr = UnivariateLinearRegression()
    ulr.fit(data["predictor"], data["response"])
    y_hat = ulr.predict(raw_data["predictor"])


    # Plot the sorted data
    plt.scatter(x=data["predictor"], y=data["response"])
    plt.scatter(x=raw_data["predictor"], y=y_hat) 
    

class UnivariateLinearRegression():
    def __init__(self):
        self.coefficient = None
        self.intercept = None
        self.mse = None


    def fit(self, x, y):
        numerator = 0
        denominator = 0
        sum_se = 0
        for x_i, y_i in zip(x, y):
            numerator += (x_i - self.mean(x)) * (y_i - self.mean(y))
            denominator += (x_i - self.mean(x)) ** 2
            
        self.coefficient = numerator / denominator
        self.intercept = self.mean(y) - (self.coefficient * self.mean(x))
        
        for x_i, y_i in zip(x, y):
            sum_se += (y_i - self.predict(x_i)) ** 2
        self.mse = sum_se / len(y)
        


    def predict(self, x):
        if type(x) == float or type(x) == int:
            return self.y_hat(x)
        elif type(x) == list:
            predictions = []
            for i, x_i in enumerate(x):
                if type(x_i) == float or type(x_i) == int:
                    predictions.append(self.y_hat(x_i))
                else:
                    sys.exit("Invalid input.")
            return predictions
        else:
            sys.exit("Invalid input.")
            
            
    # Helper module
    def y_hat(self, x):
        return (self.coefficient * x) + self.intercept
    
    
    def mean(self, arr):
        try:
            return sum(arr) / len(arr)
        except:
            sys.exit("Invalid input.")


if __name__ == "__main__":
    main()