import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import style
style.use("ggplot")
from sklearn import svm,decomposition
from sklearn.neural_network import MLPClassifier
# from data_processing import process

import pickle
from sklearn.externals import joblib

data = pd.read_csv('train_data.csv' , header = 0)
output = pd.read_csv('output.csv' , header = 0)
data = data.values
output = output.values

traindata = data[0:30, :]
y_train = output[0:30, :]
# testdata = 
# y_test = output[30:,:] 
# x=[[1 1 1],[1,1,1]]
# y=[0,1,0,1]
#########CLASSIFIER#############
# clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(100,50), random_state=1)
clf = svm.SVC(kernel="rbf")
# print clf.fit(traindata,y_train)
# print ("hi")
# s = pickle.dumps(clf)
joblib.dump(clf, 'svm_model.pkl') 

# predictedlabels = clf.predict(testdata)
# print predictedlabels
# print y_test
# confusion_matrix = np.zeros((num_classes,num_classes))
# for i in range(len(predictedlabels)):
# 	actual_label = test.actuallabel[i]
# 	predicted_label = predictedlabels[i]
# 	confusion_matrix[actual_label-1][predicted_label-1]+=1

# print "*********Confusion Matrix*********\n", confusion_matrix,"\n**********************************\n"
# # for i in range(num_classes):
# total_test_data = len(test.dataset)
# acc=float(0)
# for i in range(num_classes):
# 	acc += confusion_matrix[i][i]
# acc /= float(total_test_data)
# print "Accuracy = ",acc

 
