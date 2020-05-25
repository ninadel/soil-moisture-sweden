# dataset class
class Dataset(object)
	""" 
	Parameters
		data: pandas dataframe
		network: in-situ network name
		station: in-situ station name
		start_date: datetime
		end_date: datetime
	"""
	
	def __init__(self, data, network, station, start_date, end_date) 
		self.data = data
		self.network = network
		self.station = station
		self.startdate = start_date
		self.end_date = end_date
	
	def get_data(years = [2015, 2016, 2017, 2018], months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
		""" 
		Parameters
			years: list of years, default 2015-2018
			data_type: list of months, default 1-12
		"""

# classes for each type?
# class GLDAS(Dataset)
# class SMAP_L3(Dataset)
	