import numpy as np
import pandas as pd
from node import Node

class DecisionTreeClassifier():
    def __init__(self, min_samples_split=2, max_depth=2):
        
        # Inicializamos el árbol
        self.root = None

        # Condiciones de parada
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth

    def build_tree(self, dataset, curr_depth=0):

        X, Y = dataset[:,:-1], dataset[:,-1]
        num_samples, num_features = np.shape(X)

        # Separa hasta que se cumplan las condiciones de parada
        if num_samples>=self.min_samples_split and curr_depth<=self.max_depth:

            # Obtiene el mejor split
            best_split = self.get_best_split(dataset, num_samples, num_features)

            # Comprueba si la ganancia de información es positiva
            if best_split["info_gain"]>0:

                # Procesa el nodo izquierdo
                left_subtree = self.build_tree(best_split["dataset_left"], curr_depth+1)

                # Procesa el nodo derecho
                right_subtree = self.build_tree(best_split["dataset_right"], curr_depth+1)

                # Devuelve el nodo de decisión
                return Node(best_split["feature_index"], best_split["threshold"],
                            left_subtree, right_subtree, best_split["info_gain"])
            
        # Computa el nodo hoja
        leaf_value = self.calculate_leaf_value(Y)

        # Devuelve el nodo hoja
        return Node(value=leaf_value)
    
    def get_best_split(self, dataset, num_samples, num_features):

        # Diccionario para almacenar el mejor split
        best_split = {}
        max_info_gain = -float("inf")

        # Itera sobre cada feature
        for feature_index in range(num_features):
            feature_values = dataset[:, feature_index]
            possible_thresholds = np.unique(feature_values)

            # Itera sobre cada feature value presente en el dataset
            for threshold in possible_thresholds:
                # Obtiene el split actual
                dataset_left, dataset_right = self.split(dataset, feature_index, threshold)

                # Combrueba si los hijos no son nulos
                if len(dataset_left) > 0 and len(dataset_right) > 0:
                    y, left_y, right_y = dataset[:, -1], dataset_left[:, -1], dataset_right[:, -1]

                    # Computar la ganancia de información
                    curr_info_gain = self.information_gain(y, left_y, right_y, "gini")

                    # Actualiza el split si la ganancia de información es mayor que la actual
                    if curr_info_gain > max_info_gain:
                        best_split["feature_index"] = feature_index
                        best_split["threshold"] = threshold
                        best_split["dataset_left"] = dataset_left
                        best_split["dataset_right"] = dataset_right
                        best_split["info_gain"] = curr_info_gain
                        max_info_gain = curr_info_gain

        # Devuelve el mejor split
        return best_split
    
    def split(self, dataset, feature_index, threshold):

        # Separa el dataset en dos partes usando el feature_index y el threshold
        dataset_left = np.array([row for row in dataset if row[feature_index]<=threshold])
        dataset_right = np.array([row for row in dataset if row[feature_index]>threshold])
        return dataset_left, dataset_right
    
    def information_gain(self, parent, l_child, r_child, mode="entropy"):

        # Calcula la entropía del padre
        weight_l = len(l_child) / len(parent)
        weight_r = len(r_child) / len(parent)
        if mode=="gini":
            gain = self.gini_index(parent) - (weight_l*self.gini_index(l_child) + weight_r*self.gini_index(r_child))
        else:
            gain = self.entropy(parent) - (weight_l*self.entropy(l_child) + weight_r*self.entropy(r_child))

        return gain
    
    
    def entropy(self,y):

        class_labels = np.unique(y)
        entropy = 0
        for cls in class_labels:
            p_cls = len(y[y==cls]) / len(y)
            entropy += -p_cls * np.log2(p_cls)

        return entropy
    
    def gini_index(self,y):

        class_labels = np.unique(y)
        gini = 0
        for cls in class_labels:
            p_cls = len(y[y==cls]) / len(y)
            gini += p_cls**2

        return 1 - gini
    
    def calculate_leaf_value(self, Y):

        Y = list(Y)
        return max(Y, key=Y.count)
    
    def print_tree(self, tree=None, indent=" "):

        if not tree:
            tree = self.root

        if tree.value is not None:
            print(tree.value)

        else:
            print("X_"+str(tree.feature_index), "<=", tree.threshold, "?", tree.info_gain)
            print("%sleft:" % (indent), end="")
            self.print_tree(tree.left, indent + indent)
            print("%sright:" % (indent), end="")
            self.print_tree(tree.right, indent + indent)

    def fit(self, X, Y):

        dataset = np.concatenate((X, Y), axis=1)
        self.root = self.build_tree(dataset)

    def predict(self, X):
        predictions = [self.make_prediction(x, self.root) for x in X]
        return predictions
    
    def make_prediction(self, x, tree):

        if tree.value!=None: 
            return tree.value

        feature_val = x[tree.feature_index]
        if feature_val<=tree.threshold:
            return self.make_prediction(x, tree.left)
        else:
            return self.make_prediction(x, tree.right)
        
        