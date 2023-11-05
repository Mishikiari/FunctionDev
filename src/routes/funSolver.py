# server.py
from flask import Flask, request, jsonify
from sympy import symbols, diff, lambdify
import matplotlib.pyplot as plt
import numpy as np

app = Flask(FunctionDev)

@app.route('/calculate_derivative', methods=['POST'])
def calculate_derivative():
    data = request.get_json()
    expression = data['expression']
    x = symbols('x')
    
    derivative = diff(expression, x)
    
    func = lambdify(x, derivative, 'numpy')

    x_values = np.linspace(-10, 10, 400)
    y_values = func(x_values)

    plt.plot(x_values, y_values, label='Function')
    plt.plot(x_values, np.gradient(y_values, x_values[1]-x_values[0]), label='Derivative')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')

    plt.grid()
    plt.savefig('static/plot.png')
    plt.close()

    return jsonify({'derivative': str(derivative)})

if __name__ == '__main__':
    app.run()
