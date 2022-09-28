import os
import pandas as pd
import matplotlib.pyplot as plt
plt.rc("font", size=14)
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)


data = pd.read_csv('./data/bankchurn.csv',header=0)
print(data.shape)
print(list(data.columns))

dataFrame = pd.DataFrame(data)
print(dataFrame.head())

newdf = dataFrame.drop(['customer_id'],axis=1)
print(newdf.head())

# Data Exploration
print(newdf['churn'].value_counts())

# # Show the churn values in plot
# sns.countplot(x='churn',data=newdf, palette='hls')
# plt.show()
# plt.savefig('count_plot')

# Check the data based on churn values
print(newdf.groupby('churn').mean(numeric_only=True))

# Check the data based on age values
print(newdf.groupby('age').mean(numeric_only=True))

# Check the data based on tenure values
print(newdf.groupby('tenure').mean(numeric_only=True))

# Check the data based on products values
print(newdf.groupby('products_number').mean(numeric_only=True))



pd.crosstab(newdf.products_number,newdf.churn).plot(kind='bar')
plt.title('Churn Frequency for Products')
plt.xlabel('Product')
plt.ylabel('Frequency of Churn')
# plt.show()
plt.savefig('Churn_frq_Product')

# Check the data based on Country values
print(newdf.groupby('country').mean(numeric_only=True))

pd.crosstab(newdf.country,newdf.churn).plot(kind='bar')
plt.title('Churn Frequency for Country')
plt.xlabel('Country')
plt.ylabel('Frequency of Churn')
# plt.show()
plt.savefig('Churn_frq_Country')

cat_vars=['country','gender','tenure','products_number','credit_card','active_member']
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(newdf[var], prefix=var)
    newdf1 =newdf.join(cat_list)
    newdf=newdf1
    # print(list(newdf.columns))

cat_vars=['country','gender','tenure','products_number','credit_card','active_member']
data_vars=newdf.columns.values.tolist()
to_keep=[i for i in data_vars if i not in cat_vars]
# print(to_keep)

data_final=newdf[to_keep]
print(data_final.columns.values)

data_final_vars=data_final.columns.values.tolist()
y=['churn']
X=[i for i in data_final_vars if i not in y]

#  Feature Selection
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()

rfe = RFE(logreg,n_features_to_select=18)
rfe = rfe.fit(data_final[X], data_final[y])
print(rfe.support_)
print(rfe.ranking_)

# ['credit_score' 'age' 'balance' 'estimated_salary' 'churn'
#  'country_France' 'country_Germany' 'country_Spain' 'gender_Female'
#  'gender_Male' 'tenure_0' 'tenure_1' 'tenure_2' 'tenure_3' 'tenure_4'
#  'tenure_5' 'tenure_6' 'tenure_7' 'tenure_8' 'tenure_9' 'tenure_10'
#  'products_number_1' 'products_number_2' 'products_number_3'
#  'products_number_4' 'credit_card_0' 'credit_card_1' 'active_member_0'
#  'active_member_1']
# [False False False False  True  True  True  True  True  True False False
#   True False  True False  True  True False False  True  True  True  True
#   True  True  True  True]
# [ 7  3  8 11  1  1  1  1  1  1  4  6  1  9  1  5  1  1  2 10  1  1  1  1
#   1  1  1  1]

# Select only those columns where true come in previous command rfe.support_

selected_cols= ['country_France', 'country_Germany', 'country_Spain' ,'gender_Female',
 'gender_Male', 'tenure_0','tenure_3','tenure_5', 'tenure_7', 'tenure_8',
 'products_number_1' ,'products_number_2' ,'products_number_3',
  'products_number_4' ,'credit_card_0', 'credit_card_1', 'active_member_0',  'active_member_1']

changed_selected_cols= ['country_France', 'country_Germany', 'country_Spain',
                        'tenure_0','tenure_3','tenure_5', 'tenure_7', 'tenure_8',
                        'products_number_1' ,'products_number_2' ,'products_number_3',
                        'products_number_4']

X=data_final[changed_selected_cols]
y=data_final['churn']

# Implementing models

import statsmodels.api as sm
logit_model=sm.Logit(y,X)
result=logit_model.fit()
print(result.summary())

# The p-values for most of the variables are very small, therefore, most of them are significant to the model.

# Logistic Regression Model Fitting

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

# Predicting the test set results and caculating the accuracy

y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))
# Accuracy of logistic regression classifier on test set: 0.82

# Cross Validation

from sklearn import model_selection
from sklearn.model_selection import cross_val_score
kfold = model_selection.KFold(n_splits=10, random_state=7,shuffle=True)
modelCV = LogisticRegression()
scoring = 'accuracy'
results = model_selection.cross_val_score(modelCV, X_train, y_train, cv=kfold, scoring=scoring)
print("10-fold cross validation average accuracy: %.3f" % (results.mean()))
# 10-fold cross validation average accuracy: 0.820

#Confusion Matrix

from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)

# [[2365   14]
#  [ 528   93]]

# Compute precision, recall, F-measure and support
# The precision is the ratio tp / (tp + fp) where tp is the number of true positives and fp the number of false positives. The precision is intuitively the ability of the classifier not to label as positive a sample that is negative.
#
# The recall is the ratio tp / (tp + fn) where tp is the number of true positives and fn the number of false negatives. The recall is intuitively the ability of the classifier to find all the positive samples.
#
# The F-beta score can be interpreted as a weighted harmonic mean of the precision and recall, where an F-beta score reaches its best value at 1 and worst score at 0.
#
# The F-beta score weights recall more than precision by a factor of beta. beta == 1.0 means recall and precision are equally important.
#
# The support is the number of occurrences of each class in y_test.

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))


# ROC Curve from sklearn import metrics

from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
logit_roc_auc = roc_auc_score(y_test, logreg.predict(X_test))
fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test)[:,1])
plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.savefig('Log_ROC')
plt.show()










