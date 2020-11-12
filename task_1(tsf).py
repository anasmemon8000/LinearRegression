# -*- coding: utf-8 -*-
"""Task 1(TSF).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13vPkHfFWm_8J6dPiXRQe2r6PKQ1ChBP8

#**STEP 1. Importing Libraries**

---
"""
# Name : Anas Asif Vichhy
# institution : Sardar Patel College of Engineering, Mumbai
# Data Sience and Business Anaysis Intern at The Sparks Foundation (TSF) at GRIP.
# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

"""#**STEP 2. Reading Data**

---
"""

url = 'https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv'
data = pd.read_csv(url)
print("-----Data Import Successful-----")
data.head()

"""#**STEP 3. Distribution of Imported Data**

---
"""

plot = data.plot(x = 'Hours', y = 'Scores', style='^')
plt.xlabel('Hours studied')
plt.ylabel('Pecentage score')
plt.title('hours vs percentage')
plt.draw()

"""#**STEP 4. Data Preparation**

---
"""

X = data.iloc[:,:-1].values
y = data.iloc[:,1].values
X,y

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=50
)

"""#**STEP 5. Training the Algorithm**

---
"""

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(X_train,y_train)
print('----Training Successful-----')

line = reg.coef_*X+ reg.intercept_
plt.scatter(X,y)
plt.plot(X,line)
plt.xlabel('Hours studied')
plt.ylabel('Pecentage score')
plt.title('hours vs percentage')
plt.draw()

"""#**STEP 6. Making Predictions**

---
"""

print(X_test) # Testing data - In Hours
y_pred = reg.predict(X_test) # Predicting the scores

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df

"""#**STEP 7. Testing the Data**

---
"""

#Testing the Algorithm to obtain score corresponding to study of 9.25 Hours.
hours = [[9.25]]
own_pred = reg.predict(hours)
print("No of Hours = {}".format(hours))
print("Predicted Score = {}".format(own_pred[0]))

"""#**STEP 8. Algorithm Evaluation**

---
"""

from sklearn import metrics
#metrics.accuracy_score(y_test, y_pred)
print('Mean Absolute Error:', 
      metrics.mean_absolute_error(y_test, y_pred))
