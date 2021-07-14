import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from NeuralNetwork import NeuralNetwork
from layers import Layer, ActivationLayer, tanh, tanh_der, sigmoid, sigmoid_der, relu, relu_der


from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, f1_score)

from mlxtend.data import loadlocal_mnist
from sklearn.metrics import classification_report

def conver_number_to_vector(y):
    """Zamiana liczby z przedziału 0-9 na wektor
    np. liczba 1 wygląda następująco [0, 1, 0, , 0, 0, 0, 0, 0, 0]"""
    y1 = np.zeros((len(y),10))
    for i in range(len(y)):
        y1[i][y[i]] = 1
    y = y1
    return y


def load_data():
    """Wczytanie danych trenigowych i testowych oraz ich znormalizowanie """
    x_train, y_train = loadlocal_mnist(
            images_path='train-images.idx3-ubyte', 
            labels_path='train-labels.idx1-ubyte')
    x_train = x_train.reshape(x_train.shape[0], 1, 28*28)
    x_train = x_train.astype('float32')
    x_train /= 255
    y_train = conver_number_to_vector(y_train)
    
    x_test, y_test = loadlocal_mnist(
        images_path='t10k-images.idx3-ubyte', 
        labels_path='t10k-labels.idx1-ubyte')
    x_test = x_test.reshape(x_test.shape[0], 1, 28*28)
    x_test = x_test.astype('float32')
    x_test /= 255
    return x_train, y_train, x_test, y_test


def build_network(layers=None):
    """Zbudowanie kąpletniej sieci neuronowej o domyślnej liczbie warst równej 3"""
    x_train, y_train, x_test, y_test = load_data() 
    network = NeuralNetwork()
    network.add(Layer(28*28, 100))                
    network.add(ActivationLayer(tanh, tanh_der))
    network.add(Layer(100, 50))                   
    network.add(ActivationLayer(tanh, tanh_der))
    if layers is not None:
        if layers == 4 or layers ==5:
            network.add(Layer(50, 50))                   
            network.add(ActivationLayer(tanh, tanh_der))
        if layers == 5:
            network.add(Layer(50, 50))                   
            network.add(ActivationLayer(tanh, tanh_der))        
    network.add(Layer(50, 10))                    
    network.add(ActivationLayer(tanh, tanh_der))
    network.train(x_train, y_train, learning_rate=0.1)
    predicted_values = network.test(x_test)
    return predicted_values, y_test


def confusion_Matrix(true, pred):
    """Wyznaczenie macierzy błędów oraz miar"""
    target = [0,1,2,3,4,5,6,7,8,9]
    print('\nAccuracy: {:.2f}\n'.format(accuracy_score(true,
                                                        pred)))
    print('Micro Precision: {:.2f}'.format(precision_score(true,
                                            pred, average='micro')))
    print('Micro Recall: {:.2f}'.format(recall_score(true, pred,
                                        average='micro')))
    print('Micro F1-score: {:.2f}\n'.format(f1_score(true,
                                            pred, average='micro')))
    print('Macro Precision: {:.2f}'.format(precision_score(true,
                                            pred, average='macro')))
    print('Macro Recall: {:.2f}'.format(recall_score(true, pred,
                                        average='macro')))
    print('Macro F1-score: {:.2f}\n'.format(f1_score(true, pred,
                                            average='macro')))
    print('Weighted Precision: {:.2f}'.format(precision_score(true,
            pred, average='weighted')))
    print('Weighted Recall: {:.2f}'.format(recall_score(true,
                                            pred, average='weighted')))
    print('Weighted F1-score: {:.2f}'.format(f1_score(true, pred,
                                                average='weighted')))
    print('\nClassification Report\n')

    print(classification_report(true, pred))
    confusion = confusion_matrix(true, pred)
    fig = plt.figure(dpi=80)
    ax = fig.add_subplot(1, 1, 1)
    table = ax.table(cellText=confusion, loc='best',
                        rowLabels=target, colLabels=target)
    table.set_fontsize(14)
    table.scale(1, 4)
    ax.axis('off')
    plt.show()

pred, true = build_network()
confusion_Matrix(true, pred)
