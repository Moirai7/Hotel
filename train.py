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
		if self.test:
			_test_date = pd.to_datetime('2016-6-1')
			self.test = self.data[self.data['create_time'] >= _test_date]
			self.data = self.data[self.data['create_time'] < _test_date]
		pass

	def trainData(self):
		self.processData()
		self.showData(self.data)

		for _hotel_id in self.data.drop_duplicates(['hotel_id'])['hotel_id'] :
			_hotel = self.data[self.data.hotel_id == _hotel_id]
			if len(_hotel)<self.minOrder:
				self.showData(_hotel)
				continue
			_df = pd.DataFrame(columns=['count'])
			
		pass

if __name__ == '__main__':
	train =  Train(filename = 'order_detail.csv',test = True)
	train.trainData()
