# encoding: utf-8
"""
@author: suns
@contact: sunshuai0518@gmail.com
@time: 2019/7/1 3:22 PM
@file: logistic_regression_with_sklearn.py
@desc:
"""
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 导入 sklearn datasets 中的乳腺癌数据集，标签有'malignant', 'benign'两个，可以作为二分类的数据集
# 属性值有'mean smoothness', 'mean compactness', 'mean concavity',
#        'mean concave points', 'mean symmetry', 'mean fractal dimension',
#        'radius error', 'texture error', 'perimeter error', 'area error',
#        'smoothness error', 'compactness error', 'concavity error',
#        'concave points error', 'symmetry error',
#        'fractal dimension error', 'worst radius', 'worst texture',
#        'worst perimeter', 'worst area', 'worst smoothness',
#        'worst compactness', 'worst concavity', 'worst concave points',
#        'worst symmetry', 'worst fractal dimension'
breast_cancer = datasets.load_breast_cancer()

print(breast_cancer)

X = breast_cancer.data
y = breast_cancer.target

# 划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

# 使用 sklearn 的 LogisticRegression 作为模型，其中有 penalty，solver，dual 几个比较重要的参数，不同的参数有不同的准确率，这里为了简便都使用默认的，详细的请参考 sklearn 文档
model = LogisticRegression(solver='liblinear')

# 拟合
model.fit(X_train, y_train)

# 预测测试集
predictions = model.predict(X_test)

# 打印准确率
print('测试集准确率：', accuracy_score(y_test, predictions))

# 找一个数据测试一下
print('测试集的第10个的预测值：', model.predict([X_test[9]]))
print('测试集的第10个的真实值：', y_test[9])
