import pandas as pd
import numpy as np
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def generate_dataset(dataset_name = "simple_dataset"):
    if dataset_name == "simple_dataset":
        data = pd.DataFrame({
            'x_1': [1.0, 0.0, -1.0, 0.0],
            'x_2': [0.0, 1.0, 0.0, -1.0],
            'y': [0, 1, 1, 0]
        })
    if dataset_name == "square_dataset":
        data = pd.DataFrame({
            'x_1': [1.0, 1.0, -1.0, -1.0, 2.0, 2.0, -2.0, -2.0],
            'x_2': [1.0, -1.0, 1.0, -1.0, 2.0, -2.0, 2.0, -2.0],
            'y': [0,0,0,0,1,1,1,1]
        })
    return data

def preprocess_data(data):
    features = np.array(data[data.keys()[:-1]])
    labels = np.array(data[data.keys()[-1]])
    return features, labels

def train_perceptron(features, labels):
    model = LogisticRegression()
    model.fit(features, labels)
    return model

def train_decision_tree(features, labels):
    model = DecisionTreeClassifier()
    model.fit(features, labels)
    return model

def train_svm(features, labels):
    model = SVC()
    model.fit(features, labels)
    return model

def train_model(features, labels, model_name="perceptron"):
    if model_name == "perceptron":
        return train_perceptron(features, labels)
    if model_name == "decisiontree":
        return train_decision_tree(features, labels)
    elif model_name == "svm":
        return train_svm(features, labels)
    else:
        return train_perceptron(features, labels)

def make_predictions(model, features):
    predictions = model.predict(features)
    return predictions

def calculate_accuracy(predictions, labels):
    accuracy = accuracy_score(predictions, labels)
    return accuracy
