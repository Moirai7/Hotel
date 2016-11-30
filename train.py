import pandas as pd
import numpy as np
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,accuracy_score
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import train_test_split

class Train:
	def __init__(self,filename,test = False):
		self.fn = filename
		self.data = self.readData(test)
		self.minOrder = 10
		self.strs = ['']
		pass

	def readData(self,csv):
		if csv:
			return pd.read_csv(self.fn,dtype={'food_name': np.str_,'hotel_id':np.str_},parse_dates=['create_time'])
		else:
			return self.readFromCassandra()

	def showData(self,data):
		data.info()
		print data.head()
		pass

	def processData(self):
		'''
		self.data = self.data[['food_name','hotel_id','create_time']]
		if self.test:
			_test_date = pd.to_datetime('2016-6-1')
			self.test = self.data[self.data['create_time'] >= _test_date]
			self.data = self.data[self.data['create_time'] < _test_date]

		for _hotel_id in self.data.drop_duplicates(['hotel_id'])['hotel_id'] :
			_hotel = self.data[self.data.hotel_id == _hotel_id]
			if len(_hotel)<self.minOrder:
				self.showData(_hotel)
				continue
			#a_df = pd.DataFrame(columns=['count'])
		'''
		pass
	
	def test(self):
		X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size = .3, random_state=1)
		for i in xrange(0,len(self.strs)):
			clf = self.classifiers[i]
			y_pred = clf.predict(X_test,y_test)
			print 'predict#############################'
			print clf
			print accuracy_score(y_test,y_pred)
			print classification_report(y_test, y_pred)
		
	def trainAndSave(self,X_train,y_train):
		self.classifiers = [LogisticRegression(C=1, penalty='l2'),KNeighborsClassifier(),RandomForestClassifier(n_estimators=20, class_weight='balanced'),AdaBoostClassifier(),GaussianNB(),DecisionTreeClassifier(max_depth=5)]

		for i in xrange(0,len(self.strs)):
                	print 'fit##################'
                	self.classifiers[i].fit(X_train, y_train)
			joblib.dump(self.classifiers[i],'result/'+self.strs[i])

	def load(self):
		for i in xrange(0,len(self.strs)):
			self.classifiers[i] = joblib.load('result/'+self.strs[i])

	def trainData(self):
		self.processData()
		self.showData(self.data)

		features = ''
		features = self.data.filter(regex=features)
		target = self.data['']

		self.trainAndSave(features,target)
		pass

	def readFromCassandra(self):
		pass

	def saveFromCassandra(self):
		pass

if __name__ == '__main__':
	train =  Train(filename = 'order_detail.csv',test = True)
	
	train.trainData()
	train.test()
