import csv 
import random
import math
import numpy as np  
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import classification_report
class NaiveBayes:
    def __init__(self,filename, proportion=0.6):
        self.filename = filename
        self.classes = []
        self.test = [] 
        self.mean = []
        self.true = []
        self.pred = []
        self.proportion = proportion
        self.load_data()
    def load_data(self):
        """Załadowanie pliku"""
        self.data = csv.reader(open(self.filename, "rt")) 
        self.data = list(self.data)  
    def random_data(self):
        """Funkcja mieszająca dane """
        random.shuffle(self.data)
    def data_conversion(self):
        """Zamiana typu danych z tekstowego na liczbowy 
        oraz nazw gatunków na liczby reprezentującce te nazwy """
        i = 0 
        for data in self.data:
            if data[-1] not in self.classes: #Jeśli gatunek pojawił się 1 raz dodaajemy go do listy
                self.classes.append(data[-1])
            data[-1] = self.classes.index(data[-1]) #Zastępujemy nazwę gatunku numerem jego indeksu w liście classes
            for x in range(len(self.data[i])): 
                self.data[i][x] = float(self.data[i][x])
            i += 1 
    def test_and_traing_set(self):
        """Podzaił zbioru danych na uczący i testowy"""
        test_len = (1 - self.proportion) * len(self.data)
        while len(self.test) <= test_len:
            rand = random.randint(0,len(self.data)-1)
            self.test.append(self.data[rand])
            self.data.remove(self.data[rand])
    def mean_function(self):
        """Obliczenie średniej """
        #Dla każdej klasy i każdej kolumny liczymy wartość średnią 
        #Stworzenie tablicy o liczbie wierszy odpowiadającej liczbie klas 
        #Oraz liczbie kolumn odpowiadającej liczbie kolumn danych 
        self.mean = np.zeros((len(self.classes),len(self.data[0])))
        #Sumwanie wartości w obrębie klas oraz kolumn 
        for data in self.data:
            for i in range(len(data)-1):
                x = int(data[-1]) #Dana znajdująca się na ostatniej pozycji jest identyfikatorem klasy 
                self.mean[x][i] += data[i]
            self.mean[x][-1] += 1 #Na ostatnej pozycji przechowywujemy liczbę wierszy które sumowaliśmy
        #Obliczenie średniej 
        for i in range(len(self.mean)): 
            for j in range(len(self.mean[i])):
                self.mean[i][j] /= self.mean[i][-1]
                self.mean[i][j] = round(self.mean[i][j],2)
    def standard_deviation(self):
        """Obliczenie odchylenia standardowego dla każdej """
        #Analogicznie do wartości średniej liczymy wartość odchylenia standardowego
        self.stv = np.zeros((len(self.classes),len(self.data[0])))
        for i in range(len(self.data)):
            for j in range(len(self.data[i])-1):
                x = int(self.data[i][-1])
                self.stv[x][j] += math.pow((self.data[i][j] - self.mean[x][j]), 2)
            self.stv[x][-1] += 1
        for i in range(len(self.stv)):
            for j in range(len(self.stv[i])):
                self.stv[i][j] /= self.stv[i][-1]
                self.stv[i][j] = math.sqrt(self.stv[i][j])
                self.stv[i][j] = round(self.stv[i][j], 2)
    def prediction(self):
        """Obliczenie prawdopodobieństwa dla każdego elemetów w zbiorze tetowym, 
            że należy do danej klasy oraz przyporzątkowanie mu klasy z najwyższym 
            prawdopodobieńśwem """
        for i in range(len(self.test)):
            probabilities = []
            for k in range(len(self.classes)):
                probability = 1
                for j in range(len(self.test[i])-1):
                    mean = self.mean[k][j]
                    stv = self.stv[k][j]
                    x = self.test[i][j]
                    #Funkcja gęstości prawdopodobieństwa rozkładu normalnego 
                    if (2 * math.pow(stv, 2)) != 0:
                        expo = math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stv, 2)))) 
                        probability *= (1 / (math.sqrt(2 * math.pi) * stv)) * expo 
                    else:
                        probability = 0
                probabilities.append(probability)
            # Klasyfikacja na podstawie wartości funkcji gęstości prawdopodobieństwa 
            best = 0 
            index = -1 
            for l in range(len(probabilities)):
                if probabilities[l] > best:
                    best = probabilities[l]
                    index = l 
            # Tablica przechowująca prawidłową wartość klasyfikacji 
            self.true.append(self.test[i][-1])
            # Tablica przechowująca przewidywaną wartość klasyfikacji 
            self.pred.append(index)
        
    def confusion_Matrix(self):
        """Wyznaczenie macierzy błędów oraz miar"""
        confusion = confusion_matrix(self.true, self.pred)
        fig = plt.figure(dpi=80)
        ax = fig.add_subplot(1,1,1)
        table = ax.table(cellText=confusion, loc='best', rowLabels = self.classes, 
                            colLabels = self.classes )
        table.set_fontsize(14)
        table.scale(1,4)
        ax.axis('off')
        plt.show()
        print('\nAccuracy: {:.2f}\n'.format(accuracy_score(self.true, self.pred)))
        print('Micro Precision: {:.2f}'.format(precision_score(self.true, self.pred, average='micro')))
        print('Micro Recall: {:.2f}'.format(recall_score(self.true, self.pred, average='micro')))
        print('Micro F1-score: {:.2f}\n'.format(f1_score(self.true, self.pred, average='micro')))
        print('Macro Precision: {:.2f}'.format(precision_score(self.true, self.pred, average='macro')))
        print('Macro Recall: {:.2f}'.format(recall_score(self.true, self.pred, average='macro')))
        print('Macro F1-score: {:.2f}\n'.format(f1_score(self.true, self.pred, average='macro')))
        print('Weighted Precision: {:.2f}'.format(precision_score(self.true, self.pred, average='weighted')))
        print('Weighted Recall: {:.2f}'.format(recall_score(self.true, self.pred, average='weighted')))
        print('Weighted F1-score: {:.2f}'.format(f1_score(self.true, self.pred, average='weighted')))
        print('\nClassification Report\n')
        print(classification_report(self.true, self.pred, target_names=self.classes))

    def draw_ROC(self):
        """Narysowanie krzywej ROC na wykresie"""
        fpr, tpr, thresholds = metrics.roc_curve(self.pred, self.true, pos_label=2)
        roc_auc = metrics.auc(fpr, tpr)
        plt.figure()
        plt.plot(fpr, tpr, label='Krzywa ROC(powierzchnia = %0.2f)' % roc_auc)
        plt.plot([0, 1], [0, 1], 'k--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver operating characteristic ')
        plt.legend(loc="lower right")
        plt.show()
    def diagrams(self,x,y,xlabel,ylabel):
        """Wykresy zależności kolumn badanego zbioru danych """
        colors = {0:'red', 1:'blue', 2:'green'}
        label_red = None
        label_green= None
        label_blue = None
        fig, ax = plt.subplots(figsize=(8, 6))
        for i in range(len(self.data)):
            if label_red == None and self.data[i][-1] == 0:
                plt.scatter(self.data[i][x], self.data[i][y], 
                            c=colors[self.data[i][-1]], label='Iris-setosa')
                label_red = 1 
            if label_blue == None and self.data[i][-1] == 1:
                plt.scatter(self.data[i][x], self.data[i][y], 
                            c=colors[self.data[i][-1]], label='Iris-versicolor')
                label_blue = 1 
            if label_green == None and self.data[i][-1] == 2:
                plt.scatter(self.data[i][x], self.data[i][y], 
                            c=colors[self.data[i][-1]], label='Iris-virginica')
                label_green= 1 
            else:
                plt.scatter(self.data[i][x], self.data[i][y], 
                            c=colors[self.data[i][-1]])          
        ax.legend()
        plt.grid(True)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        ax.set_title("IRIS DATASET CATEGORIZED")
        plt.show()

def main(filename,randomData):
        x = NaiveBayes(filename)
        if randomData:
            x.random_data()
        x.data_conversion()
        x.test_and_traing_set()
        x.mean_function()
        x.standard_deviation()
        x.prediction()
        x.confusion_Matrix()
        x.draw_ROC()


def test_proportions(filename):
    proportions = [0.1,0.2,0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    for proportion in proportions:
        x = NaiveBayes(filename, proportion)
        x.random_data()
        x.data_conversion()
        x.test_and_traing_set()
        x.mean_function()
        x.standard_deviation()
        x.prediction()
        x.confusion_Matrix()
        x.draw_ROC()

def show_diagrams():
    x = NaiveBayes(r"C:\Users\Julka\Downloads\iris.data")
    names = ['petal length', 'petal width', 'sepal length', 
                'sepal width']
    for i in range(len(names)-1):
        x.diagrams(i,i+1,names[i],names[i+1])

main(r"C:\Users\Julka\Downloads\iris.data",False)



            
        

        
