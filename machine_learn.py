import scipy as sp
import numpy as np
import build
from sklearn import model_selection, preprocessing, feature_selection, ensemble, linear_model, metrics, decomposition

model = ensemble.GradientBoostingClassifier()

param_dic = {'learning_rate':[0.15,0.1,0.05,0.01,0.005,0.001],      #weighting factor for the corrections by new trees when added to the model
'n_estimators':[100,250,500,750,1000,1250,1500,1750],  #number of trees added to the model
'max_depth':[2,3,4,5,6,7],    #maximum depth of the tree
'min_samples_split':[2,4,6,8,10,20,40,60,100],    #sets the minimum number of samples to split
'min_samples_leaf':[1,3,5,7,9],     #the minimum number of samples to form a leaf
'max_features':[2,3,4,5,6,7],     #square root of features is usually a good starting point
'subsample':[0.7,0.75,0.8,0.85,0.9,0.95,1]} 


x_values = ["do_manual_check",
                "ext_toDelete",
                "is_doc", 
                "is_pic",
                "is_coding_file", 
                "is_vid", 
                "is_mp3", 
                "is_shortcut",
                "is_folder",
                "is_unclassified",
                "name_length",
                "num_spaces",
                "num_real_words",
                "file_size",
                "days_since_created",
                "is_duplicate"]

data = build.get_data()


data_train, data_test = model_selection.train_test_split(data,test_size = 0.1)


# seperate date into train and test set
x_train = data_train[x_values]
y_train = data_train["delete_file"]

x_test = data_test[x_values]
y_test = data_test["delete_file"]



random_search = model_selection.RandomizedSearchCV(model, 
       param_distributions=param_dic, n_iter=10, 
       scoring="accuracy").fit(x_train, y_train)

print("Best Model parameters:", random_search.best_params_)
print("Best Model mean accuracy:", random_search.best_score_)
model1 = random_search.best_estimator_

model1.fit(x_train,y_train)

predicted_prob = model1.predict_proba(x_test)[:,1]
predicted = model1.predict(x_test)
accuracy = metrics.accuracy_score(y_test,predicted)

print(accuracy)