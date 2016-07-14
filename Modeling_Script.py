def run_model():
	"""
	run a gbm on structured data 
	return a list of model ids
	"""

	# required imports
	import h2o
	import numpy as np
	import math
	from h2o.estimators.gbm import H2OGradientBoostingEstimator

	# get structured data from Transform_Data.py
	from Transformation_Script import transform_data

	# returns an h2o dataframe, list of features, and the string response column name
	telco_dataset, features_list, response_name =  transform_data()

	# initialize the GBM estimator
	default_model = H2OGradientBoostingEstimator(model_id = "default_model", seed = 1234)

	# train using the entire dataset with the default model metrics
	default_model.train(x=features_list, y=response_name, training_frame=telco_dataset)

	
	# TO DO: handle different return method if you have multiple models
	return default_model.model_id