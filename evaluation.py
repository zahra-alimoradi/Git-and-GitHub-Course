
import random

total_error = 0

for i in range(100):
    y_test = random.random()
    y_pred = random.random()

    error = y_test - y_pred
    total_error += error

print("Mean Error:", total_error / 100)