import pandas as pd
import numpy as np

class Train:
	def __init__(self,filename,test = False):
		self.fn = filename
		self.data = self.readData()
		self.test = test
		self.minOrder = 10
		pass

	def readData(self):
		return pd.read_csv(self.fn,dtype={'food_name': np.str_,'hotel_id':np.str_},parse_dates=['create_time'])

	def showData(self,data):
		data.info()
		print data.head()
		pass

	def processData(self):
		self.data = self.data[['food_name','hotel_id','create_time']]
		pass

	def trainData(self):
		self.processData()
		self.showData(self.data)
		for hotel in self.data.drop_duplicates(['hotel_id'])['hotel_id'] :
			x_train = self.data[self.data.hotel_id == hotel]
			if len(x_train)<self.minOrder:
				self.showData(x_train)
				continue
			
		pass

if __name__ == '__main__':
	train =  Train(filename = 'order_detail.csv',test = True)
	train.trainData()
