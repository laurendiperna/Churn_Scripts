
def read_datasource():
	"""
	This function imports an unstructured data set from a json file
	returns: Pandas Dataframe
	"""
	# required imports
	import pandas as pd 

	# get s3 link to dataset
	# original dataset comes from ibm watson analytics
	# https://community.watsonanalytics.com/wp-content/uploads/
	# 2015/03/WA_Fn-UseC_-Telco-Customer-Churn.csv
	data_source = "https://s3.amazonaws.com/h2o-datasets/churn/unstructure_churn_dataset.json.txt"

	# import and convert json to pandas frame
	dataset = pd.read_json(data_source)

	return dataset