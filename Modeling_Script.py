def run_model():
	"""
	Runs a GBM on a structured data set
	returns:
		 a list of model ids
	"""

	# required imports
	import h2o
	import json

	# get structured data from Transform_Data.py
	from Transformation_Script import transform_data

	# returns an h2o dataframe, list of features, and the string response column name
	telco_dataset, features_list, response_name =  transform_data()

	# initialize the GBM estimator
	default_gbm = h2o.H2OGradientBoostingEstimator(model_id = "default_gbm", seed = 1234)
	default_glm = h2o.H2OGeneralizedLinearEstimator(model_id = "default_glm", seed = 1234)
	default_dl = h2o.H2ODeepLearningEstimator(model_id = "default_dl", seed = 1234)

	# train using the entire dataset with the default model metrics
	default_gbm.train(x=features_list, y=response_name, training_frame=telco_dataset)
	default_glm.train(x=features_list, y=response_name, training_frame=telco_dataset)
	default_dl.train(x=features_list, y=response_name, training_frame=telco_dataset)

	#Print out all model ids and print out list of model ids
	print("Default GBM Model ID: %s" % default_gbm.model_id)
	print("Default GLM Model ID: %s" % default_glm.model_id)
	print("Default DL Model ID: %s" % default_dl.model_id)
	
	model_id_list = [default_gbm.model_id,default_glm.model_id,default_dl.model_id]
	print("All Model IDs as a list: %s" % model_id_list)
	# uncomment the block below to get alternative print out method
	# print("<< END_TEXT")
	# print(json.dumps({"jsonrpc":"2.0", "result":[default_gbm.model_id]}))
	# print("END_TEXT")
	return model_id_list

if __name__ == '__main__':
    run_model()