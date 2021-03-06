import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

dataset = pandas.read_csv(url, names=names)

#1Statistical summary
#1.1 to get size
print "Dataset shape"
print dataset.shape
#1.2 to get first 20 elements
print "Getting first 20 elements in dataset"
print dataset.head(20)
#1.3 to get description about the dataset
print "Getting description about the dataset"
print dataset.describe()

#2Class distribution
#2.1 grouping the number of rows based on class
print dataset.groupby('class').size()

#3Datavizualisation
#3.1 univariate plots(plots of each individual variable)
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()
#3.2 histogram
dataset.hist()
plt.show()

#4Mutivariate plots(scatterplots of all pairs of attributes)
scatter_matrix(dataset)
plt.show()

#5Evaluation of some algorithms
#5.1 Creating a validation dataset
#split out validation dataset
array = dataset.values
print "printing dataset values"
print array
x = array[:,0:4]
print "printing x"
print x
y = array[:,4]
print "printing y"
print y 
validation_size = 0.20
seed = 7
scoring = 'accuracy'
x_train, x_validation, y_train, y_validation = model_selection.train_test_split(x, y, test_size=validation_size, random_state=seed)

print "printing x train"
print x_train
print len(x_train)

print "prnting x_validation"
print x_validation
#5.2 Using 10 fold cross validation to estimate accuracy


#5.3 Build Models
#The Algorithms we are going to use to predict the evaluation
#Logistic Regression(LR)
#Linear Discriminant Analysis(LDA)
#K Nearest Neighbors(KNN)
#Classification and Regression Trees(CART)
#Gaussian Naive Bayes(NB)
#Suppor Vector Machines(SVM)

#So here Linear algorithms are (LR and LDA) non linear algorithms are (KNN, CART, NB, SVM)
#spot check algorithms
models = []

#from sklearn.linear_model import LogisticRegression
models.append(('LR', LogisticRegression()))

#from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
models.append(('LDA', LinearDiscriminantAnalysis()))

#from sklearn.neighbors import KNeighborsClassifier
models.append(('KNN', KNeighborsClassifier()))

#from sklearn.tree import DecisionTreeClassifier 
models.append(('CART', DecisionTreeClassifier()))

#from sklearn.naive_bayes import GaussianNB
models.append(('NB', GaussianNB()))

#from sklearn.svm import SVC
models.append(('SVM', SVC()))

results = []
names = []

for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, x_train, y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print (msg)

#Compare Algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()	

#6 Make Predictions
knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
predictions = knn.predict(x_validation)
print accuracy_score(y_validation, predictions)
print confusion_matrix(y_validation, predictions)
print classification_report(y_validation, predictions) 

