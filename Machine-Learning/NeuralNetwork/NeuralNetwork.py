import numpy as np 

class NeuralNetwork:
    def __init__(self):
        self.layers = []

    def add(self, layer):
        """Dodanie nowej warstwy do sieci"""
        self.layers.append(layer)
    
    def loss_der_function(self, y_true, y_pred):
        """Obliczenie pochodnej funkcji błędu. """
        self.loss_der = 2*(y_pred-y_true)/y_true.size
        return self.loss_der

    def train(self, x_train, y_train, learning_rate):
        """Uczenie sieci neuronowych"""
        for i in range(len(x_train)):
            output = x_train[i]
            for layer in self.layers:
                output = layer.forward(output)
            error = self.loss_der_function(y_train[i], output)
            for layer in reversed(self.layers):
                error = layer.backward(error, learning_rate)
        
    def test(self, input_data):
        """Funkcja sprawdzająca poprawność działania sieci. """
        result = []
        for i in range(len(input_data)):
            output = input_data[i]
            for layer in self.layers:
                output = layer.forward(output)
            predicted_value = np.argmax(output)
            result.append(predicted_value)
        return result


