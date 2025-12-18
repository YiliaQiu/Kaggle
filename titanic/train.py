

import pandas as pd
import sklearn.metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score



def visualize(data):
    # print(data.columns) # ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp','Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
    print(data.head(5))
    print(len(data),data.info())
    '''
    RangeIndex: 891 entries, 0 to 890
    Data columns (total 9 columns):
    #   Column    Non-Null Count  Dtype  
    ---  ------    --------------  -----  
     0   Pclass    891 non-null    int64  
     1   Sex       891 non-null    object 
     2   Age       714 non-null    float64
     3   SibSp     891 non-null    int64  
     4   Parch     891 non-null    int64  
     5   Ticket    891 non-null    object 
     6   Fare      891 non-null    float64
     7   Cabin     204 non-null    object 
     8   Embarked  889 non-null    object 
    '''
    for col in data.columns:
        print(data[col].dtype) # int64,object,float64
        print("--"* 15)
        if data[col].dtype == object:
           print(data[col].value_counts())
        else:
            print(col, "\r", data[col].describe())

    return

if __name__ == '__main__':
    # get data
    train = pd.read_csv("train.csv")
    # 'Ticket' Variable means ticket num, no use for predicting
    x_columns = ['Pclass', 'Sex', 'Age', 'SibSp','Parch', 'Fare', 'Embarked']
    X = train[x_columns]
    # 查看每个变量的类型和缺失值情况
    # visualize(X)
    # 修改变量类型:pclass改成定性变量
    X["Pclass"].astype("category")
    X["Embarked"].astype("category")
    # 缺失值填充：age, embarked:众数
    age_median = X['Age'].median()
    X.loc[:,"Age_fillna"] = X["Age"].fillna(age_median)
    X.loc[:,"Embarked_fillna"] = X["Embarked"].fillna(X["Embarked"].mode()[0])
    X = X.drop(columns=["Age", "Embarked"])
    # 异常值

    # 再查看每个变量的分布情况
    # print("--"*30)
    # visualize(X)


    # 定性变量进行独热编码
    X_dummies = pd.get_dummies(X, columns=['Sex', 'Embarked_fillna'])
    # print(X_dummies.columns)

    y = train["Survived"]
    X_train, X_test, y_train, y_test = train_test_split(X_dummies, y, test_size=0.5, random_state=0)
    clf = LogisticRegression()
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    print("logistic:", accuracy_score(y_test, y_predict))

    clf = KNeighborsClassifier()
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    print("KNN:", accuracy_score(y_test, y_predict))

    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    print("Decision Tree:", accuracy_score(y_test, y_predict))

    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    print("Random Forest:", accuracy_score(y_test, y_predict))

    clf = svm.SVC()
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    print("svm:", accuracy_score(y_test, y_predict))

    clf = GaussianNB()
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    print("naive bayes:", accuracy_score(y_test, y_predict))

    # # predict
    # test = pd.read_csv("test.csv")
    # x_test = test[x_columns]
    # print(clf.predict(x_test))


