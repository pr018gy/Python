import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

# Load data
X, y = load_breast_cancer(return_X_y=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Set up GridSearchCV 
param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [1, 0.1, 0.01, 0.001]}
grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=2)

# Grid search
grid.fit(X_train, y_train)

# Best model
clf = grid.best_estimator_

# Evaluate model
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Get support vectors
support_vectors = X[clf.support_]
print("Support vectors:", support_vectors)

# Number of SVs per class
num_sv_per_class = {i:0 for i in np.unique(y)} 
for i in clf.support_:
    num_sv_per_class[y[i]] += 1
    
print("Num SVs per class:", num_sv_per_class)
print("Number of candidates tried in each iteration:", halving_cv.n_candidates_)
print("Best parameters:", halving_cv.best_params_)
