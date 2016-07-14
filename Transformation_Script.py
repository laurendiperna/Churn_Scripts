def transform_data():
	"""
	Imports a structured dataset and adds new features.
	returns: 
	frame - the telco_dataset structured dataframe with newly created features
	features_list - the list of features
	response_name - the response column name 
	"""

	# required imports
	import h2o
	import numpy as np
	import math

	# initialize h2o using all cores
	h2o.init(nthreads = -1)

	# get dataset from Import_Unstructured_Data.py
	from Extraction_Script import read_datasource

	# get the structured pandas dataframe 
	pandas_dataset = read_datasource()

	# get a list of the column names (before you covert to an h2o frame) to replace the h2o headers,
	# which replace the pandas dataframe headers when you covert to an h2o frame
	columns_names = list(pandas_dataset.columns)

	# convert to an h2o frame
	telco_dataset = h2o.H2OFrame(pandas_dataset)
	# overwrite the h2o column headers with the original column headers
	telco_dataset.columns = columns_names

	# update the telco data format: 
	# change SeniorCitizen to 'yes'/ 'no'
	telco_dataset['SeniorCitizen'] = (telco_dataset['SeniorCitizen'] == 1).ifelse('Yes','No')
	# Add the same form of capitalization across variables
	# columns changed were: customerID, gender, tenure
	telco_dataset.columns =[u'CustomerID',
	 u'Gender',
	 u'SeniorCitizen',
	 u'Partner',
	 u'Dependents',
	 u'Tenure',
	 u'PhoneService',
	 u'MultipleLines',
	 u'InternetService',
	 u'OnlineSecurity',
	 u'OnlineBackup',
	 u'DeviceProtection',
	 u'TechSupport',
	 u'StreamingTV',
	 u'StreamingMovies',
	 u'Contract',
	 u'PaperlessBilling',
	 u'PaymentMethod',
	 u'MonthlyCharges',
	 u'TotalCharges',
	 u'Churn']


	# add a column to check if people use automatic bank transfers as their payment method
	telco_dataset['Bank transfer (automatic)'] = (telco_dataset['PaymentMethod'] == 'Bank transfer (automatic)').ifelse(1,0)

	 

	 # get a list of the features, remove customerid and churn columns
	features_list = telco_dataset.columns
	features_list.remove('Churn')
	features_list.remove('CustomerID')
	# get the response column name
	response_name = 'Churn'

	return telco_dataset, features_list, response_name 
